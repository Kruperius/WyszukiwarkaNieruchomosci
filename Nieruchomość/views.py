from django.shortcuts import render
from .formularze import NieruchomoscFormularz
from .klasy_stron_1 import Morizon, Gratka, Gumtree
from django.core.paginator import Paginator
from multiprocessing import Process
import concurrent.futures

# Create your views here.

def result(request, *args, **kwargs):
	
	if request.method == 'POST':	

		lokalizacja = request.POST.get('lokalizacja')
		transakcja = request.POST.get('transakcja')
		rodzaj = request.POST.get('rodzaj')
		rodzaj_zabudowy = request.POST.get('rodzaj_zabudowy')
		typ_domu = request.POST.get('typ_domu')
		komercyjne = request.POST.get('komercyjne')
		typ_dzialki = request.POST.get('typ_dzialki')
		cena_od = request.POST.get('cena_od')
		cena_do = request.POST.get('cena_do')

		# Morizon(lokalizacja, transakcja, rodzaj, rodzaj_zabudowy, typ_domu, komercyjne, typ_dzialki,
		# 	cena_od, cena_do)

		# Gratka(lokalizacja, transakcja, rodzaj, rodzaj_zabudowy, typ_domu, komercyjne, typ_dzialki,
		# cena_od, cena_do)

		# Gumtree(lokalizacja, transakcja, rodzaj, rodzaj_zabudowy, typ_domu, komercyjne, typ_dzialki,
		# cena_od, cena_do)

		dane = []

		M = [concurrent.futures.ProcessPoolExecutor().submit(Morizon, lokalizacja, transakcja, rodzaj, rodzaj_zabudowy, typ_domu, komercyjne, typ_dzialki,
			cena_od, cena_do), concurrent.futures.ProcessPoolExecutor().submit(Gratka, lokalizacja, transakcja, rodzaj, rodzaj_zabudowy, typ_domu, komercyjne, typ_dzialki,
			cena_od, cena_do), concurrent.futures.ProcessPoolExecutor().submit(Gumtree, lokalizacja, transakcja, rodzaj, rodzaj_zabudowy, typ_domu, komercyjne, typ_dzialki,
			cena_od, cena_do)]
		# M_return = M.result()

		for i in M:
			dane.extend(i.result())

		# G = concurrent.futures.ThreadPoolExecutor().submit(Gratka, lokalizacja, transakcja, rodzaj, rodzaj_zabudowy, typ_domu, komercyjne, typ_dzialki,
		# 	cena_od, cena_do)
		# G_return = G.result()

		# Gum = concurrent.futures.ThreadPoolExecutor().submit(Gumtree, lokalizacja, transakcja, rodzaj, rodzaj_zabudowy, typ_domu, komercyjne, typ_dzialki,
		# 	cena_od, cena_do)
		# Gum_return = Gum.result()

		# dane = M_return + G_return + Gum_return
		# gratka = G_return
		# gumtree = Gum_return
		# dane.extend(gratka + gumtree)

		request.session['dane'] = dane
		paginator = Paginator(dane, 20)

		numer_str = request.GET.get('page')
		obj_str = paginator.get_page(numer_str)

		return render(request, 'result.html', {'dane': obj_str})

	else:

		dane = request.session.get('dane')
		paginator = Paginator(dane, 20)

		numer_str = request.GET.get('page')
		obj_str = paginator.get_page(numer_str)

	return render(request, 'result.html', {'dane': obj_str})

def wyszukaj(request, *args, **kwargs):
	formularz = NieruchomoscFormularz(request.POST or None)
	kontekst = {'formularz': formularz, 
	'rodzaj_zabudowy': formularz['rodzaj_zabudowy'].value(),
	'typ_domu': formularz['typ_domu'].value(),
	'komercyjne': formularz['komercyjne'].value(),
	'typ_dzialki': formularz['typ_dzialki'].value()}

	return render(request, 'formularz1.html', kontekst)


	