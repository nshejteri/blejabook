from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from userprofile.models import UserProfile

def index(request):
	print("PROVERA 2")
	if request.user.is_authenticated():
		return render(request, 'main_app/home.html', {})
	else:
		#return HttpResponseRedirect("/account/login/")
		return render(request, 'index.html', {})





