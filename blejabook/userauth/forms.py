from django import forms
from django.contrib.auth.models import User
from userprofile.models import UserProfile
from django.forms import CharField, BooleanField, Form, ChoiceField, DateField
import datetime
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _

GENDER_CHOICES = ( 
		('m', 'Male'),
		('f', 'Female'),
	)

class MyUserForm(UserCreationForm):
	def __init__(self, *args, **kw):
		super(UserCreationForm, self).__init__(*args, **kw)
		self.fields['username'].widget.attrs['placeholder'] = 'Username'
		self.fields['username'].widget.attrs['autofocus'] = 'autofocus'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields.pop('password2')

	email = forms.EmailField(label=_('Email'), required=True, widget=forms.TextInput(attrs={'placeholder': 'Email', 'autofocus': 'autofocus'}))
	email2 = forms.EmailField(label=_('Email confirmation'), required=True, widget=forms.TextInput(attrs={'placeholder': 'Email Confirmation', 'autofocus': 'autofocus'}))

	error_messages = {
		'duplicate_username': _("A user with that username already exists."),
		'password_mismatch': _("The two password fields didn't match."),
		'email_mismatch': _("The two email fields didn't match."),
	}

	class Meta:
		model = User
		fields = ('username', 'email', 'email2')

	def clean_email2(self):
		email = self.cleaned_data['email']
		email2 = self.cleaned_data['email2']

		if email and email2 and email != email2:
			raise forms.ValidationError(
				self.error_messages['email_mismatch'],
				code='email_mismatch',
			)		
		email = email2
		return email

class UserProfileForm(forms.ModelForm):

	#gender = ChoiceField(GENDER_CHOICES, label='Gender', required=True)
	gender = forms.CharField(widget=forms.RadioSelect(choices=GENDER_CHOICES))
	date_of_birth = forms.DateField(required=True, widget=SelectDateWidget(years=range(1950, datetime.date.today().year)))
	country = forms.CharField(max_length=30, label='Country', widget=forms.TextInput(attrs={'placeholder': 'Country', 'autofocus': 'autofocus'}))
	city = forms.CharField(max_length=30, label='City', widget=forms.TextInput(attrs={'placeholder': 'City', 'autofocus': 'autofocus'}))
	
	class Meta:
		model = UserProfile
		fields = ('gender', 'date_of_birth', 'country', 'city')

   

   
    