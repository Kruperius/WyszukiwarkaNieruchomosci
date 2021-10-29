from lxml import html
import requests
import re
import unicodedata
import math

# class Witryna:
# 	lokalizacja = request.POST.get('lokalizacja')
# 	transakcja = request.POST.get('transakcja')
# 	rodzaj = request.POST.get('rodzaj')
# 	rodzaj_zabudowy = request.POST.get('rodzaj_zabudowy')
# 	typ_domu = request.POST.get('typ_domu')
# 	komercyjne = request.POST.get('komercyjne')
# 	typ_dzialki = request.POST.get('typ_dzialki')
# 	cena_od = request.POST.get('cena_od')
# 	cena_do = request.POST.get('cena_do')

# class Morizon:
	
# 	def __init__(self, lokalizacja, transakcja, rodzaj, rodzaj_zabudowy, typ_domu, komercyjne, 
# 		typ_dzialki, cena_od, cena_do):

# 		self.lokalizacja = lokalizacja
# 		self.transakcja = transakcja
# 		self.rodzaj = rodzaj
# 		self.rodzaj_zabudowy = rodzaj_zabudowy
# 		self.typ_domu = typ_domu
# 		self.komercyjne = komercyjne
# 		self.typ_dzialki = typ_dzialki
# 		self.cena_od = cena_od
# 		self.cena_do = cena_do

# 	a = {'S': '', 'W': '/do-wynajecia'}
# 	t = a[self.transakcja]

# 	b = {'D': '/nieruchomosci/', 'M': '/mieszkania/', 'Domy': '/domy/', 'K': '/komercyjne/', 'Dz': '/dzialki/', 'G': '/garaze/', 'P': '/pokoje/'}
# 	if t == '':
# 		b['G'] = '/sprzedarz/garaze/'
# 	r = b[self.rodzaj]

# 	c = {'d': '', 'A': 'apartamentowiec/', 'B': 'blok/', 'D': 'dom-wielorodzinny/', 'K': 'w-kamienicy/'}
# 	r_z = c[self.rodzaj_zabudowy]

# 	d = {'D': '', 'W': 'wolnostojacy/', 'B': 'blizniak/', 'P': 'palac-dworek/', 'A': 'atrialny/', 'L': 'letniskowy/', 'Sz': 'szeregowiec/', 'K': 'kamienice/', 'B': 'blok/', 'G': 'gospodarstwo/'}
# 	r_d = d[self.typ_domu]

# 	e = {'D': '', 'B': 'biuro/', 'H': ''}
# 	k = e[self.komercyjne]

# 	f = {'D': '', 'R': 'rolna/', 'B': 'budowlana/', 'L': 'lesne/', 'Re': 'rekreacyjna/', 'S': 'siedliska/', 'P': 'przemyslowa/', 'I': 'handlowo-uslugowa/'}
# 	t_dz = f[self.typ_dzialki]

# 	# if rodzaj == 'D' or 'G' or 'P':
# 	# 	r_z, r_d, k, t_dz = '', '', '', ''
# 	# elif rodzaj == 'M':
# 	# 	r_d, k, t_dz = '', '', ''
# 	# elif rodzaj == 'Domy':
# 	# 	r_z, k, t_dz = '', '', ''
# 	# elif rodzaj == 'K':
# 	# 	r_z, r_d, t_dz = '', '', ''
# 	# elif rodzaj == 'Dz':
# 	# 	r_z, r_d, k = '', '', ''
		
# 	def zam(x):
# 		sub = {'Ł': 'L', 'ł': 'l', 'ẞ': 'SS', 'ß': 'ss'}
# 		return sub[x.group()]

# 	g = re.sub('Ł|ł|ẞ|ß', zam, self.lokalizacja)
# 	g = unicodedata.normalize('NFKD', g).encode('ascii', 'ignore').decode('ascii')
# 	g = re.sub('ul|al|ulica|aleje|pl|plac|skwer', '', g)
# 	g = re.sub('[\W_]+', '/', g)
# 	g +='/'
# 	lok = g.lower()

