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

def get_profile(username):
	user = User.objects.get(username=username)
	return  user.profile

def get_profil_owner(username):
	return User.objects.get(username=username)

@profile_permission
def user_profile(request, username, permission=False):
	"""
	Funkcija za prikaz korisnickog profila.
	"""
	profil_owner = get_profil_owner(username)
	profile = get_profile(username)
	context = {'permission': permission, 'profile': profile, 'profil_owner': profil_owner}

	return render(request, 'userprofile/profile.html', context)

@profile_permission
def edit_profile(request, username, permission=False):
	"""
	Funkcija za izmenu profilnih podataka.
	"""
	if permission == False:
		return HttpResponse('kurcina')
	else:
		profile = get_profile(username)

		if request.method == 'POST':
			form = UserProfileForm(request.POST, instance=profile)
			
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('.')
		else:
			form = UserProfileForm(instance=profile)

	return render(request, 'userprofile/edit_profile.html', {'form': form})

def all_users(request):
	"""
	Funkcija ...
	"""
	users = User.objects.exclude(id=request.user.id)
	return render(request, 'userprofile/all_users.html', {'users': users})