'''

daire alanı   :  πr2
daire çevresi :  2πr

yari çapı verilen bir dairenin alan ve çevresini hesaplayınız. (r: 3.14)

'''
pi = 3.14

r = float(input("yarı çap: "))

alan = pi * (r ** 2)

cevre = 2 * pi * r

print("alan: "+ str(alan) + " çevre " + str(cevre))

