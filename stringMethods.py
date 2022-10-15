message = "Hello There. My name is Sadık Turan"

message = message.upper() #- Her harf büyük yazılır
message = message.lower() #- Her harf küçük yazılır
message = message.title() #- Her kelimenin baş harfi büyük yazılır
message = message.strip() #- Girilen kelimenin başında ve sonundaki boşluk karekterini siler(passwd)
message = message.split() #- Cümleyi parçaya ayırdı. Haliyle [] şeklinde o kelimeyi çağırabilirsin
message = message.split(".") #- noktada bir parçala demek
message = " ".join(message) #-Parçalanmış cümleleri bir araya getirir araya da boşluk ekledik