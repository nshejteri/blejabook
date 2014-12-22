from django.shortcuts import render
from django.shortcuts import redirect
from private_messages.forms import ComposeMessageForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.views.generic import UpdateView, ListView 
from django.http import HttpResponse
from private_messages.models import Msg
from private_messages.models import Thread
from private_messages.models import DeletedMessages
from django.utils import timezone
from django.db.models import Q
from django.db.models import Max, Min

# Create your views here.

def compose_message(request, username, form_class=ComposeMessageForm):
	"""
	Funkcija koja preuzima podatke sa forme kod slanja poruke korisniku preko liste svih korisnika.
	"""
	if request.method == 'POST':
		user_recipient = User.objects.get(username=username)
		message_form = form_class(data=request.POST)
		message_form.initial['recipient'] = user_recipient.profile.name

		if message_form.is_valid():

			# ispitati da li u Thread ima isti par korisnika, ako nema napraviti novi par a ako ima 
			# pokupiti ID tog Thread-a.
			s = request.user 		# logovani korisnik koji salje poruku
			r = user_recipient 		# korisnik kome se salje poruka

			check_pair = Thread.objects.filter(Q(participant_a=s, participant_b=r) | Q(participant_a=r, participant_b=s))

			# check_pair je [] ako nista nije pronadjeno
			if not check_pair:
				""" 
				Nije pronadjen trazeni par ID-ova u Thread tabeli, kreiramo novi red u tabeli Thread 
				i povezujemo novu poruku sa datim Thread-om 
				"""
				p_a = User.objects.get(id=min(s.id, r.id))
				p_b = User.objects.get(id=max(s.id, r.id))

				thread = Thread.objects.create(created_at=timezone.now(), participant_a=p_a, participant_b=p_b)

				message = message_form.save(commit=False)
				message.sender = s
				message.recipient = r
				message.sent_at = thread.created_at
				message.thread = thread
				message.save()

			else:
				""" 
				Pronadjen je trazeni par ID-ova u Thread tabeli. Povezujemo ga sa novom porukom. 
				"""
				message = message_form.save(commit=False)
				message.sender = s
				message.recipient = r
				message.sent_at = timezone.now()
				message.thread = check_pair[0]
				message.save()

			return render(request, 'message_success_sent.html', {'to_user': message.recipient})

		else:
			print(message_form.errors)		
	else:
		""" Kada se pozove GET metoda """
		name = User.objects.get(username=username).profile.name
		message_form = form_class()
		message_form.initial['recipient'] = name
	
	return render(request, 'compose_message.html', {'message_form': message_form, 'username': username})


"""
def compose_message(request, username, form_class=ComposeMessageForm):
	
	#Funkcija koja preuzima podatke sa forme kod slanja poruke korisniku preko liste svih korisnika.
	
	if request.method == 'POST':
		#name = User.objects.get(username=username).profile.name
		user_recipient = User.objects.get(username=username)
		message_form = form_class(data=request.POST)
		message_form.initial['recipient'] = user_recipient.profile.name

		if message_form.is_valid():

			# ispitati da li u bazi postoji isti par (sender, recipient), (recipient, sender) pa ako ima
			# prethodnu takvu poruku postaviti za PARENT

			s = request.user
			r = user_recipient

			# poslednja poruka sa trazenim parom (sender, recipient)
			qs = Message.objects.filter(Q(sender=s, recipient=r) | Q(sender=r, recipient=s))

			
			# qs je [] ako nista nije pronadjeno

			message = message_form.save(commit=False)
			message.sender = request.user
			message.recipient = User.objects.get(username=username)
			message.sent_at = timezone.now()
			if qs:
				message.parent_msg = qs[0]
				#for i in qs:
					#print("+++++++++++++++++++++++++++++++++++++++++++++++++++\n%s" % i)
					#print("+++++++++++++++++++++++++++++++++++++++++++++++++++\n")
			message.save()

			return render(request, 'message_success_sent.html', {'to_user': message.recipient})
		else:
			print(message_form.errors)
		
	else:
		name = User.objects.get(username=username).profile.name
		message_form = form_class()
		message_form.initial['recipient'] = name
	
	return render(request, 'compose_message.html', {'message_form': message_form, 'username': username})

def user_messages(request):
	
	#SELECT m1.id, m1.sender, m1.recipient, MIN(m1.sender, m1.recipient), MAX(m1.sender, m1.recipient), m1.sent_at FROM (SELECT * FROM Message m1 WHERE m1.sender=3 OR m1.recipient=3 GROUP BY m1.sender, m1.recipient ORDER BY m1.sent_at) m1 GROUP BY MIN(sender, recipient), MAX(sender, recipient) ORDER BY sent_at;
	#SELECT * FROM (SELECT id, text, sender, recipient, MIN(sender, recipient) AS x, MAX(sender, recipient) as y, sent_at, COUNT(id)
	#FROM Message
	#GROUP BY x, y) WHERE sender=3 OR recipient=3
	
	# m = Message.objects.extra(where=["private_messages_message.sender_id='3' OR private_messages_message.recipient_id='3'"]).values('sender','recipient').annotate(asd=Count('sender'))

	#messages = Message.objects.filter(Q(sender=request.user) | Q(recipient=request.user))
	threads = Message.objects.get_threads(request.user)
	return render(request, 'messages.html', {'threads': threads})

def thread_messages(request, thread_id):

	msg = Message.objects.get(pk=thread_id)
	print("EEEEEEEEEEEEEEEEEEeee %s" % request.user.sent_messages.all())

	thread_messages = Message.objects.thread_messages(msg, messages=[])

	return render(request, 'message.html', {'thread_messages': thread_messages})

def thread_delete(request, thread_id):

	msg = Message.objects.get(pk=thread_id)
	thread_messages = Message.objects.thread_messages(msg, messages=[])

	if thread_messages[0].sender.id == request.user.id:
		for m in thread_messages:
			m.sender_deleted_at = timezone.now()
			m.save()
	else:
		for m in thread_messages:
			m.recipient_deleted_at = timezone.now()
			m.save()
	return None
"""

def user_threads(request):
	"""
	Funkcije preuzima sve niti iz baze podataka za logovanog korisnika i prikazuje ih u templejtu.
	"""
	threads = Msg.objects.get_user_threads(request.user)
	return render(request, 'messages.html', {'threads': threads})

def thread_messages(request, thread_id):
	"""
	Funkcija preuzima sve poruke za zadatu nit i prikazuje ih u templejtu.
	"""
	thread_messages = Msg.objects.get_thread_messages(request.user, thread_id)
	return render(request, 'message.html', {'thread_messages': thread_messages})

def delete_thread(request, thread_id, last_msg_id):
	"""
	Funkcija brise sve poruke iz odabrane niti.
	"""
	thread = Thread.objects.get(id=thread_id)
	last_message = Msg.objects.get(id=last_msg_id)
	DeletedMessages.objects.get_or_create(deleted_by=request.user, deleted_at=timezone.now(), 
		id_of_last_del_msg=last_message, thread=thread)

	return redirect('user_threads')