from collections import abc
from ensurepip import bootstrap
from unittest import result


website = "http://www.sadikturan.com"
course = "python kursu: baştan sona python"

#1 'course' karakter dizisinde kaç karakter vardır?

'''
result = len(course)
print(result)

'''
#2 web site içinden www karakterlerini alın. 

'''

result = website[7:10]
print(result)

'''
#3 website içinden com karakterini alın

'''
result = website[22:25]
print(result)

result = website[length-3:length] #alternatif
'''

#4 course içinden ilk 15 ve son 15 karakteri alın

'''
result = course[0:15]
result = course[:15]
result = course[-15:]
print(result)

'''

#5 course ifadesindeki karakterleri tersten yazdırın

'''
result = course[::-1]
print(result)

'''
#6 aşağıda verilen değişkenler ile ekrana ifadeyi yazdırın.
#  'benim adım borsa yilmaz, yasim 32 ve meslegim mühendis.'
#   ad, soyad, yas, is = bora, yilmaz, 32, muhendis

'''
ad = ('bora') 
soyad = ('yilmaz')
yas = 32
meslek = ('muhendis')

print(f'benim adim {ad} soyadım {soyad} yasim {yas} meslegim {meslek}')

'''
#7 hello world ifadesindeki w harfini w ile değiştirin

'''
s = 'hello wordl'
result = s[0:6] + 'W' + s[-4:]
print(s)

print(result)

'''

#8 abc ifadesini yan yana 3 defa yazdırın

'''
result = "abc "
print (result *3)

'''





