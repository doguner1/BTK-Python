'''
Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız

Daire Alanı : pi r*2
Daire Çevresi : 2 pi r

(pi : 3.14)
'''

yarıCap = float(input("Yarı çap: "))
pi = 3.14

DaireAlanı = 3.14 * float(yarıCap**2)
DaireCevresi = float(2) * pi * float(yarıCap)

print("Daire Alanı: " + str(DaireAlanı))
print("Daire Çevresi : " + str(DaireCevresi))

