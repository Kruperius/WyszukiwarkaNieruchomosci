from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
class Zrodla(models.Model):
	#witryna = [('m', 'morizon.pl'), ('g', 'gratka.pl'), ]

	#nazwa = MultiSelectField(choices=witryna, max_length=100)
	nazwa = models.CharField(max_length = 100)
	

	def __str__(self):
		return self.nazwa

class Nieruchomosci(models.Model):
	s_w = [('S', 'Sprzedarz'), ('W', 'Wynajem')]
	rodz = [('D', 'Dowolny'), ('M', 'Mieszkania'), ('Domy', 'Domy'), ('K', 'Komercyjne'), ('Dz', 'Działki'), ('G', 'Garaże'), ('P', 'Pokoje')]
	rodz_z = [('d', 'Dowolny'), ('A', 'Apartamentowiec'), ('B', 'Blok'), ('D', 'Dom'), ('K', 'Kamienica')]
	typ_d = [('D', 'Dowolny'), ('W', 'Wolnostojacy'), ('B', 'Blizniak'), ('P', 'Pałac/Dworek'), ('A', 'Atrialny'), ('L', 'Letniskowy'), ('Sz', 'Szeregowiec'), ('K', 'Kamienica'), ('Blok', 'Blok'), ('G', 'Gospodarstwo')]
	typ_k = [('D', 'Dowolny'), ('B', 'Biura'), ('H', 'Hale i Magazyny')]
	typ_dz = [('D', 'Dowolny'), ('R', 'Rolna'), ('B', 'Budowlana'), ('L', 'Leśna'), ('Re', 'Rekreacyjna'), ('S', 'Siedliskowa'), ('P', 'Przemysłowa'), ('I', 'Inwestycyjna')]
	witryna = [('m', 'morizon.pl'), ('g', 'gratka.pl'), ('gum', 'gumtree.pl'), ('o', 'otodom.pl'), ('d', 'domiporta.pl'), ('o', 'olx.pl'), ('sz', 'szybko.pl')]

	lokalizacja = models.CharField(max_length = 255, blank=True)
	transakcja = models.CharField(choices=s_w, max_length=100, default='S')
	rodzaj = models.CharField(choices=rodz, max_length=100, default='D')
	rodzaj_zabudowy = models.CharField(choices=rodz_z, max_length=100, default='d')
	typ_domu = models.CharField(choices=typ_d, max_length=100, default='D')
	komercyjne = models.CharField(choices=typ_k, max_length=100, default='D')
	typ_dzialki = models.CharField(choices=typ_dz, max_length=100, default='D')
	opis = models.TextField(blank=True)
	cena_od = models.DecimalField(max_digits=9, decimal_places=2, blank=True)
	cena_do = models.DecimalField(max_digits=9, decimal_places=2, blank=True)
	data_dodania = models.DateTimeField(blank=True)
	#zrodlo = models.ForeignKey(Zrodla, on_delete=models.CASCADE)
	zrodla = MultiSelectField(choices=witryna, max_length=100)


	#def __str__(self):
		#return self.nazwa
		