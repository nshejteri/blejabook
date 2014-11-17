from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from userprofile.models import UserProfile
from django.contrib.auth.decorators import login_required
from userauth.forms import UserProfileForm



def profile_permission(func):		
	def wraper(request, username):
		if request.user == User.objects.get(username=username):
			return func(request, username, permission=True)
		else:
			return func(request, username, permission=False)
	return wraper

	
def get_user_profile(username):

	user = User.objects.get(username=username)
	return  user.profile

def get_model_fields(model):
    return model._meta.fields

@profile_permission
def user_profile(request, username, permission=False):

	user_profile = get_user_profile(username)
	context = { 'permision': permission, 'user_profile': user_profile }
	return render(request, 'userprofile/user_profile.html', context)


@profile_permission
def edit_profile(request, username, permission=False):
	
	if permission == False:
		return HttpResponse('kurcina')
	else:
		user_profile = get_user_profile(username)
		if request.method=='POST':
			form = UserProfileForm(request.POST, instance = user_profile)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('.')
		else:
			form = UserProfileForm(instance = user_profile)

	return render(request, 'userprofile/edit_profile.html', { 'form': form} )
