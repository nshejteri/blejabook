from django import forms
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from private_messages.models import Msg

class ComposeMessageForm(forms.ModelForm):
	"""
	Forma za slanje privatne poruke korisniku izabranom u listi svih korisnika.
	"""
	recipient = forms.CharField(label=_(u"To"), max_length=60, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
	message_text = forms.CharField(label=_(u"Message text"), widget=forms.Textarea(attrs={'rows': '6', 'cols': '40', 'class': 'form-control', 'autofocus': 'autofocus', 'placeholder': 'Message text...'}))

	class Meta:
		model = Msg
		fields = ('message_text',)


