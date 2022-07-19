#liczenie ilości liter w wyrazie

var="Gdańsk"

i=0 #początkowy indeks liczonych liter w zmiennej

while i<len(var):
    print(var[i])
    i+=1
    
print("Letter count:",len(var))
