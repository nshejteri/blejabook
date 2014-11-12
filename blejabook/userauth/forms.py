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
		self.fields.keyOrder = [
			'username',
			'email',
			'password1',
			'password2',
		]

	username = forms.RegexField(label=_('Username'), regex=r'^\w+$', max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Username', 'autofocus': 'autofocus'}), error_messages={ 'invalid': _('This value must contain only letters, numbers and underscores.') })	
	email = forms.EmailField(label=_('Email'), required=True, widget=forms.TextInput(attrs={'placeholder': 'Email', 'autofocus': 'autofocus'}))
	password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
	password2 = forms.CharField(label=_('Password confirmation'), widget=forms.PasswordInput(attrs={'placeholder': 'Password confirmation'}), help_text=_('Enter the same password as above, for verification.'))

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)
		user.username = self.cleaned_data['username']
		user.email = self.cleaned_data['email']
		user.password1 = self.cleaned_data['password1']
		user.password2 = self.cleaned_data['password2']

		if commit:
			user.save()
		return user

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

    


    