# 1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.

# 2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.


ogrenciler = {}

number = input("ogrenci no: ")
name = input("öğrenci adı: ")
surname = input("ogrenci soyadı: ")
phone = input("ogrenci telefon: ")

# ogrenciler[number] = {
#    'ad': name,
#    'soyad': surname,
#    'telefon': phone          # aynısnı update methodu ile yapacağzı
# }

ogrenciler.update({
   number: {
      'ad': name,            # update kullanarak birden fazla veri ekleyebiliriz
      'soyad': surname,
      'telefon': phone
   }
})

print(ogrenciler)

ogrNo = input('öğrenci no: ')
ogrenci = ogrenciler[ogrNo]
print(ogrenci)

print(f"Aradığın {ogrNo} nolu öğrencinin adı: {ogrenci['ad']} soyadı: {ogrenci['soyad']} ve telefonu ise {ogrenci['telefon']}")