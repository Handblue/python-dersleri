
name = 'Emir'
surname = 'Yigit'
age = 22

# print(' my name is {} {}'.format(name, surname))  # ilk yol

# print(' my name is {1} {0}'.format(name, surname))  # indexleri değiştirdik böylece yigit emir oldu

# print(' my name is {s} {n}'.format(n=name, s=surname)) #sayı vermek yerine harf verdik burada da gayet kolay

# print(" my name is {} {} I am {} years old.".format(name, surname, age)) # yaş değişkeni ekledik
 

# result = 200 / 700

# print('the result is {r:1.3}'.format(r=result)) # {r:1.3} bilgisinde ki 3 bilgisi virgülden sonra basamak olacağını gösteriyor. 1 bilgisi ise kaç karakterlik boşluk bırakacağını ögtseriyor.

print(f" my name is {name} {surname} I am {age} years old.") # sadece başlarına f koyduk ve süslü parantez içersinde yazabiliyor olduk. Kolay.
