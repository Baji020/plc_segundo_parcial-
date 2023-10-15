#https://replit.com/join/bmxuwfyzty-danielgonzal232

x = float(input("Dame el precio del producto: "))
y = float(input("Cuantos quieres: "))
z = input("Que categoria es (A, B o C):")

if z.lower() == "a":
    s = 0.10
elif z.lower() == "b":
    s = 0.05
elif z.lower() == "c":
    s = 0.02

f = x * y * s
print("El total es de", f)

if y > 10:
    j = f * 0.05
    print("Tu total es de", j)
