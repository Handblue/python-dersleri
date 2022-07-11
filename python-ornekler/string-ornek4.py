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

result = course.lower()
print(course)