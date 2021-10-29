import requests
import re
import unicodedata
import math
import time
from bs4 import BeautifulSoup, SoupStrainer
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def lok_url(lokalizacja):

	sub = {'Ł': 'L', 'ł': 'l', 'ẞ': 'SS', 'ß': 'ss'}

	a = re.sub('Ł|ł|ẞ|ß', lambda a: sub[a.group()], lokalizacja)
	b = unicodedata.normalize('NFKD', a).encode('ascii', 'ignore').decode('ascii')
	c = re.sub(' ul[\W_]+| al[\W_]+| sw[\W_]+| ulica[\W_]+| aleje[\W_]+| swietego[\W_]+| swietej[\W_]+| swietych[\W_]+| pl[\W_]+| plac[\W_]+| skwer[\W_]+', ' ', b)
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
	div = SoupStrainer(class_='message-title')
	soup = BeautifulSoup(Wyszukaj.text, 'lxml', parse_only=div).get_text()

	if soup == '':

		try:
			p = SoupStrainer(class_='listing-header__description')
			wyszukan = BeautifulSoup(Wyszukaj.text, 'lxml', parse_only=p).get_text()
			l_wyszukan = re.search('\d+', wyszukan).group()
			print(l_wyszukan)
		except:
			wyszukaj_dane.dane.append(['Brak ogłoszeń spełniających Twoje kryteria'])

		pagin = math.ceil(int(l_wyszukan) / 35)
		pagin_reszta = int(l_wyszukan) % 35

		if pagin > 50:
			pagin = 50
		
		for i in range(1, pagin+1):

			url_p = url
			
			if url.endswith('/'):
				url_p += f'?page={i}'
			else:
				url_p += f'&page={i}'

			wyszukaj = requests.get(url_p)
			div_1 = SoupStrainer(itemscope=True)
			pars = BeautifulSoup(wyszukaj.text, 'lxml', parse_only=div_1)
			wyszukania = pars.find_all("div", itemscope=True)
			wyszukania.pop() 

			for i in wyszukania:

				tytul = i.find('h2').get_text()
				podtytul = i.find('p', class_='single-result__category').get_text().strip().replace('\n\n', ' ')
				cechy = i.find('ul', class_="param list-unstyled list-inline").get_text()
				opis = i.find('div', class_='description single-result__description').get_text()
				cena = i.find('p', class_='single-result__price').get_text()
				cena_za_m2 = ''
				try:
					cena_za_m2 += i.find('p', class_='single-result__price single-result__price--currency').get_text()
				except:
					pass
				img = i.find('img').get('src')
				oferta_url = i.find('a', class_="property_link property-url").get('href')

				# podtytul = re.sub('\n\n|\n', lambda a: ' ' if a.group() == '\n\n' else '', podtytul_1)

				wyszukaj_dane.dane.append([tytul, podtytul, cechy, opis, cena, cena_za_m2, img, oferta_url])

	else: 
		wyszukaj_dane.dane.append(['Brak ogłoszeń spełniających Twoje kryteria Morizon.pl'])	

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

	d = {'D': '', 'W': 'wolnostojacy/', 'B': 'blizniak/', 'P': 'palac-dworek/', 'A': 'atrialny/', 'L': 'letniskowy/', 'Sz': 'szeregowiec/', 'K': 'kamienice/', 'Blok': 'blok/', 'G': 'gospodarstwo/'}
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

	return Morizon.dane


