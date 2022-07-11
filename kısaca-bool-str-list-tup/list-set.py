
liste = ['a','b','c','d','e','a']
print(liste)

liste = liste + ['f'] #listeye f harfini ekledik
print(liste)

print(liste[3:5])

liste.append('g') #kolay yoldan g harfini listeye ekledik
print(liste)

print(liste.pop()) #son eklediğimiz g harfini attı.

print(liste.pop(5)) #5. indexte olan harfi attık
print(liste) 

########################################

sayilar = [1,5454,87456,6655,1]
sayilar.sort() # büyükten küçüğe düzenliyor
print(sayilar)

print(set(sayilar)) # set yazmak çift olan şeyleri teke düşürüyor ve süslü parantez içine alıyor.