#Reto parcial 2
#https://replit.com/join/fwnmtkivsn-danielgonzal232

print("En tu clase tienes 6 alumnos, dime quienes aprobaron")

x = float(input("¿Cuál es la calificación del primer alumno? "))
y = float(input("¿Cuál es la calificación del segundo alumno? "))
z = float(input("¿Cuál es la calificación del tercer alumno? "))
v = float(input("¿Cuál es la calificación del cuarto alumno? "))
r = float(input("¿Cuál es la calificación del quinto alumno? "))
l = float(input("¿Cuál es la calificación del sexto alumno? "))

xa = int(input("¿Cuántas asignaciones completó el primer alumno de 0 a 10? "))
ya = int(input("¿Cuántas asignaciones completó el segundo alumno de 0 a 10? "))
za = int(input("¿Cuántas asignaciones completó el tercer alumno de 0 a 10? "))
va = int(input("¿Cuántas asignaciones completó el cuarto alumno de 0 a 10? "))
ra = int(input("¿Cuántas asignaciones completó el quinto alumno de 0 a 10? "))
la = int(input("¿Cuántas asignaciones completó el sexto alumno de 0 a 10? "))

xp = input("¿El primer alumno participó (si o no)? ").lower()
yp = input("¿El segundo alumno participó (si o no)? ").lower()
zp = input("¿El tercer alumno participó (si o no)? ").lower()
vp = input("¿El cuarto alumno participó (si o no)? ").lower()
rp = input("¿El quinto alumno participó (si o no)? ").lower()
lp = input("¿El sexto alumno participó (si o no)? ").lower()

if x > 70 and xa >= 5 and xp == "si":
    print("El primer estudiante aprobó")
else:
    print("El primer estudiante reprobó")

if y > 70 and ya >= 5 and yp == "si":
    print("El segundo estudiante aprobó")
else:
    print("El segundo estudiante reprobó")

if z > 70 and za >= 5 and zp == "si":
    print("El tercer estudiante aprobó")
else:
    print("El tercer estudiante reprobó")

if v > 70 and va >= 5 and vp == "si":
    print("El cuarto estudiante aprobó")
else:
    print("El cuarto estudiante reprobó")

if r > 70 and ra >= 5 and rp == "si":
    print("El quinto estudiante aprobó")
else:
    print("El quinto estudiante reprobó")

if l > 70 and la >= 5 and lp == "si":
    print("El sexto estudiante aprobó")
else:
    print("El sexto estudiante reprobó")