# 	print(t, r, r_z, r_d, k, t_dz, lok)
# 	print(rodzaj, rodzaj_zabudowy, typ_domu, komercyjne, typ_dzialki)

# 	h = cena_od

# 	i = cena_do

# 	url = 'https://www.morizon.pl{}{}{}{}{}{}{}'.format(t, r, r_z, r_d, k, t_dz, lok)
# 	wyszukaj = requests.get(url)
# 	pars = html.fromstring(wyszukaj.text)
# 	print(url)

# 	xpath = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[1]/div/div/div/section/div[1]/ul/li[2]/b/text()'
# 	powierzchnia = pars.xpath(xpath)

# 	if len(powierzchnia) == 1:
			
# 		powierzchnia = powierzchnia[0]

# 	else:
# 		powierzchnia = 'Brak'

def lok_url(lokalizacja):

	sub = {'Ł': 'L', 'ł': 'l', 'ẞ': 'SS', 'ß': 'ss'}

	a = re.sub('Ł|ł|ẞ|ß', lambda a: sub[a.group()], lokalizacja)
	b = unicodedata.normalize('NFKD', a).encode('ascii', 'ignore').decode('ascii')
	c = re.sub('ul|al|ulica|aleje|pl|plac|skwer', '', b)
	d = re.sub('[\W_]+', '/', c)
	if len(d) > 0:
		d +='/'
	lok_url.e = d.lower()

def cena_url(cena_od, cena_do):

	if cena_od == '':
		cena_url.c_od = ''
	else:
		cena_url.c_od =  '?ps%5Bprice_from%5D=' + cena_od

	if cena_do == '':
		cena_url.c_do = ''
	elif cena_od == '':
		cena_url.c_do = '?ps%5Bprice_to%5D=' + cena_do
	else:
		cena_url.c_do = '&ps%5Bprice_to%5D=' + cena_do

