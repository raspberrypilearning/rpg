#!/bin/python3

# Talimatlar yayınlanınca RPG başlangıç projesini bu kodla değiştir

def talimatlariGoster():
  #ekrana ana menü ve komutları yazdır
  print('''
RPG Oyunu
========
Komutlar:
  git [yön]
  al [eşya]
''')

def durumuGoster():
  #ekrana oyuncunun durumunu yazdır
  print('---------------------------')
  print('Şu anda buradasınız: ' + suankiOda)
  #şu anki envanteri ekrana yazdır
  print('Envanter : ' + str(envanter))
  #Eğer varsa ekrana bir eşya yazdır
  if "eşya" in odalar[suankiOda]:
    print('Bir ' + odalar[suankiOda]['eşya'] + ' görüyorsunuz')
  print("---------------------------")

#ilk başta boş olan bir envanter
envanter = []

#bir odayı başka odalara bağlayan bir sözlük
odalar = {

            'Koridor' : { 
                  'güney' : 'Mutfak'
                },

            'Mutfak' : {
                  'kuzey' : 'Koridor'
                }

         }

#oyuncuyu Koridorda başlat
suankiOda = 'Koridor'

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
    if "eşya" in odalar[suankiOda] and hamle[1] in odalar[suankiOda]['eşya']:
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

