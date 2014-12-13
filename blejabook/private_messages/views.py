from django.shortcuts import render
from private_messages.forms import ComposeMessageForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.views.generic import UpdateView, ListView 
from django.http import HttpResponse
from private_messages.models import Message
from django.utils import timezone

# Create your views here.


def compose_message(request, username, form_class=ComposeMessageForm):
	"""
	Funkcija koja preuzima podatke sa forme kod slanja poruke korisniku preko liste svih korisnika.
	"""
	if request.method == 'POST':
		name = User.objects.get(username=username).profile.name
		message_form = form_class(data=request.POST)
		message_form.initial['recipient'] = name

		if message_form.is_valid():

			message = message_form.save(commit=False)
			message.sender = request.user
			message.recipient = User.objects.get(username=username)
			message.sent_at = timezone.now()
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
	pass