def wyszukaj_dane(t, r, r_z, r_d, k, t_dz, lok, c_od, c_do):

	wyszukaj_dane.dane = []

	url = 'https://www.morizon.pl{}{}{}{}{}{}{}{}{}'.format(t, r, r_z, r_d, k, t_dz, lok, c_od, c_do)
	Wyszukaj = requests.get(url)
	Pars = html.fromstring(Wyszukaj.text)

	xpath_brak_ogloszen = '//*[@id="contentPage"]/div[1]/div/div/div[2]/div/div/div[1]/text()'
	brak_ogloszen = Pars.xpath(xpath_brak_ogloszen)

	xpath_l_wyszukan = '//*[@id="contentPage"]/div[1]/div/div/div/header/div/p/text()'
	l_wyszukan = re.search('\d+', Pars.xpath(xpath_l_wyszukan)[0]).group()
	print(l_wyszukan)

	if not brak_ogloszen:

		pagin = math.ceil(int(l_wyszukan) / 35)
		pagin_reszta = int(l_wyszukan) % 35
		
		for i in range(1, pagin+1):

			url_p = url
			
			if url.endswith('/'):
				url_p += '?page={}'.format(i)
			else:
				url_p += '&page={}'.format(i)

			wyszukaj = requests.get(url_p)
			pars = html.fromstring(wyszukaj.text)

			if i < pagin: 

				for i in range(1, 36):

					xpath_tytul = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/header/a/div/div[1]/h2/text()'.format(i)
					xpath_podtytul = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/header/a/div/div[1]/p/text()'.format(i)
					xpath_podtytul_input = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/header/a/div/div[1]/p/span/text()'.format(i)
					xpath_podtytul_input_strong = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/header/a/div/div[1]/p/span/strong/text()'.format(i)
					xpath_cecha_1 = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/div[1]/ul/li[1]/b/text()'.format(i)
					xpath_cecha_1_2 = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/div[1]/ul/li[1]/text()'.format(i)
					xpath_cecha_2_05 = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/div[1]/ul/li[2]/text()'.format(i)
					xpath_cecha_2 = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/div[1]/ul/li[2]/b/text()'.format(i)
					xpath_cecha_2_2 = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/div[1]/ul/li[2]/text()'.format(i)
					xpath_cecha_3_05 = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/div[1]/ul/li[3]/text()'.format(i)
					xpath_cecha_3 = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/div[1]/ul/li[3]/b/text()'.format(i)
					xpath_cecha_3_2 = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/div[1]/ul/li[3]/text()'.format(i)
					xpath_opis = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/div[2]/p/text()'.format(i)
					xpath_cena = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/header/a/div/div[2]/p[1]/text()'.format(i)
					xpath_cena_za_m2 = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/header/a/div/div[2]/p[2]/text()'.format(i)
					xpath_img = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/div[1]/div/div/img/@src'.format(i)
					xpath_oferta_url = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/header/a/@href'.format(i)

					tytul = pars.xpath(xpath_tytul)
					podtytul = pars.xpath(xpath_podtytul)
					podtytul_input = pars.xpath(xpath_podtytul_input)
					podtytul_input_strong = pars.xpath(xpath_podtytul_input_strong)
					cecha_1 = pars.xpath(xpath_cecha_1)
					cecha_1_2 = pars.xpath(xpath_cecha_1_2)
					# cecha_2_05 = pars.xpath(xpath_cecha_2_05)
					cecha_2 = pars.xpath(xpath_cecha_2)
					cecha_2_2 = pars.xpath(xpath_cecha_2_2)
					# cecha_3_05 = pars.xpath(xpath_cecha_3_05)
					cecha_3 = pars.xpath(xpath_cecha_3)
					cecha_3_2 = pars.xpath(xpath_cecha_3_2)
					opis = pars.xpath(xpath_opis)
					cena = pars.xpath(xpath_cena)
					cena_za_m2 = pars.xpath(xpath_cena_za_m2)
					img = pars.xpath(xpath_img)
					oferta_url = pars.xpath(xpath_oferta_url)

					if podtytul:
						podtytul[0] = re.sub('\n', '', podtytul[0])

					x = 1
					for i in podtytul_input:
						podtytul.insert(x, i)
						x += 1
					
					y = 1
					for i in podtytul_input_strong:
						podtytul.insert(y, i)
						y += 1

					wyszukaj_dane.dane.append([' '.join(tytul), ' '.join(podtytul), *cecha_1, ' '.join(cecha_1_2), *cecha_2, ' '.join(cecha_2_2), *cecha_3, ' '.join(cecha_3_2), *opis, *cena, *cena_za_m2, *img, *oferta_url])

			elif i == pagin and pagin_reszta != 0:
				
				for i in range(1, pagin_reszta + 1):

					xpath_tytul = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/header/a/div/div[1]/h2/text()'.format(i)
					xpath_podtytul = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/header/a/div/div[1]/p/text()'.format(i)
					xpath_podtytul_input = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/header/a/div/div[1]/p/span/text()'.format(i)
					xpath_podtytul_input_strong = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/header/a/div/div[1]/p/span/strong/text()'.format(i)
					xpath_cecha_1 = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/div[1]/ul/li[1]/b/text()'.format(i)
					xpath_cecha_1_2 = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/div[1]/ul/li[1]/text()'.format(i)
					xpath_cecha_2_05 = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/div[1]/ul/li[2]/text()'.format(i)
					xpath_cecha_2 = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/div[1]/ul/li[2]/b/text()'.format(i)
					xpath_cecha_2_2 = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/div[1]/ul/li[2]/text()'.format(i)
					xpath_cecha_3_05 = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/div[1]/ul/li[3]/text()'.format(i)
					xpath_cecha_3 = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/div[1]/ul/li[3]/b/text()'.format(i)
					xpath_cecha_3_2 = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/div[1]/ul/li[3]/text()'.format(i)
					xpath_opis = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/div[2]/p/text()'.format(i)
					xpath_cena = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/header/a/div/div[2]/p[1]/text()'.format(i)
					xpath_cena_za_m2 = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/header/a/div/div[2]/p[2]/text()'.format(i)
					xpath_img = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/div[1]/div/div/img/@src'.format(i)
					xpath_oferta_url = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/header/a/@href'.format(i)

					tytul = pars.xpath(xpath_tytul)
					podtytul = pars.xpath(xpath_podtytul)
					podtytul_input = pars.xpath(xpath_podtytul_input)
					podtytul_input_strong = pars.xpath(xpath_podtytul_input_strong)
					cecha_1 = pars.xpath(xpath_cecha_1)
					cecha_1_2 = pars.xpath(xpath_cecha_1_2)
					# cecha_2_05 = pars.xpath(xpath_cecha_2_05)
					cecha_2 = pars.xpath(xpath_cecha_2)
					cecha_2_2 = pars.xpath(xpath_cecha_2_2)
					# cecha_3_05 = pars.xpath(xpath_cecha_3_05)
					cecha_3 = pars.xpath(xpath_cecha_3)
					cecha_3_2 = pars.xpath(xpath_cecha_3_2)
					opis = pars.xpath(xpath_opis)
					cena = pars.xpath(xpath_cena)
					cena_za_m2 = pars.xpath(xpath_cena_za_m2)
					img = pars.xpath(xpath_img)
					oferta_url = pars.xpath(xpath_oferta_url)

					if podtytul:
						podtytul[0] = re.sub('\n', '', podtytul[0])

					x = 1
					for i in podtytul_input:
						podtytul.insert(x, i)
						x += 1
					
					y = 1
					for i in podtytul_input_strong:
						podtytul.insert(y, i)
						y += 1

					wyszukaj_dane.dane.append([' '.join(tytul), ' '.join(podtytul), *cecha_1, ' '.join(cecha_1_2), *cecha_2, ' '.join(cecha_2_2), *cecha_3, ' '.join(cecha_3_2), *opis, *cena, *cena_za_m2, *img, *oferta_url])

			else:

				for i in range(1, 36):

					xpath_tytul = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/header/a/div/div[1]/h2/text()'.format(i)
					xpath_podtytul = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/header/a/div/div[1]/p/text()'.format(i)
					xpath_podtytul_input = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/header/a/div/div[1]/p/span/text()'.format(i)
					xpath_podtytul_input_strong = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/header/a/div/div[1]/p/span/strong/text()'.format(i)
					xpath_cecha_1 = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/div[1]/ul/li[1]/b/text()'.format(i)
					xpath_cecha_1_2 = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/div[1]/ul/li[1]/text()'.format(i)
					xpath_cecha_2_05 = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/div[1]/ul/li[2]/text()'.format(i)
					xpath_cecha_2 = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/div[1]/ul/li[2]/b/text()'.format(i)
					xpath_cecha_2_2 = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/div[1]/ul/li[2]/text()'.format(i)
					xpath_cecha_3_05 = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/div[1]/ul/li[3]/text()'.format(i)
					xpath_cecha_3 = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/div[1]/ul/li[3]/b/text()'.format(i)
					xpath_cecha_3_2 = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/div[1]/ul/li[3]/text()'.format(i)
					xpath_opis = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/div[2]/p/text()'.format(i)
					xpath_cena = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/header/a/div/div[2]/p[1]/text()'.format(i)
					xpath_cena_za_m2 = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/header/a/div/div[2]/p[2]/text()'.format(i)
					xpath_img = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/div[1]/div/div/img/@src'.format(i)
					xpath_oferta_url = '//*[@id="contentPage"]/div[1]/div/div/div/section/div[{}]/div/div/div/section/header/a/@href'.format(i)

					tytul = pars.xpath(xpath_tytul)
					podtytul = pars.xpath(xpath_podtytul)
					podtytul_input = pars.xpath(xpath_podtytul_input)
					podtytul_input_strong = pars.xpath(xpath_podtytul_input_strong)
					cecha_1 = pars.xpath(xpath_cecha_1)
					cecha_1_2 = pars.xpath(xpath_cecha_1_2)
					# cecha_2_05 = pars.xpath(xpath_cecha_2_05)
					cecha_2 = pars.xpath(xpath_cecha_2)
					cecha_2_2 = pars.xpath(xpath_cecha_2_2)
					# cecha_3_05 = pars.xpath(xpath_cecha_3_05)
					cecha_3 = pars.xpath(xpath_cecha_3)
					cecha_3_2 = pars.xpath(xpath_cecha_3_2)
					opis = pars.xpath(xpath_opis)
					cena = pars.xpath(xpath_cena)
					cena_za_m2 = pars.xpath(xpath_cena_za_m2)
					img = pars.xpath(xpath_img)
					oferta_url = pars.xpath(xpath_oferta_url)

					if podtytul:
						podtytul[0] = re.sub('\n', '', podtytul[0])

					x = 1
					for i in podtytul_input:
						podtytul.insert(x, i)
						x += 1
					
					y = 1
					for i in podtytul_input_strong:
						podtytul.insert(y, i)
						y += 1

					wyszukaj_dane.dane.append([' '.join(tytul), ' '.join(podtytul), *cecha_1, ' '.join(cecha_1_2), *cecha_2, ' '.join(cecha_2_2), *cecha_3, ' '.join(cecha_3_2), *opis, *cena, *cena_za_m2, *img, *oferta_url])

	else: 
		wyszukaj_dane.dane.append(['Brak ogłoszeń spełniających Twoje kryteria'])	

