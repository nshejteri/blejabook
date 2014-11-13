from django.shortcuts import render
from userauth.forms import MyUserForm, UserProfileForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth

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

	return render(request, '/account/signup.html', {'user_form':user_form, 'user_profile_form': user_profile_form})

def user_login(request):
	if request.method=='POST':
		username = request.POST['username']
		password = request.POST['password']

		user=auth.authenticate(username=username, password=password)
		if user:
			if user.is_active:
				auth.login(request, user)
				return HttpResponseRedirect('/admin/')
			else:
				return HttpResponse('jok')
		else:
			print 'invalid login details: {0}, {1}'.format(username, password)
			return HttpResponse('invalid login details supplied')
	else:
		return render(request,'account/login.html/',{})





    



	