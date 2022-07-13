from lib2to3.pytree import type_repr
from tkinter.font import names


list = [1,2,3]

tuple = (1, 'iki', 3)

print(type(list))
print(type(tuple)) # tipini öğrendik


print(list[2])
print(tuple[2]) # 2. elemanlarında ne var onu sorguladık.

print(len(list))  
print(len(tuple)) # eleman sayılarını yazdırdık

list = ['ali','veli']
tuple = ('damla','ayşe')
print(list)
print(tuple) # önceli içeriği sil ve bunu ekle

list = ['ali','veli']
tuple = ('damla','ayşe')
names = ('osman','hakkı','Emir') + tuple

print(names) #tuple ve names bilgilerini birleştirdi.