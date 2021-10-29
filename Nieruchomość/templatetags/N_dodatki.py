from django import template
from django import forms

register = template.Library()

opis = forms.CharField()

def dodaj_pole(value):
	return value.update({'opis': opis})

register.filter('dodaj_pole', dodaj_pole)