def Gratka_url(lokalizacja, transakcja, rodzaj, rodzaj_zabudowy, typ_domu, komercyjne, typ_dzialki,
		cena_od, cena_do):

	chrome_options = Options()
	chrome_options.headless = True  

	przegladarka = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=chrome_options)

	przegladarka.get('https://www.gratka.pl/nieruchomosci')

	action = ActionChains(przegladarka)

	przegladarka.find_element_by_class_name('crossDialog__close').click()
	print(lokalizacja, transakcja, rodzaj, rodzaj_zabudowy, typ_domu, komercyjne, typ_dzialki,
		cena_od, cena_do)

	if transakcja == 'S':
		pass

	else:
		przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[4]').click()
		przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[4]/div/div/ul/li[2]/span').click()

	if rodzaj == 'D':
		pass

	elif rodzaj == 'M':	

		przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[1]').click()
		przegladarka.find_element_by_xpath('//*[@id="mieszkania-2"]').click()
		time.sleep(0.5)

	elif rodzaj == 'Domy':

		przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[1]').click()
		przegladarka.find_element_by_xpath('//*[@id="domy-9"]').click()
		time.sleep(0.5)

	elif rodzaj == 'K':
		
		przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[1]').click()
		przegladarka.find_element_by_xpath('//*[@id="lokale-uzytkowe-16"]').click()
		
		if komercyjne == 'D':	
			
			przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div/div[3]/ul/li[1]').click()
			time.sleep(0.5)

		elif komercyjne == 'B':

			przegladarka.find_element_by_xpath('//*[@id="biura-17"]').click()
			time.sleep(0.5)

		elif komercyjne == 'H':

			przegladarka.find_element_by_xpath('//*[@id="hale-magazyny-21"]').click()
			time.sleep(0.5)

	elif rodzaj == 'Dz':
		
		przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[1]').click()
		przegladarka.find_element_by_xpath('//*[@id="dzialki-grunty-37"]').click()
		time.sleep(0.2)
		
		if typ_dzialki == 'D':

			przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div/div[3]/ul/li[1]').click()
			time.sleep(0.5)

		elif typ_dzialki == 'R':

			przegladarka.find_element_by_xpath('//*[@id="rolna-42"]').click()
			time.sleep(0.5)

		elif typ_dzialki == 'B':

			przegladarka.find_element_by_xpath('//*[@id="budowlana-38"]').click()
			time.sleep(0.5)

		elif typ_dzialki == 'L':

			przegladarka.find_element_by_xpath('//*[@id="lesna-62"]').click()
			time.sleep(0.5)	

		elif typ_dzialki == 'Re':

			przegladarka.find_element_by_xpath('//*[@id="rekreacyjna-58"]').click()
			time.sleep(0.5)

		elif typ_dzialki == 'S':

			przegladarka.find_element_by_xpath('//*[@id="siedliskowa-66"]').click()
			time.sleep(0.5)

		elif typ_dzialki == 'P':

			przegladarka.find_element_by_xpath('//*[@id="przemyslowa-54"]').click()
			time.sleep(0.5)

		elif typ_dzialki == 'I':

			przegladarka.find_element_by_xpath('//*[@id="inwestycyjna-46"]').click()
			time.sleep(0.5)		

	elif rodzaj == 'G':

		przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[1]').click()
		przegladarka.find_element_by_xpath('//*[@id="garaze-86"]').click()
		przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div/div[3]/ul/li[1]').click()
		time.sleep(0.5)

	elif rodzaj == 'P':

		przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[1]').click()
		przegladarka.find_element_by_xpath('//*[@id="pokoje-120"]').click()
		time.sleep(0.5)

	przegladarka.get(przegladarka.current_url)
	action = ActionChains(przegladarka)

	przegladarka.find_element_by_id('lendiClose').click()
	
	if rodzaj == 'M':
		
		if rodzaj_zabudowy == 'd':
			pass

		elif rodzaj_zabudowy == 'A':

			przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[18]/button').click()
			przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[12]').click()
			przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[12]/div/div/ul/li[4]').click()

		elif rodzaj_zabudowy == 'B':

			przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[18]/button').click()
			przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[12]').click()
			przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[12]/div/div/ul/li[1]').click()

		elif rodzaj_zabudowy == 'D':

			przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[18]/button').click()
			przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[12]').click()
			przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[12]/div/div/ul/li[3]').click()

		elif rodzaj_zabudowy == 'K':

			przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[18]/button').click()
			przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[12]').click()
			przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[12]/div/div/ul/li[2]').click()

		else:
			pass

	if rodzaj == 'Domy':

		if typ_domu == 'D':
			pass

		elif typ_domu == 'W':

			przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[20]/button').click()
			przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[12]').click()
			przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[12]/div/div/ul/li[1]').click()

		elif typ_domu == 'B':

			przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[20]/button').click()
			przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[12]').click()
			przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[12]/div/div/ul/li[2]').click()

		elif typ_domu == 'P':

			przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[20]/button').click()
			przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[12]').click()
			przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[12]/div/div/ul/li[3]').click()

		elif typ_domu == 'A':

			przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[20]/button').click()
			przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[12]').click()
			przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[12]/div/div/ul/li[7]').click()

		elif typ_domu == 'L':

			przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[20]/button').click()
			przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[12]').click()
			przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[12]/div/div/ul/li[8]').click()

		elif typ_domu == 'Sz':

			przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[20]/button').click()
			przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[12]').click()
			przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[12]/div/div/ul/li[4]').click()

		elif typ_domu == 'K' or 'Blok':

			przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[20]/button').click()
			przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[12]').click()
			przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[12]/div/div/ul/li[9]').click()

		elif typ_domu == 'G':

			przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[20]/button').click()
			przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[12]').click()
			przegladarka.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[12]/div/div/ul/li[10]').click()

		else:
			pass			

	if lokalizacja != '':

		search_box = przegladarka.find_element_by_name('lokalizacja_region')
		action.move_to_element(search_box).perform()
		search_box.send_keys(lokalizacja)
		time.sleep(0.2)
		action.move_by_offset(0, 30).click().perform()

	przegladarka.find_element_by_name('cena-calkowita_min').click()
	
	c_od = przegladarka.find_element_by_name('cena-calkowita_min')
	# action.move_to_element(c_od).perform()
	c_od.send_keys(cena_od)

	c_do = przegladarka.find_element_by_name('cena-calkowita_max')
	# action.move_to_element(c_do).perform()
	c_do.send_keys(cena_do)		

	submit = przegladarka.find_element_by_class_name('generator__applyFilters')
	submit.click()
	submit.click()

	try:
		time.sleep(1)
		Gratka_url.url = przegladarka.current_url
		print(Gratka_url.url)
	finally:	
		przegladarka.quit()

