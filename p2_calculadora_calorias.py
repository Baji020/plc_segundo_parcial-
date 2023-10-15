#https://replit.com/join/cjvzhjxbdm-danielgonzal232

x = float(input("Dame tu peso en kg: "))
y = float(input("Dame el tiempo de actividad fisica en minutos: "))
z = input("Dame el tipo de ejercicio(correr, nadar, andar en bicicleta): ")

if z == "correr":
  cm = 0.077
elif z == "nadar":
  cm = 0.074
elif z == "andar en bicicleta":
  cm = 0.035

cq = cm * x * y
print("Las calorias quemadas ", cq)
