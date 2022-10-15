website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

#1 "course" karekter dizisinde kaç karekter bulunmakta?
result = len(website)
length = len(website)

#2 "website" içinde www karekterlerini alın
result = website[7:10]

#3 "website" içinden com karekterini alın
result = website[22:25]
result = website[length-3:length]

#4 "course" içinden ilk 15 ve son 15 karekterlerini alın
result = course[:15]
result = course[-15:]

#5 "course" ifadesindeki karakterleri tersten yazdırın
result = course[::-1]


name, surname, age, job = "Bora","Yılmaz","32","mühendis"

#6 Yukarıda verilen değişken ile ekrena aşağıdaki ifadeyi yazınız
## "Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis."
result = "Benim adım " +name+ " "+surname+", Yaşım "+ str(age)+ " ve mesleğim "+job
result = "Benim adım {} {}, Yaşım {} ve mesleğim {}.".format(name,surname,age,job)
result = f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}."


#7 "Heloo world" ifadesindeki w harfini W ile değiştir
s = "Hello world"
s = s[0:6] + "W" + s[-4:]
s.replace("w","W")
result = s

#8 "abc" ifadesini yan yana 3 defa yazdırın
result = "abc" * 3