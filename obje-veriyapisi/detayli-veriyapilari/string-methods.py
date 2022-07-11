from email import message
from operator import index


message = 'hello there. my name is Emir Yigit'

# message = message.upper() # tüm harfleri büyük bir şekilde yazdırdı.
# message = message.lower() # tüm harfleri küçük bir şekilde yazdırdı.
# message = message.title()   # sadece baş harfleri büyük
# message = message.capitalize() # sadece ilk harf büyük

# message = message.strip() # hatalı bir boşluk koyulursa onu siliyor 
# message = message.split() # tüm boşluklar bölünerek bize gösterilir
# message = message.split('.') # noktadan itibaren 2 ye ayırıyor

# message = message.split()
# message = ' '.join(message) # splitin ayırdığı kelimeleri birleştirir ve boşluklara bizim istediğim karakteri girer.

# index = message.find('Emir') # cümle içersinde kelime arar.
# print(index)

# isfound = message.startswith('h') # h ile mi başlıyor doğru ise True yanlış ise False
# print(isfound)

# isfound = message.endswith('t') # t ile mi bitiyor doğru ise True yanlış ise False
# print(isfound)

# message = message.replace('emir','osman') # emir bilgisini osmana çevirdi.
# message = message.replace('ö','o').replace('ü','u').replace('ş','s') # türkçe karakterleri çevirdik

# message = message.center(100)  # sağına ve soluna 100 karakterlik boşluk koydu

print(message)