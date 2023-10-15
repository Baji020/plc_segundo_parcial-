#https://replit.com/join/bmxuwfyzty-danielgonzal232

x = float(input("Dame el precio del producto: "))
y = float(input("Cuantos quieres: "))
z = input("Que categoria es (A, B o C)")
if z == "A" or z == "a":
  e = (x * y) * 0.10
  print("El total es de", e)
elif z == "b" or z == "B":
  e = (x * y) * 0.05
  print("El,total es de", e)
elif z == "c" or z == "C":
  e = (x * y) * 0.02
  print("El total es de", e)
