from django.shortcuts import render
from userauth.forms import MyUserForm, UserProfileForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def signup(request):
	if request.method == 'POST':
		pass

	else:
		user_form = MyUserForm()
		user_profile_form = UserProfileForm()

	return render(request, 'account/signup.html', {'user_form': user_form, 'user_profile_form': user_profile_form })