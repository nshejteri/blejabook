# Pokretanje sa komandom: python populate_db.py

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blejabook.settings')

import django
django.setup()

from userprofile.models import UserProfile
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth.hashers import make_password

def populate():

	user1 = add_user('user1', 'user1@gmail.com', 'user1')
	user2 = add_user('user2', 'user2@gmail.com', 'user2')
	user3 = add_user('user3', 'user3@gmail.com', 'user3')
	user4 = add_user('user4', 'user4@gmail.com', 'user4')
	user5 = add_user('user5', 'user5@gmail.com', 'user5')

	add_profile(user1, 'User 1', datetime(1991, 01, 01, 0, 0), 'm', 'Srbija', 'Backi Breg', True, '1233456789123')
	add_profile(user2, 'User 2', datetime(1992, 02, 02, 0, 0), 'm', 'Srbija', 'Kolut', True, '1233456789123')
	add_profile(user3, 'User 3', datetime(1993, 03, 03, 0, 0), 'm', 'Srbija', 'Bezdan', True, '1233456789123')
	add_profile(user4, 'User 4', datetime(1994, 04, 04, 0, 0), 'm', 'Srbija', 'Sombor', True, '1233456789123')
	add_profile(user5, 'User 5', datetime(1995, 05, 05, 0, 0), 'm', 'Srbija', 'Novi Sad', True, '1233456789123')

def add_user(username, email, password):
	user = User.objects.get_or_create(username=username, email=email, password=make_password(password))[0]
	return user

def add_profile(user, name, date_of_birth, gender, country, city, verified, confirmation_key):
	profile = UserProfile.objects.get_or_create(user=user, name=name, date_of_birth=date_of_birth, gender=gender, country=country, city=city, verified=verified, confirmation_key=confirmation_key)[0]
	return profile

if __name__ == '__main__':
	print "Starting population script..."
	populate()