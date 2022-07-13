


from operator import index
from unittest import result


names = ['Ali','Yağmur','Hakan','Deniz']
years = [1998, 2000, 1998, 1987]

# 1- "Cenk" ismini listenin sonuna ekleyiniz.
names.append('Cenk')
print(names)

# 2- "Sena" değerini listenin başına ekleyiniz.
names.append('Sena')
print(names)

# 3- "Deniz" ismini listeden siliniz.
names.remove('Deniz')
print(names)


# 4- "Deniz" isminin indeksi nedir ?
# index = names.index('Deniz')  # denizi az önce sildiğimiz için hata verecektir fakat kod doğru
# print(index)


# 5- "Ali" listenin bir elemanı mıdır ?
result = 'Ali' in names
result = names.index('Ali') # 2. yol - alinin index değerine bakıyoruz -1 den büyükse vardır.
print(result)


# 6- Liste elemanlarını ters çevirin.
names.reverse()
print(names)


# 7- Liste elemanlarını alfabetik olarak sıralayınız.
names.sort()
print(names)

# 8- years listesini rakamsal büyüklüğe göre sıralayınız.
years.sort()
print(years)


# 9- str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.
str = "Chevrolet,Dacia"
result = str.split(',')
print(result)


# 10- years dizisinin en büyük ve en küçük elemanı nedir ?
min = min(years)
max = max(years)
print(min, max)


# 11- years dizisinde kaç tane 1998 değeri vardır ?
result = years.count(1998)
print(result)


# 12- years dizisinin tüm elemanlarını siliniz.
years.clear()
print(years)


# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.

markalar = []

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

print(markalar)






