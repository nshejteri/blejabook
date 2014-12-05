from django import template
import datetime

register = template.Library()

@register.filter(name='age')
def age(bday, d=None):
	"""
	Filter koji racuna godine od datuma rodjenja i danasnjeg datuma.
	"""
	if d is None:
		d = datetime.date.today()
	return (d.year - bday.year) - int((d.month, d.day) < (bday.month, bday.day))

@register.filter(name='online')
def online(online, status='Offline'):
	"""
	Filter vraca vrednost 'Online' ili 'Offline' u zavisnosti od prosledjene vrednosti 'True' ili 'None'.
	"""
	if online is True:
		status = 'Online'
	else:
		status = 'Offline'

	return status