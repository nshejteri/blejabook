from django.shortcuts import render
from userauth.forms import MyUserForm, UserProfileForm


# Create your views here.

def signup(request):
	
	if request.method=='POST':
		user_form=MyUserForm(data=request.POST)
		user_profile_form=UserProfileForm(data=request.POST)

		if user_form.is_valid() and user_profile_form.is_valid():
			user = user_form.save()
			profile=user_profile_form.save(commit=False)
			profile.user=user
			profile.save()
		else:
			print user_form.errors, user_profile_form.errors

	else:
		user_form = MyUserForm()
		user_profile_form = UserProfileForm()

	return render(request, 'account/signup.html', {'user_form':user_form, 'user_profile_form': user_profile_form})



	