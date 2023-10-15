#https://replit.com/join/tqtdhokuxi-danielgonzal232

x = float(input("Dame tu edad: "))
y = float(input("A que edad te piensas jubilar: "))
z = float(input("Dame la cantidad deseada para jubilarte: "))
v = float(input("Dame tu rendimiento actual en porcentaje: "))
t = y - x  
n = t * 12  
r = v / 12  

pmt = z * (r / (1 - (1 + r) ** -n))

print("Lo que tienes que ahorrar mensualmente es", pmt)

