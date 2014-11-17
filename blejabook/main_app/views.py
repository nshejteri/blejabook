from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from userprofile.models import UserProfile


def permision(func):		
	def wraper(request, username, permission=False):
		if request.user == User.objects.get(username=username):
			return func(request, username, permission=True)
		else:
			return func(request, username, permission=False)

	return wraper
	
def get_user(username):

	user = User.objects.get(username=username)
	user_profile = UserProfile.objects.get(user=user)
	return user_profile

def index(request):

	if request.user.is_authenticated():
		return render(request,'main_app/index.html', {})
	else:
		return HttpResponseRedirect("/account/login/")

@permision
def user_profile(request, username, permission=False):

	user_profile = get_user(username)
	context = { 'permision': permission, 'user_profile': user_profile }
	return render(request, 'main_app/user_profile.html', context)





