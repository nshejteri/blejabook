from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class MessageManager(models.Manager):
	"""
	Manager klasa koja sadrzi funkcije za pristup bazi podataka radi preuzimanja podataka o nitima korisnika
	i porukama koje su sadrzane u nitima.
	"""
	def get_user_threads(self, user):
		"""
		Funkcija koja SQL upitom vraca listu niti (Thread-ova) iz baze podataka za logovanog korisnika.
		"""
		from django.db import connection
		cursor = connection.cursor()

		cursor.execute("""
			SELECT t.id, t.participant_a_id, t.participant_b_id, m.id AS msg_id, m.message_text, m.sent_at,
			m.sender_id, m.recipient_id, COUNT(t.id) AS msg_num, d.deleted_by_id, d.id_of_last_del_msg_id FROM private_messages_thread t
			JOIN private_messages_msg m ON m.thread_id = t.id
			LEFT JOIN private_messages_deletedmessages d ON d.thread_id = m.thread_id
			AND (m.sender_id=d.deleted_by_id OR m.recipient_id=d.deleted_by_id)
			AND d.id_of_last_del_msg_id >= m.id AND d.deleted_by_id = %s
			WHERE (t.participant_a_id = %s OR t.participant_b_id = %s) 
			AND d.deleted_by_id IS NULL GROUP BY t.id ORDER BY -m.sent_at""", [user.pk, user.pk, user.pk])

		result_list = []
		
		for row in cursor.fetchall():
			p = self.model(id=row[0], message_text=row[4], sender=User.objects.get(pk=row[6]), recipient=User.objects.get(pk=row[7]))
			p.sent_at = row[5]
			p.message_num = row[8]
			p.last_msg_id = row[3]
			result_list.append(p)

		return result_list

	def get_thread_messages(self, user, thread_id):
		"""
		Funkcija koja SQL upitom vraca listu poruka logovanog korisnika koje pripadaju odabranoj niti (Thread-u)
		"""
		from django.db import connection
		cursor = connection.cursor()

		cursor.execute("""
			SELECT t.id, m.message_text, m.sent_at, m.read_at,
			m.sender_id, m.recipient_id FROM private_messages_thread t
			JOIN private_messages_msg m ON m.thread_id = t.id
			LEFT JOIN private_messages_deletedmessages d ON d.thread_id = m.thread_id
			AND (m.sender_id=d.deleted_by_id OR m.recipient_id=d.deleted_by_id)
			AND d.id_of_last_del_msg_id >= m.id AND d.deleted_by_id = %s
			WHERE (t.participant_a_id = %s OR t.participant_b_id = %s) 
			AND d.deleted_by_id IS NULL AND t.id = %s""", [user.pk, user.pk, user.pk, thread_id])

		result_list = []
		
		for row in cursor.fetchall():
			p = self.model(id=row[0], message_text=row[1], sender=User.objects.get(pk=row[4]), recipient=User.objects.get(pk=row[5]))
			p.sent_at = row[2]
			p.read_at = row[3]
			result_list.append(p)

		return result_list

"""
class MessageManager(models.Manager):

	def thread_messages(self, msg, messages=None):

		if messages is None:
			messages = []
		
		if not msg.parent_msg:
			messages.append(msg)
			return messages
		else:
			messages.append(msg)
			message = Message.objects.get(pk=msg.parent_msg.pk)
			return self.thread_messages(message, messages)

	def get_threads(self, user):

		from django.db import connection
		cursor = connection.cursor()

		cursor.execute('''
			SELECT * FROM 
			(SELECT id, message_text, sender_id, recipient_id, 
				MIN(sender_id, recipient_id) AS x, 
				MAX(sender_id, recipient_id) AS y, sent_at, COUNT(id) AS message_num, sender_deleted_at, recipient_deleted_at
			FROM private_messages_message GROUP BY x, y) WHERE (sender_id=%s AND sender_deleted_at IS NULL) OR (recipient_id=%s AND recipient_deleted_at IS NULL) ORDER BY -sent_at''', [user.pk, user.pk])
		result_list = []
		
		for row in cursor.fetchall():
			p = self.model(id=row[0], message_text=row[1], sender=User.objects.get(pk=row[2]), recipient=User.objects.get(pk=row[3]))
			p.sent_at = row[6]
			p.message_num = row[7]
			p.sender_deleted_at = row[8]
			p.recipient_deleted_at = row[9]
			result_list.append(p)
		return result_list

class Message(models.Model):

	#Private messages model (from user to user)

	message_text = models.TextField(_("Message_text"))
	sender = models.ForeignKey(User, related_name='sent_messages', verbose_name=_("Sender"))
	recipient = models.ForeignKey(User, related_name='received_messages', null=True, blank=True, verbose_name=_('Recipient'))
	parent_msg = models.ForeignKey('self', related_name='next_messages', null=True, blank=True, verbose_name=_("Parent message"))
	sent_at = models.DateTimeField(_("Sent at"), null=True, blank=True)
	read_at = models.DateTimeField(_("Read at"), null=True, blank=True)
	sender_deleted_at = models.DateTimeField(_("Sender deleted at"), null=True, blank=True)
	recipient_deleted_at = models.DateTimeField(_("Recipient deleted at"), null=True, blank=True)

	objects = MessageManager()

	class Meta:
		ordering = ('-sent_at',)

	def __str__(self):
		return 'ID: %s -- Sender: %s -- Recipient: %s -- Sent at: %s' % (self.pk, self.sender.pk, self.recipient.pk, self.sent_at)
"""

class Thread(models.Model):
	"""
	Model koji reprezentuje nit (thread) koji sadrzi sve poruke (dijalog) izmedju dva korisnika.
	Ucesnici dialoga su participant_a i participant_b i moze biti iskljucivo jedan takav par u tabeli.
	"""
	created_at = models.DateTimeField(_('created at'))
	participant_a = models.ForeignKey(User, related_name='participant_a', verbose_name='participant a')
	participant_b = models.ForeignKey(User, related_name='participant_b', verbose_name='participant b')

	class Meta:
		unique_together= ('participant_a', 'participant_b')

class Msg(models.Model):
	"""
	Model koji reprezentuje poruku u privatnoj komunikaciji korisnika.
	"""
	message_text = models.TextField(_('message_text'))
	sender =models.ForeignKey(User, related_name='sent_messages', verbose_name=_('sender'))
	recipient = models.ForeignKey(User, related_name='received_messages', verbose_name=_('recipient'))
	sent_at = models.DateTimeField(_('sent at'), blank=True)
	read_at = models.DateTimeField(_('read at'), null=True, blank=True)
	thread = models.ForeignKey(Thread, related_name='thread_messages', verbose_name=_('thread'))

	objects = MessageManager()

	class Meta:
		ordering = ('-sent_at',)

class DeletedMessages(models.Model):
	"""
	Model koji povezuje korisnika, poruku i nit (thread) radi evidencije poruka u niti koje je korisnik obrisao 
	iz svog inboxa. Evidentira se korisnik koji je izvrsio brisanje, vreme kada je izvrseno brisanje,
	ID poslednje poruke u niti koja se brise i ID niti kojoj pripadaju poruke koje se brisu.
	"""
	deleted_by = models.ForeignKey(User, related_name='deleted_messages', verbose_name='deleted by')
	deleted_at = models.DateTimeField(_('deleted at'))
	id_of_last_del_msg = models.ForeignKey(Msg, verbose_name='ID of last deleted message')
	thread = models.ForeignKey(Thread, verbose_name='thread ID of deleted messages')

