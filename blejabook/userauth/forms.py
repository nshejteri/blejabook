from django import forms
from django.contrib.auth.models import User
from userprofile.models import UserProfile
from django.forms import CharField, BooleanField, Form, ChoiceField, DateField
import datetime
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _

class MyUserForm(UserCreationForm):
	def __init__(self, *args, **kw):
		super(UserCreationForm, self).__init__(*args, **kw)
		self.fields['username'].widget.attrs['placeholder']='Username'
		self.fields['username'].widget.attrs['autofocus']='autofocus'
		self.fields['password1'].widget.attrs['placeholder']='Password'
		self.fields['password2'].widget.attrs['placeholder']='Password confirmation'

	email = forms.EmailField(label=_('Email'), required=True, widget=forms.TextInput(attrs={'placeholder': 'Email', 'autofocus': 'autofocus'}))

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

	def clean_email(self):
 		email = self.cleaned_data['email']
 		return email

class UserProfileForm(forms.ModelForm):

	GENDER_CHOICES = ( 
     	('m', 'Male'), 
     	('f', 'Female'),
    )

	gender = ChoiceField(GENDER_CHOICES, label='Gender', required=True)
	date_of_birth = forms.DateField(required=True, widget=SelectDateWidget(years=range(1950, datetime.date.today().year)))
	country = forms.CharField(max_length=30, label='Country', widget=forms.TextInput(attrs={'placeholder': 'Country', 'autofocus': 'autofocus'}))
	city = forms.CharField(max_length=30, label='City', widget=forms.TextInput(attrs={'placeholder': 'City', 'autofocus': 'autofocus'}))

	class Meta:
		model = UserProfile
		fields = ('gender', 'date_of_birth', 'country', 'city')

	
   

   
    