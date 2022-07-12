from email import message
from unittest import result


website = "http://www.sadikturan.com"
course = "python kursu: baştan sona python"

# hello word karakter dizisinin bas ve sondaki boşluk karakterini silin.
'''
result = ' hello word '.strip() # normal olarak baş ve sonraki boşlukları siler
result = ' hello word '.lstrip() # left in l si bu yüzden soldaki boşluklar gider
result = ' hello word '.rstrip() # rigth ın r si sağki boşluklar

result = website.lstrip('/:pth') # / : p t h karakterlerini sildi.

print(result)

'''

# www.sadikturan.com içindeki sadikturan bilgisi dışındaki bilgileri silin.
'''
result = website.strip('/:pth.comw') 
print(result)

#2. yöntem 
result = 'www.sadikturan.com'.strip('w.moc')

'''

# course karakter dizisinin tüm karakterlerini küçük yap
'''
result = course.lower()
print(result)

'''
# web site içinde kaç tane a karakteri vardır
'''
result = website.count('a') # sorunun cevabı
result = website.count('www') # sadece www göster
result = website.count('www',0,10) # sıfır ile on arasında ise bize göster
print(result)

'''

# 'website' "www" ile başlayıp com ile bitiyor mu?
'''
result = website.startswith('www') # false değerimi aldık
result = website.startswith('http') # true döndü
result = website.startswith('com') # true döndü 

print(result)

'''

# 'website' içinde '.com' ifadesi var mı?
'''
result = website.find('.com') # sorunun cevabı
result = website.index('com') # alternatif çözüm

result = course.rfind('python')  # sağdan başlayarak sayar.
result = website.rindex('com') # sağdan saymaya başlar. (r = right)
result = website.rindex('com') # hata mesajı döner exception

print(result)

'''

# 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
'''
result = course.isalpha() # false döndü
result = 'hello'.isalpha() # kendimiz değişken tanımladık true döndü
result = course.isdigit() # gelen değerler rakam mı? false döndü
result = '123'.isdigit() # şimdi true değerini aldık çünkü rakamsal ifade var.

print(result)

'''

# 'Contents' ifadesini satırda 50 karakter içinde yerleştirip sağ ve soluna * ekleyiniz.
'''
result = 'Contents'.center(50,'*') # sağda ve solda yıldız
result = 'Contents'.rjust(50,'*') # sadece sağ da yıldız
result = 'Contents'.ljust(50,'*') # sadece sol da yıldız

print(result)

'''

# 'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
'''
result = course.replace(' ','-') # çözüm
result = course.replace(' ','-',5) # sadece 5 adet çizgi koyar
result = course.replace(' ','') # boşlukları sil

print(result)

'''

# 'hello world' karakter dizisinin 'world' ifaadesini 'there' olarak değiştiriniz.

'''
result = 'hello world'.replace('world','there')

print(result)

'''

# 'course' karakter dizisini boşluk karakterlerinden ayırın.
'''
result =course.split(' ')
result = result[2] # 2. ifadesindeki kelimeyi alıyor. (baştan) 0,1,2 diye gidiyor.
result = result[3]

print(result)

'''