def Gratka_wyszukaj_dane(url):

	Gratka_wyszukaj_dane.dane = []

	# try:
	Wyszukaj = requests.get(url)
	span = SoupStrainer(class_='listingHeader__offersCount ')
	l_wyszukan = int(re.sub('\s', '', BeautifulSoup(Wyszukaj.text, 'lxml', parse_only=span).get_text().strip('()')))

	if l_wyszukan != 0:

		pagin = math.ceil(l_wyszukan / 32)
		pagin_reszta = l_wyszukan % 32

		if pagin > 50:
			pagin = 50
		
		for i in range(1, pagin+1):

			url_p = url + f'?page={i}'

			wyszukaj = requests.get(url_p)
			article = SoupStrainer(class_='teaserUnified')
			pars = BeautifulSoup(wyszukaj.text, 'lxml', parse_only=article)
			wyszukania = pars.find_all('article', class_='teaserUnified') 

			for i in wyszukania:

				tytul = i.find('a', class_='teaserUnified__anchor').get_text()
				podtytul = ''
				cechy = ''
				prep_cechy = i.find_all('ul', class_='teaserUnified__params')
				for ul in prep_cechy:
					lista_li = ul.find_all('li', class_='teaserUnified__listItem')
					for li in lista_li:
						cechy += li.get_text()
				opis = i.find('p', class_='teaserUnified__description').get_text().strip()
				cena = re.sub('(?<=\D{3})[\w\W]*|(?<=\D{4})[\w\W]*', '', i.find('p', class_='teaserUnified__price').get_text().strip())
				cena_za_m2 = ''
				try:
					cena_za_m2 += i.find('span', class_='teaserUnified__additionalPrice').get_text().strip()
				except:
					pass
				img = i.find('img').get('src')
				oferta_url = i.find('a').get('href')

				# podtytul = re.sub('\n\n|\n', lambda a: ' ' if a.group() == '\n\n' else '', podtytul_1)

				Gratka_wyszukaj_dane.dane.append([tytul, podtytul, cechy, opis, cena, cena_za_m2, img, oferta_url])

	else: 
		Gratka_wyszukaj_dane.dane.append(['Brak ogłoszeń spełniających Twoje kryteria Gratka.pl'])
	# except:
	# 	Gratka_wyszukaj_dane.dane.append(['Wystąpił błąd na Gratka.pl. Spróbuj jeszcze raz.'])		

