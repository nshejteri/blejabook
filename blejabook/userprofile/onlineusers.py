from django.core.cache import cache
from django.conf import settings
from django.contrib.auth.models import User

ONLINE_TIMEOUT = getattr(settings, 'ONLINE_TIMEOUT', 60 * 1)

def get_online_now(self):
	"""
	Funkcija koja vraca listu online korisnika (korisnika koji su imali aktivnost u prethodnih 15min)
	"""
	return User.objects.filter(id__in=self.online_now_ids or [])

class OnlineNowUsersMiddleware(object):
	"""
	Middleware klasa za memorisanje i postavljanje na request objekat liste online korisnika.
	"""

	def process_request(self, request):
		"""
		"""
		uids = cache.get('online_now', [])

		online_keys = ['online-%s' % (u,) for u in uids]
		fresh = cache.get_many(online_keys).keys()
		online_now_ids = [int(k.replace('online-', '')) for k in fresh]

		if request.user.is_authenticated():
			uid = request.user.id

			if uid in online_now_ids:
				online_now_ids.remove(uid)
			online_now_ids.append(uid)

		# Postavka na request objekat lista id-a online korisnika i liste objekata online korisnika
		request.__class__.online_now_ids = online_now_ids
		request.__class__.online_now = property(get_online_now)

		# Postavka aktivnih korisnika (unutar 15min) u kes memoriju u formatu 'online-PK': True
		# i liste id-a svih online korisnika u formatu 'online_now': [id1, id2,..]
		cache.set('online-%s' % (request.user.pk,), True, ONLINE_TIMEOUT)
		cache.set('online_now', online_now_ids)

