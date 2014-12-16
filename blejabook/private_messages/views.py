from django.shortcuts import render
from private_messages.forms import ComposeMessageForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.views.generic import UpdateView, ListView 
from django.http import HttpResponse
from private_messages.models import Message
from django.utils import timezone
from django.db.models import Q

# Create your views here.


def compose_message(request, username, form_class=ComposeMessageForm):
	"""
	Funkcija koja preuzima podatke sa forme kod slanja poruke korisniku preko liste svih korisnika.
	"""
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

def thread_messages(request):
	"""
	"""
	msg = Message.objects.get(pk=63)
	thread = Message.objects.message_thread_for(request.user, msg)

	return render(request, 'messages.html', {'thread': thread})

def user_messages(request):
	"""
	"""

	messages = Message.objects.filter(Q(sender=request.user) | Q(recipient=request.user))
	return render(request, 'messages.html', {'messages': messages})

