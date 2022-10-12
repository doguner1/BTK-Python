
'''
x = input("1. sayı: ")
y = input("2. sayı ")

toplam = x + y
toplamint = int(x) + int(y)
print("Toplam1 " + toplam) #1010
print("Toplam2 " + str(toplamint)) #20
'''


x = 5
y = 1.5
name = "Doğu"
isOnline = True


#-- int to float --

x = float(x)
print(x) # 5.0
print(type(x)) #float

#-- float to int --
y = int(y)
print(y) # 1
print(type(y)) #int

#-- int and float to str --
result = str(x) + str(y)
print(result)
print(type(result))

#-- bool to str --
isOnline = str(isOnline)
print(isOnline)
print(type(isOnline))

#-- bool to int --
isOnline = int(isOnline)
print(isOnline) #1
print(type(isOnline)) #int