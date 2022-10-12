
name = "Doğu"
surname ="Güner"
age = 23
print("My name is {} {}".format(name,surname))
print("My name is {1} {0}".format(name,surname)) #Yer değişti yerleştirme işleminde
print("My name is {} {} and I am {} years old.".format(name,surname,age))
#Hemen üstdeki yani 7 satırdaki kod da age kısmında bir çevirme işlemi yapmadığımıza dikkat

result = 200 / 700
print(result) #0.4
print("the result is {}".format(result)) #the result is 0.2857142857142857
print("the result is {r:1.3}".format(r=result))
#Buradaki 3 virgülden sonra kaç basamak olacağını gösteriyor

print(f"My name is {name} {surname} and I am {age} years old.") #f string