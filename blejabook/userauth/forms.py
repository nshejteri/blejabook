from django import forms
from django.contrib.auth.models import User
from userprofile.models import UserProfile
from django.forms import CharField, BooleanField, Form, ChoiceField, DateField
import datetime
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _

class MyUserForm(forms.ModelForm):
	"""
    A form that creates a user, with no privileges, from the given username and
    password.
    """
	
	error_messages = {
        'duplicate_username': _("A user with that username already exists."),
        'password_mismatch': _("The two password fields didn't match."),
    }

	username = forms.RegexField(label=_('Username'), regex=r'^\w+$', max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Username', 'autofocus': 'autofocus'}), error_messages={ 'invalid': _('This value must contain only letters, numbers and underscores.') })	
	email = forms.EmailField(label=_('Email'), required=True, widget=forms.TextInput(attrs={'placeholder': 'Email', 'autofocus': 'autofocus'}))
	password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
	password2 = forms.CharField(label=_('Password confirmation'), widget=forms.PasswordInput(attrs={'placeholder': 'Password confirmation'}), help_text=_('Enter the same password as above, for verification.'))

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

	def clean_username(self):
		# Since User.username is unique, this check is redundant,
		# but it sets a nicer error message than the ORM. See #13147.
		username = self.cleaned_data["username"]
		try:
			User._default_manager.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError(
			self.error_messages['duplicate_username'],
			code='duplicate_username'
		)

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError(
				self.error_messages['password_mismatch'],
				code='password_mismatch',
			)
		return password2

	def clean_email(self):
 		email = self.cleaned_data['email']
 		return email

 	def save(self, commit=True):
 		user = super(MyUserForm, self).save(commit=False)
 		user.set_password(self.cleaned_data["password1"])
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

	
   

   
    