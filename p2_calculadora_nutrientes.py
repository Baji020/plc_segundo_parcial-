#https://replit.com/join/ufrkwriiua-danielgonzal232

ingredientes = {}
while True:
    ni = input("Dame el nombre del ingrediente: ")
    
    c = float(input("Dame cantidad de calorías por cada 100g: "))
    p = float(input("Cantidad de proteína por cada 100g: "))
    g = float(input("Cantidad de grasa por cada 100g: "))
    ch = float(input("Cantidad de carbohidratos por cada 100g: "))

    ingredientes[ni] = {
        'calorias': c,
        'proteinas': p,
        'grasas': g,
        'carbohidratos': ch
    }

receta = {}
while True:
    ni = input("Ingrese el nombre del ingrediente en la receta: ")
    
    ca = float(input(f"Cantidad de {ni} en gramos: "))
    receta[ni] = ca

tc = sum(ingredientes[ingrediente]['calorias'] * (ca / 100) for ingrediente, ca in receta.items())
tp = sum(ingredientes[ingrediente]['proteinas'] * (ca / 100) for ingrediente, ca in receta.items())
tg = sum(ingredientes[ingrediente]['grasas'] * (ca / 100) for ingrediente, ca in receta.items())
tch = sum(ingredientes[ingrediente]['carbohidratos'] * (ca / 100) for ingrediente, ca in receta.items())

print("Nutrientes totales en la receta:")
print(f"Calorías: {tc} kcal")
print(f"Proteínas: {tp} gramos")
print(f"Grasas: {tg} gramos")
print(f"Carbohidratos: {tch} gramos")


    
