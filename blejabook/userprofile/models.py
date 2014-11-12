from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class UserProfile(models.Model):

	user = models.OneToOneField(User)
	date_of_birth = models.DateField('Date of birth', default=datetime(1900, 01, 01, 0, 0))
	gender = models.CharField(max_length=1, choices=(('m', 'Male'), ('f', 'Female')))
	country = models.CharField(max_length=30)
	city = models.CharField(max_length=30)

	User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])