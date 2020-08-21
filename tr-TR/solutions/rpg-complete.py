#!/bin/python3

def talimatlariGoster():
    #ekrana ana menü ve komutları yazdır
    print('''
RPG Oyunu
========

Bir anahtar ve iksirle bahçeye git
Canavarlardan kaç!

Yoruluyorsun, her hamlende 1 canın gidecek. 

Komutlar:
  git [yön]
  al [eşya]
''')

def durumuGoster():
  #ekrana oyuncunun durumunu yazdır
  print('---------------------------')
  print(isim + ' şu anda burada: ' + suankiOda)
  print("Can: " + str(can))
  #şu anki envanteri ekrana yazdır
  print("Envanter : " + str(envanter))
  #Eğer varsa ekrana bir eşya yazdır
  if "eşya" in odalar[suankiOda]:
    print('Bir ' + odalar[suankiOda]['eşya'] + ' görüyorsunuz')
  print("---------------------------")

# oyunu kur
isim = None
can = 5
suankiOda = 'Koridor'
envanter = []

#-# KODLARIN BURAYA GELİR #-#
# Dosyadan veri yükle

#bir odayı başka odalara bağlayan bir sözlük
odalar = {

            'Koridor' : { 'güney' : 'Mutfak',
                  'doğu' : 'Oturma Odası',
                  'eşya' : 'anahtar'
                },

            'Mutfak' : { 'kuzey' : 'Oturma Odası',
                  'eşya' : 'canavar'
                },

            'Oturma Odası' : { 'batı' : 'Koridor',
                  'güney' : 'Bahçe',
                  'eşya' : 'iksir'

                },

            'Bahçe' : { 'kuzey' : 'Oturma Odası' }

         }

# oyuncuya adını sor
if isim is None:
  isim = input("Hey maceracı, adın ne? ")
  talimatlariGoster()

#sonsuz döngü
while True:

  durumuGoster()

  #oyuncunun sonraki 'hamle'sini al
  #.split() dizgiyi diziye ayırır
  #ör: 'git batı' yazarsanız şunu elde edersiniz:
  #['git','batı']
  hamle = ''
  while hamle == '':
    hamle = input('>')

  hamle = hamle.lower().split()

  #eğer ilk olarak git yazarlarsa
  if hamle[0] == 'git':
    can = can - 1
    #gitmek istedikleri yere izinleri var mı kontrol et
    if hamle[1] in odalar[suankiOda]:
      #şu anki odayı yeni oda yap
      suankiOda = odalar[suankiOda][hamle[1]]
    #yeni odaya gidebileceği bir kapı (bağlantı) yok
    else:
      print('Bu yoldan gidemezsiniz!')

  #eğer ilk olarak al yazarlarsa
  if hamle[0] == 'al' :
    #odada bir eşya varsa ve almak istedikleri eşya oysa
    if 'eşya' in odalar[suankiOda] and hamle[1] in odalar[suankiOda]['eşya']:
      #o eşyayı envanterlerine ekle
      envanter += [hamle[1]]
      #yardımcı bir mesaj göster
      print(hamle[1] + ' alındı!')
      #odadan o eşyayı sil
      del odalar[suankiOda]['eşya']
    #aksi halde, eşya orada değilse
    else:
      #onlara alamayacaklarını söyle
      print('Bunu alamazsınız: ' + hamle[1] + '!')

  #oyuncu canavar olan bir odaya girerse kaybeder
  if 'eşya' in odalar[suankiOda] and 'canavar' in odalar[suankiOda]['eşya']:
    print('Bir canavar seni yakaladı... OYUN BİTTİ!')
    break

  if can == 0:
    print('Bitkin düştün... OYUN BİTTİ!')

  #oyuncu bahçeye bir anahtar ve iksirle ulaşırsa kazanır
  if suankiOda == 'Bahçe' and 'anahtar' in envanter and 'iksir' in envanter:
    print('Evden kaçtın... KAZANDIN!')
    break

  #-# KODLARIN BURAYA GELİR #-#
  # Oyun verisini dosyaya kaydet