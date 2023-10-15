#https://replit.com/join/ztcxxivzvx-danielgonzal232

print("Tienes una clase de 5 alumnos")
x = float(input("Califcacion de tu primer estudiante: " ))
y = float(input("Calificacion de tu segundo estudiante: "))
z = float(input("Calificacion de tu tercer estudiante: "))
v = float(input("Calificacion de tu cuarto alumno: "))
w = float(input("Calificacion de tu quinto alumno: "))

n = [x, y, z, v,w]
s = sum(n)
c = len(n)
p = s / c
print("Tu promedio es: ", p)

man = max(n)
min = min(n)
print("La nota más alta es:", man)
print("La nota más baja es:", min)

a = sum(n >= 60 for n in n)
r= c - a
print("Estudiantes que aprobaron:", a)
print("Estudiantes que reprobaron:", r)
