#https://replit.com/join/kejxbcxuvr-danielgonzal232

x = input("¿Qué quieres ser? (a) Elfo, (b) Demonio, (c) Arcángel, (d) Hada, (f) Vampiro o (g) Gigante: ")
rd = random.randint(1, 8)

if x == "a" or x == "A":
    print("Eres un elfo")
    y = input("Estás en una cueva con un gigante, tienes que matarlo. ¿Qué arma quieres? (espada o arco): ")
    if y == "espada":
        print("Necesitas obtener un resultado mayor que 5 para ganar")
        if rd > 5:
            print("Ganaste")
        else:
            print("Perdiste")
    elif y == "arco":
        print("Necesitas obtener un resultado mayor que 6 para ganar")
        if rd > 6:
            print("Ganaste")
        else:
            print("Perdiste")

elif x == "b" or x == "B":
    print("Eres un demonio")
    y = input("Estás peleando contra un arcángel. ¿Qué arma quieres? (poder oscuro o guadaña): ")
    if y == "poder oscuro":
        print("Necesitas obtener un resultado mayor que 5 para ganar")
        if rd > 5:
            print("Ganaste")
        else:
            print("Perdiste")
    elif y == "guadaña":
        print("Necesitas obtener un resultado mayor que 4 para ganar")
        if rd > 4:
            print("Ganaste")
        else:
            print("Perdiste")

elif x == "c" or x == "C":
    print("Eres un arcángel")
    y = input("Estás en una cueva peleando contra un demonio, tienes que matarlo. ¿Qué arma quieres? (a) Gracia del sol o (b) Gracia del mar: ")
    if y == "a":
        print("Necesitas obtener un resultado mayor que 3 para ganar")
        if rd > 3:
            print("Ganaste")
        else:
            print("Perdiste")
    elif y == "b":
        print("Necesitas obtener un resultado mayor que 6 para ganar")
        if rd > 6:
            print("Ganaste")
        else:
            print("Perdiste")

elif x == "d" or x == "D":
    print("Eres un hada")
    y = input("Estás en el bosque del rey hada peleando contra un vampiro. Tienes que ganar para que no destruya el bosque. ¿Qué arma quieres? (a) Lanza divina o (b) Espada divina: ")
    if y == "a":
        print("Necesitas obtener un resultado mayor que 4 para ganar")
        if rd > 4:
            print("Ganaste")
        else:
            print("Perdiste")
    elif y == "b":
        print("Necesitas obtener un resultado mayor que 5 para ganar")
        if rd > 5:
            print("Ganaste")
        else:
            print("Perdiste")

elif x == "f" or x == "F":
    print("Eres un vampiro")
    y = input("Estás peleando contra una hada mala que quiere destruirlo todo. Debes detenerla. ¿Qué arma quieres? (a) Técnica de sangre o (b) Puño limpio: ")
    if y == "a":
        print("Necesitas obtener un resultado mayor que 5 para ganar")
        if rd > 5:
            print("Ganaste")
        else:
            print("Perdiste")
    elif y == "b":
        print("Necesitas obtener un resultado mayor que 7 para ganar")
        if rd > 7:
            print("Ganaste")
        else:
            print("Perdiste")

elif x == "g" or x == "G":
    print("Eres un gigante")
    y = input("Estás peleando contra un elfo en una pelea sin sentido. ¿Qué arma quieres? (a) Martillo o (b) Control de la tierra: ")
    if y == "a":
        print("Necesitas obtener un resultado mayor que 3 para ganar")
        if rd > 3:
            print("Ganaste")
        else:
            print("Perdiste")
    elif y == "b":
        print("Necesitas obtener un resultado mayor que 6 para ganar")
        if rd > 6:
            print("Ganaste")
        else:
            print("Perdiste")
else:
    print("Personaje no válido. Elige uno de los personajes mencionados.")
