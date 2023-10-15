#https://replit.com/join/xplsihnjmg-danielgonzal232

x = input("Que quieres convertir(a) millas, b) litros o c) grados Fahrenheit): ")

if x == "a":
  m = float(input("Dmae el numero de millas: "))
  k = m * 1.609
  print("En kilometros es", k)

elif x == "b":
  l = float(input("Dame el numero de litros: "))
  g = l * 0.264
  print("En galones es", g)

elif x == "c":
  f = float(input("Dame el numero en fahrenheit: "))
  c = (f - 32) * 5 / 9
  print("En celcius es", c)


