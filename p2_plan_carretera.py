#https://replit.com/join/kiszeapzwf-danielgonzal232

x = float(input("Dame la distancia a recorrer en millas: "))
y = float(input("Dame el rendimiento en millas por galón de tu automóvil: "))
z = float(input("Dame el precio actual de la gasolina: "))
v = int(input("¿Cuántos días planeas viajar? "))

cd = (x / y) * z
ct = cd * v  

print("El costo total del viaje es", ct)
