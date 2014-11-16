from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect


def index(request):

	if request.user.is_authenticated():
		return render(request,'main_app/index.html',{})
	else:
		return HttpResponseRedirect("/account/login/")