def Gratka(lokalizacja, transakcja, rodzaj, rodzaj_zabudowy, typ_domu, komercyjne, typ_dzialki,
		cena_od, cena_do):

	Gratka.dane = []

	try:
		Gratka_url(lokalizacja, transakcja, rodzaj, rodzaj_zabudowy, typ_domu, komercyjne, typ_dzialki,
		cena_od, cena_do)
		Gratka_wyszukaj_dane(Gratka_url.url)
		Gratka.dane = Gratka_wyszukaj_dane.dane
	except:
		Gratka.dane.append(['Wystąpił błąd na Gratka.pl. Spróbuj jeszcze raz.'])

	return Gratka.dane

# def Otodom(lokalizacja, transakcja, rodzaj, rodzaj_zabudowy, typ_domu, komercyjne, typ_dzialki,
# 		cena_od, cena_do):

# 	if rodzaj == 'P':
# 		Otodom.dane = []

# 	a = {'D': '/nieruchomosci/', 'M': '/mieszkanie/', 'Domy': '/dom/', 'K': '/lokal-uzytkowy/', 'Dz': '/dzialke/', 'G': '/garaz/'}
# 	r = [rodzaj]

# 	b = {'S': 'sprzedam', 'W': 'wynajme'}
# 	t = b[transakcja]

# 	c = {'d': '', 'A': 'apartamentowiec/', 'B': 'blok/', 'D': 'dom-wielorodzinny/', 'K': 'w-kamienicy/'}
# 	r_z = c[rodzaj_zabudowy]

# 	d = {'D': '', 'W': 'wolnostojacy/', 'B': 'blizniak/', 'P': 'palac-dworek/', 'A': 'atrialny/', 'L': 'letniskowy/', 'Sz': 'szeregowiec/', 'K': 'kamienice/', 'B': 'blok/', 'G': 'gospodarstwo/'}
# 	r_d = d[typ_domu]

# 	e = {'D': '', 'B': 'biuro/', 'H': ''}
# 	k = e[komercyjne]

# 	f = {'D': '', 'R': 'rolna/', 'B': 'budowlana/', 'L': 'lesne/', 'Re': 'rekreacyjna/', 'S': 'siedliska/', 'P': 'przemyslowa/', 'I': 'handlowo-uslugowa/'}
# 	t_dz = f[typ_dzialki

def Gumtree_cena_url(lokalizacja, cena_od, cena_do):

	c = ''

	if cena_od == '' and cena_do == '':
	    pass
	elif lokalizacja == '':
	        c = '?pr=' + cena_od + ',' + cena_do
	else:
	    c = '&pr=' + cena_od + ',' + cena_do

	Gumtree_cena_url.cena = c.rstrip(',')

def Gumtree_lok_url(lokalizacja):

	a = re.sub(' ul[\W_]+| al[\W_]+| sw[\W_]+| ulica[\W_]+| aleje[\W_]+| swietego[\W_]+| swietej[\W_]+| swietych[\W_]+| pl[\W_]+| plac[\W_]+| skwer[\W_]+', ' ', lokalizacja).strip()
	b = re.sub('[\W_]+', '+', a).lower()
	Gumtree_lok_url.c = '?q=' + b

