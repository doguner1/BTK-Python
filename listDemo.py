# "BMW,Mercedes,Opel, Mazda" elemanlarına sahib bir liste oluştur
arabalar = ["BMW","Mercedes","Opel", "Mazda"]

# Liste kaç elemanlıdır
result = len(arabalar)

# Listenin ilk ve son elemanı nedir
result = arabalar[0]
result = arabalar[3]
result = arabalar[-1]
# Mazda değerini Toyota ile değiştirin
arabalar[-1] = "Toyota"

# Mercedes listesinin bir elemanı mıdır
result = "Mercedes" in arabalar

# Listenin -2 indeksindeli değer nedir
result = arabalar[-2]

# Listenin ilk 3elemanını alın
result = arabalar[0:3]
result = arabalar[:3]

# Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekle
arabalar[-2:] = ["Toyota","Renault"]

# Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin
result = arabalar + ["Audi", "Nissan"] #-- Arabalar hala 4 değerli sadece iki elemanlı halini resault a ekledik


# Listenin son elemanını silin
del arabalar[-1]

# Liste elemanlarını tersten yazdırın
result = arabalar[::-1]

# Aşağıdaki verileri bir liste içinde saklayınız

         # studentA: = Yiğit Bilgi 2010, (70,60,70)
         # studentB: = Sena Turan 1999, (80,80,70)
         # studentC: = Ahmet Turan 1998, (80,70,90)
studentA = ["Yiğit","Bilgi",2010,[70,60,70]]
#..
#..


# Liste elemanlarını yazdır
result = f"{studentA[0]} {studentA[1]} {2022-studentA[2]} yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}"
print(result)