def Morizon(lokalizacja, transakcja, rodzaj, rodzaj_zabudowy, typ_domu, komercyjne, typ_dzialki,
		cena_od, cena_do):

	a = {'S': '', 'W': '/do-wynajecia'}
	t = a[transakcja]

	b = {'D': '/nieruchomosci/', 'M': '/mieszkania/', 'Domy': '/domy/', 'K': '/komercyjne/', 'Dz': '/dzialki/', 'G': '/garaze/', 'P': '/pokoje/'}
	if t == '':
		b['G'] = '/sprzedarz/garaze/'
	r = b[rodzaj]

	c = {'d': '', 'A': 'apartamentowiec/', 'B': 'blok/', 'D': 'dom-wielorodzinny/', 'K': 'w-kamienicy/'}
	r_z = c[rodzaj_zabudowy]

	d = {'D': '', 'W': 'wolnostojacy/', 'B': 'blizniak/', 'P': 'palac-dworek/', 'A': 'atrialny/', 'L': 'letniskowy/', 'Sz': 'szeregowiec/', 'K': 'kamienice/', 'B': 'blok/', 'G': 'gospodarstwo/'}
	r_d = d[typ_domu]

	e = {'D': '', 'B': 'biuro/', 'H': ''}
	k = e[komercyjne]

	f = {'D': '', 'R': 'rolna/', 'B': 'budowlana/', 'L': 'lesne/', 'Re': 'rekreacyjna/', 'S': 'siedliska/', 'P': 'przemyslowa/', 'I': 'handlowo-uslugowa/'}
	t_dz = f[typ_dzialki]

	lok_url(lokalizacja)
	lok = lok_url.e 

	cena_url(cena_od, cena_do)
	c_od = cena_url.c_od
	c_do = cena_url.c_do

	wyszukaj_dane(t, r, r_z, r_d, k, t_dz, lok, c_od, c_do)

	Morizon.dane = wyszukaj_dane.dane

	print(t, r, r_z, r_d, k, t_dz, lok, c_od, c_do)
	print(rodzaj, rodzaj_zabudowy, typ_domu, komercyjne, typ_dzialki, cena_od, cena_do)
