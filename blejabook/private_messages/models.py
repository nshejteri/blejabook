from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Message(models.Model):
	"""
	Private messages model (from user to user)
	"""
	message_text = models.TextField(_("Message_text"))
	sender = models.ForeignKey(User, related_name='sent_messages', verbose_name=_("Sender"))
	recipient = models.ForeignKey(User, related_name='received_messages', null=True, blank=True, verbose_name='Recipient')
	parent_msg = models.ForeignKey('self', related_name='next_messages', null=True, blank=True, verbose_name=_("Parent message"))
	sent_at = models.DateTimeField(_("sent at"), null=True, blank=True)
	read_at = models.DateTimeField(_("read at"), null=True, blank=True)
	replied_at = models.DateTimeField(_("replied at"), null=True, blank=True)
	sender_deleted_at = models.DateTimeField(_("Sender deleted at"), null=True, blank=True)
	recipient_deleted_at = models.DateTimeField(_("Recipient deleted at"), null=True, blank=True)

