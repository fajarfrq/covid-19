import os,time
try:
	import requests
except:
	os.system('pip intsall requests')
	
ck = requests.Session()

def menu():
	print('[ \x1b[31mCOVID-19 Case Data\x1b[37m ]')
	print('-'*49)
	print('''[+] Author    : Vrx                           [+]
[+] Instagram : fajarid05_                    [+]
[+] Version   : 1.0                           [+]
[+] Source Api: 'https://api.kawalcorona.com' [+]''')
	print('-'*49)
	banner()
def banner():
	print('[ \x1b[32mCommand\x1b[37m ]')
	print('''[!] prov : Melihat seluruh data di Provinsi
[!] indo : Melihat seluruh data di Indonesia
[!] world: Melihat seluruh data di Dunia     
[!] exit : Untuk Keluar''')
	print('')
	pilih = input('[?]command/> ')
	if pilih == 'Indo' or pilih == 'indo':
		indonesia()
	elif pilih == 'prov' or pilih == 'Prov':
		provinsi()
	elif pilih == 'world' or pilih == 'World':
		world()
	elif pilih == 'exit' or pilih == 'Exit':
		print('bye.....')
		time.sleep(2)
		exit()
	else:
		print()
		banner()
def indonesia():
	indonesia = ck.get('https://api.kawalcorona.com/indonesia')
	data = indonesia.json()
	negara = data[0]['name']
	positif = data[0]['positif']
	sembuh = data[0]['sembuh']
	mati = data[0]['meninggal']
	print('')
	print('[ Data Terkini Di Indonesia ]')
	print('-'*30)
	print()
	print('[*] Negara    : ',negara)
	print('[*] Positif   : '+ str(positif) + ' orang')
	print('[*] \x1b[32mSembuh\x1b[37m    : '+ str(sembuh) + ' orang')
	print('[*] \x1b[31mMeninggal\x1b[37m : '+ str(mati) + ' orang')
	print('')
	input('[\x1b[31mback\x1b[37m]')
	menu()
def provinsi():
	url_prov = ck.get('https://api.kawalcorona.com/indonesia/provinsi')
	data_prov = url_prov.json()
	print()
	print('[ \x1b[31mData Di Setiap Provinsi Di Indonesia\x1b[37m ]')
	print('-'*40)
	print('')
	for x in data_prov:
		nama_prov = (x['attributes']['Provinsi'])
		positif = (x['attributes']['Kasus_Posi'])
		sembuh = (x['attributes']['Kasus_Semb'])
		mati = (x['attributes']['Kasus_Meni'])
		print('[*] Provinsi  :',nama_prov)
		print('[*] Positif   : '+ str(positif) + ' orang')
		print('[*] \x1b[32mSembuh \x1b[37m   : '+ str(sembuh) + ' orang')
		print('[*] \x1b[31mMeninggal\x1b[37m : ' + str(mati) + ' orang')
		print()
	print('[*] Total Provinsi :',len(data_prov))
	print()
	input('[\x1b[31mback\x1b[37m]')
	menu()
def world():
	positif = ck.get('https://api.kawalcorona.com/positif').json()
	sembuh = ck.get('https://api.kawalcorona.com/sembuh').json()
	mati = ck.get('https://api.kawalcorona.com/meninggal').json()
	ttl_positif = positif['value']
	ttl_sembuh = sembuh['value']
	ttl_mati = mati['value']
	print('')
	print('[ \x1b[31mData Kasus COVID-19 Di Seluruh Dunia\x1b[37m ]')
	print('-'*40)
	print('[*] Total Positif   : '+ str(ttl_positif) + ' orang')
	print('[*] \x1b[32mTotal Sembuh\x1b[37m    : '+ str(ttl_sembuh) + ' orang')
	print('[*] \x1b[31mTotal Meninggal\x1b[37m : '+ str(ttl_mati) + ' orang')
	print()
	input('[\x1b[31mback\x1b[37m]')
	menu()

menu()
	