# "Bmw , Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.

cars = ['Bmw' , 'Mercedes', 'Opel', 'Mazda']
print(cars)

# liste kaç elemanlıdır

result = len(cars)


# listenin ilk ve son elemanı nedir?

result = cars[0]
result = cars[3]

# mazda değerini toyota ile değiştir

# cars[-1]= 'Toyota'    # bu kısmı yorum satırı yapmazsanız aşağıdaki bazı kodlar çalışmaz
# result = cars

# Mercedes listenin bir elemanı mıdır

result = 'Mercedes' in cars # true döndü
result = 'Mercedesss' in cars # false döndü

# listenin -2 indexindeki değer nedir?

result = cars[-2] 

# listenin ilk 3 elemanını alın.

result = cars[0:3]
result = cars[:3] # aynı sonuç gelir

# listenin son 2 elemanını yerine "toyota" ve "renault" değerini ekleyin.

cars[-2:] = ['Toyota', 'Renault'] 
result = cars

# listenin üzerinde "audi" ve "nissan" değerini ekleyin

result = cars + ['Audi', 'Nissan']

# listenin son elemanını silin.

del cars[-1]
result = cars

# liste elemalarını tersten yazdırınız.

result = cars[::-1]

# aşağıdaki verileri bir liste içerisinde saklayınız.

    # studentA: Yiğit Bilgi 2010, (70,60,70)
    # studentB: Sena Turan 1999, (80,80,70)
    # studentC: Ahmet Turan 1998, (80,70,90)

studentA = ['yigit','Bilgi',2010,[70,60,70]]
studentB = ['sena','turan',1999,[80,80,70]]
studentC = ['ahmet','turan',1998,[80,70,90]]




#liste elemanlarını ekrana yazdırınız.

result = studentA[0]
result = studentB[1]
result = studentC[3][1]

result = f"{studentA[0]} {studentA[1]} {2019-studentA[2]} yaşında ve ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}"

print(result)


