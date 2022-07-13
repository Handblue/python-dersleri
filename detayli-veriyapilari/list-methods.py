numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a','g','s','b','y','a','s']

val = min(numbers) # minimum değer
val = max(numbers) # max değer

val = min(letters)
val = max(letters)

val = numbers[3:6] # 3. indexten 5 e kadar al

numbers[4] = 40 # indexte 4 olanı 40 yaptı

numbers.append(50) # listemize 50 yi ekledik

numbers.insert(3, 25) # 3. indexten sonra 25i ekle dedik

numbers.insert(-1, 112) # en sona ekleme yaptık 112yi ekledik

numbers.pop() # eleman silme
numbers.pop(0) # sıfırıncı indexteki eleman silinir.

numbers.remove(112) # istenilen veriyi bul ve sil (112 silinecek)

numbers.sort() # sayısal büyüklük olarak sıralanır.
numbers.reverse() # tam tersini yapar

numbers.clear() # tüm elemanları temizler/siler.


#print(numbers)
#print(val)


#başlarda print(val) komutunu kullanıyoruz daha sonra print(numbers) e geçiyoruz deneyerek öğrenin.


#  https://www.w3schools.com/python/python_ref_list.asp
#  https://docs.python.org/3/tutorial/datastructures.html