def Gumtree_wyszukaj_dane(r, r_z, r_d, k, t_dz, lok, cena):

	Gumtree_wyszukaj_dane.dane = []

	url = 'https://www.gumtree.pl{}{}{}'.format(r, lok, cena)
	Wyszukaj = requests.get(url)
	div = SoupStrainer(class_='message')
	soup = BeautifulSoup(Wyszukaj.text, 'lxml', parse_only=div).get_text()
	p = SoupStrainer(class_='error-content')
	soup2 = BeautifulSoup(Wyszukaj.text, 'lxml', parse_only=p).get_text()
	div2 = SoupStrainer(class_='error-msg')
	soup3 = BeautifulSoup(Wyszukaj.text, 'lxml', parse_only=div2).get_text()

	if soup == '' and soup2 == '' and soup3 == '' and r_z == 'd' and r_d == 'D' and k == 'D' and t_dz == 'D' and r != 'K' and r != 'G':

		try:
			span = SoupStrainer(class_='breadcrumbs')
			wyszukan = BeautifulSoup(Wyszukaj.text, 'lxml', parse_only=span).get_text()
			l_wyszukan = re.search('\d+', wyszukan).group()
		except:
			Gumtree_wyszukaj_dane.dane.append(['Brak ogłoszeń spełniających Twoje kryteria Gumtree.pl'])

		pagin = math.ceil(int(l_wyszukan) / 20)
		pagin_reszta = int(l_wyszukan) % 20

		if pagin > 50:
			pagin = 50
		
		for i in range(1, pagin+1):

			# url_p = re.sub(r'\b(?=v1c)', 'page-' + str(i) + '/', url)
			url_p = re.sub('\d$|\d(?=\?)', str(i), url)

			# url_p = url
			# url_p += f'/page-{i}'

			wyszukaj = requests.get(url_p)
			div_1 = SoupStrainer(class_='tileV1')
			pars = BeautifulSoup(wyszukaj.text, 'lxml', parse_only=div_1)
			wyszukania = pars.find_all('div', class_='tileV1') 

			for i in wyszukania:

				tytul = i.find('a', class_='href-link').get_text()
				podtytul = ''
				cechy = ''
				opis = i.find('div', class_='description').get_text()
				cena = i.find('span', class_='value').get_text().strip()
				cena_za_m2 = ''
				img = ''
				try:
					img = i.find('img').get('data-src')
				except:
					pass
				oferta_url = 'https://www.gumtree.pl' + i.find('a', class_='href-link').get('href')

				# podtytul = re.sub('\n\n|\n', lambda a: ' ' if a.group() == '\n\n' else '', podtytul_1)

				Gumtree_wyszukaj_dane.dane.append([tytul, podtytul, cechy, opis, cena, cena_za_m2, img, oferta_url])

	else: 
		Gumtree_wyszukaj_dane.dane.append(['Brak ogłoszeń spełniających Twoje kryteria Gumtree.pl'])



def Gumtree(lokalizacja, transakcja, rodzaj, rodzaj_zabudowy, typ_domu, komercyjne, typ_dzialki,
		cena_od, cena_do):

	t = transakcja

	b = {'D': '/s-nieruchomosci/v1c2p1', 'M': '/s-mieszkania-i-domy-sprzedam-i-kupie/mieszkanie/v1c9073a1dwp1', 'Domy': '/s-mieszkania-i-domy-sprzedam-i-kupie/dom/v1c9073a1dwp1', 'K': '', 'Dz': '/s-dzialki/v1c9194p1', 'G': '', 'P': '/s-pokoje-do-wynajecia/v1c9000p1'}
	if t == 'W':
		b.update({'M': '/s-mieszkania-i-domy-do-wynajecia/mieszkanie/v1c9008a1dwp1', 'Domy': '/s-mieszkania-i-domy-do-wynajecia/dom/v1c9008a1dwp1'}) 
	r = b[rodzaj]

	r_z = rodzaj_zabudowy

	r_d = typ_domu

	k = komercyjne

	t_dz = typ_dzialki

	Gumtree_lok_url(lokalizacja)
	lok = Gumtree_lok_url.c

	Gumtree_cena_url(lokalizacja, cena_od, cena_do)
	cena = Gumtree_cena_url.cena

	Gumtree_wyszukaj_dane(r, r_z, r_d, k, t_dz, lok, cena)

	Gumtree.dane = Gumtree_wyszukaj_dane.dane

	return Gumtree.dane
	