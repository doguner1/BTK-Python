number = [1,2,3,4]
letters = ["s","g","f","t"]

val = min(number)
val = max(number)

number.append(49)
number.append("23") #string de ekledi
number.insert(3,78) #3.index e 78 ekledi

number.pop() #sondaki eleman silindi
number.pop(0) #baştaki eleman silindi
number.remove(49) #49 u bul ve sil demek

number.sort() #liste sıralı bir şekillendi
number.reverse() #terse göre sıralandı

print(number.count(10)) #10 dan kaçtane var sayar
number.clear() #hepsini temizledi