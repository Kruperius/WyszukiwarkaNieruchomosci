from django import forms
from .models import Nieruchomosci

class NieruchomoscFormularz(forms.ModelForm):
	class Meta:
		model = Nieruchomosci
		fields = ['lokalizacja', 'transakcja', 'rodzaj', 'rodzaj_zabudowy', 'typ_domu', 'komercyjne', 'typ_dzialki', 'cena_od', 'cena_do']