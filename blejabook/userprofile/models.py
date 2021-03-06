from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.sites.models import Site
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse, NoReverseMatch
from django.core.cache import cache
import os
import uuid

# Create your models here.
def generate_new_filename(instance, filename):
	"""
	"""
	f, ext = os.path.splitext(filename)
	return "profile/%s_%s%s" % (instance.user.username, uuid.uuid4(), ext)

class EmailConfirmationManager(models.Manager):

	def send_confirmation(self, request, user):
		
		confirmation_key = user.profile.confirmation_key
		current_site = Site.objects.get_current()
		protocol = getattr(settings, 'DEFAULT_HTTP_PROTOCOL', 'http')
		path = reverse('userauth.views.confirm_email', args=[confirmation_key])
		uri = request.build_absolute_uri(path)
		activate_url = protocol + ':' + uri.partition(':')[2]

		context = {
			'user': user,
			'activate_url': activate_url,
			'current_site': current_site,
			'confirmation_key': confirmation_key,
		}

		subject = render_to_string('account/email_confirmation_subject.txt', context)
		subject = "".join(subject.splitlines())
		message = render_to_string('account/email_confirmation_message.txt', context)

		send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])

	def is_key_expired(self):
		pass

	def confirm_email(self, confirmation_key):
		
		try:
			user_profile_to_confirm = self.get(confirmation_key=confirmation_key)
		except self.model.DoesNotExist:
			return None

		if user_profile_to_confirm is not None and not user_profile_to_confirm.verified:
			user_profile_to_confirm.verified = True
			user_profile_to_confirm.save()

class UserProfile(models.Model):

	user = models.OneToOneField(User, related_name='profile')
	name = models.CharField('First-Last Name', max_length=40, default='')
	date_of_birth = models.DateField('Date of birth', default=datetime(1900, 01, 01, 0, 0))
	gender = models.CharField(max_length=1, choices=(('m', 'Male'), ('f', 'Female')))
	country = models.CharField(max_length=30)
	city = models.CharField(max_length=30)
	profile_image = models.ImageField('profile image', upload_to=generate_new_filename, default='', null=True, blank=True)
	verified = models.BooleanField(default=False)
	confirmation_key = models.CharField(max_length=60, default='')

	User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

	objects = EmailConfirmationManager()

	def online(self):
		"""
		Funkcija vraca 'True' ako je korisnik online u suprotnom vraca 'None'.
		"""
		return cache.get('online-%s' % self.user.id)

	def num_of_online(self):
		"""
		Funkcija vraca broj online korisnika.
		"""
		return len(cache.get('online_now'))


