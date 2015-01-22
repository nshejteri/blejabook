from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from userprofile.models import UserProfile
from django.contrib.auth.decorators import login_required
from userauth.forms import UserProfileForm
from PIL import Image
from os.path import join
from django.conf import settings

def profile_permission(func):
	"""
	Anotacija koja omogucava prikaz dodatnih opcija na profilu logovanog korisnika (sopstvenom)
	dok na ostalim profilima korisnika onemogucuje prikaz dodatnih opcija.
	"""
	def wrapper(request, username):
		if request.user == User.objects.get(username=username):

			return func(request, username, permission=True)
		else:

			return func(request, username, permission=False)
	return wrapper

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
		url_redirection = '/accounts/profile/' + username + '/'
		if request.method == 'POST':
			form = UserProfileForm(request.POST, request.FILES, instance=profile)
			
			if form.is_valid():
				form.save()
				
				img_path = join(settings.MEDIA_ROOT, str(get_profile(username).profile_image))
				print("PATH %s " % img_path)
			
				img = Image.open(img_path)
				print("SIZE %s " % str(img.size))

				img.thumbnail((160, 160))
				img.save(img_path, 'JPEG')

				return HttpResponseRedirect(url_redirection)
			else:
				return HttpResponse('VALIDACIJA PROBLEM')
		else:
			form = UserProfileForm(instance=profile)

	return render(request, 'userprofile/edit_profile.html', {'form': form})

@login_required
def all_users(request):
	"""
	Funkcija ...
	"""
	users = User.objects.exclude(id=request.user.id)
	return render(request, 'userprofile/all_users.html', {'users': users})
