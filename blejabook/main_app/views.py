from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from userprofile.models import UserProfile

PERMISION = False

def permision(func):		
	def wraper(request, username):
		if request.user == User.objects.get(username=username):
			global PERMISION 
			PERMISION = True
		return func(request, username)
	return wraper
	
def get_user(username):

	user = User.objects.get(username=username)
	user_profile = UserProfile.objects.get(user=user)
	return user_profile


def index(request):

	if request.user.is_authenticated():
		return render(request,'main_app/index.html',{})
	else:
		return HttpResponseRedirect("/account/login/")


@permision
def user_profile(request, username):

	global PERMISION
	user_profile = get_user(username)
	context = {'permision': PERMISION}
	PERMISION = False
	return render(request, 'main_app/user_profile.html',context)





