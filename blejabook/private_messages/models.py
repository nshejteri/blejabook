from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class MessageManager(models.Manager):
	"""
	"""
	def message_thread_for(self, user, msg, messages=[]):
		"""
		"""
		print("POSLAO PORUKU %s " % msg.pk)
		if not msg.parent_msg:
			print("KRAJ %s" % msg.pk) 
			messages.append(msg)
			return messages
		else:
			messages.append(msg)
			message = Message.objects.get(pk=msg.parent_msg.pk)
			return self.message_thread_for(message)

class Message(models.Model):
	"""
	Private messages model (from user to user)
	"""
	message_text = models.TextField(_("Message_text"))
	sender = models.ForeignKey(User, related_name='sent_messages', verbose_name=_("Sender"))
	recipient = models.ForeignKey(User, related_name='received_messages', null=True, blank=True, verbose_name=_('Recipient'))
	parent_msg = models.ForeignKey('self', related_name='next_messages', null=True, blank=True, verbose_name=_("Parent message"))
	sent_at = models.DateTimeField(_("Sent at"), null=True, blank=True)
	read_at = models.DateTimeField(_("Read at"), null=True, blank=True)
	replied_at = models.DateTimeField(_("Replied at"), null=True, blank=True)
	sender_deleted_at = models.DateTimeField(_("Sender deleted at"), null=True, blank=True)
	recipient_deleted_at = models.DateTimeField(_("Recipient deleted at"), null=True, blank=True)

	objects = MessageManager()

	class Meta:
		ordering = ('-sent_at',)

	def __str__(self):
		return 'ID: %s -- Sender: %s -- Recipient: %s -- Sent at: %s' % (self.pk, self.sender.pk, self.recipient.pk, self.sent_at)