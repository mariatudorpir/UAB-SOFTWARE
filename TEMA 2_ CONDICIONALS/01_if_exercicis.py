###
# EXERCICIS
###

# Exercici 1: Determinar el més gran de dos nombres
# Demana a l'usuari que introdueixi dos nombres i mostra un missatge
# que indiqui quin és més gran o si són iguals.

num1, num2 = map(float, input("introdueix dos nombres separats per una coma: ").split(","))
if num1<num2:
    print(f"{num2} es mes gran que {num1}")
elif num1>num2:
    print(f"{num1} es mes gran que {num2}")
else:
    print(f"{num1} es igual a {num2}")

# Exercici 2: Calculadora senzilla
# Demana a l'usuari dos nombres i una operació (+, -, *, /).
# Fes l'operació i mostra'n el resultat (gestiona la divisió per zero).

num1, num2 = float(input("Entra numero 1: ")), float(input("Entra numero 2: "))
operacion = input("Entra una operacion (+, -, *, /): ")
if operacion == "+":
    suma = num1 + num2
    print(f"El resultado es: {suma}")
elif operacion == "-":
    resta = num1 - num2
    print(f"El resultado es: {resta}")
elif operacion == "*":
    multi = num1 * num2
    print(f"El resultado es: {multi}")
else:
    div = num1 / num2
    print(f"El resultado es: {div}")

# Exercici 3: Any de traspàs
# Demana a l'usuari que introdueixi un any i determina si és de traspàs.
# Un any és de traspàs si és divisible per 4, excepte si és divisible per 100
# però no per 400.

anio = int(input("Entra un año para averiguar si es bisiesto: "))
if anio % 4 == 0:
    if anio % 100 == 0:
        if anio % 400 == 0:
            print(f"{anio} es año bisiesto.")
        else:
            print(f"{anio} no es bisiesto.")
    else:
        print(f"{anio} es año bisiesto.")
else:
    print(f"{anio} no es bisiesto.")

# Exercici 4: Classificar edats
# Demana a l'usuari que introdueixi una edat i classifica-la en:
# - Nadó (0-2 anys)
# - Infant (3-12 anys)
# - Adolescent (13-17 anys)
# - Adult (18-64 anys)
# - Persona gran (65 anys o més)

edad = int(input("Entra una edad: "))
if edad >= 0 and edad <= 2:
    print("Eres un bebé.")
elif edad >= 3 and edad <= 12:
    print("Eres un niño.")
elif edad >= 13 and edad <= 17:
    print("Eres un adolescente.")
elif edad >= 18 and edad <= 64:
    print("Eres un adulto.")
else:
    print("Eres un adulto mayor")

# Exercici 5: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble

num = float(input("Nivel de senyal rebut en dBm: ").strip())
if -50 <= num:
    print("Excel·lent")
elif -67 <= num:
    print("Bona")
elif -75 <=num:
    print("Feble")
else:
    print("Molt feble")

# Exercici 6: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.

potencia = float(input("Potència òptica rebuda en dBm: ").strip())
if -27 <= potencia <= -8:
    print("Acceptable")
elif potencia < -27:
    print("Massa baix")
else: 
    print("Massa alt")

# Exercici 7: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.

consum = float(input("Consum de dades en GB: ").strip())
if consum > 20:
    addicionals = consum - 20
    print(f"Has superat el limit de 20GB, havent consumit {addicionals} GBs addicionals.")
else:
    print("Estas dins del limit")

# Exercici 8: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.

ences = input("L'indicador del terminal òptic està encès? (y/n): ").strip()
router = input("L'indicador del router està encès? (y/n): ").strip()
if ences == "y":
    print("Cal revisar el cable de fibra.")
elif router != "y":
    print("Cal comprovar el servei del proveïdor.")
else:
    print("La connexió sembla funcionar correctament.")

# Exercici 9: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.

bateria = float(input("Percentatge bateria: ").strip())
if bateria < 0 or bateria > 100:
    print("Valor no valid")
elif bateria < 20:
    print("Crític")
elif bateria < 50:
    print("Baix")
else:
    print("Suficient")

# Exercici 10: Qualitat d'una connexió de xarxa
# Demana la latència en mil·lisegons i el percentatge de paquets perduts.
# Rebutja una latència negativa o una pèrdua fora del rang del 0 % al 100 %.
# Classifica la connexió com a excel·lent si la latència és de 30 ms o menys
# i la pèrdua és de l'1 % o menys; bona si és de 80 ms o menys i la pèrdua és
# del 3 % o menys; acceptable si és de 150 ms o menys i la pèrdua és del 5 %
# o menys; en qualsevol altre cas, deficient.

latencia, paquets = map(float, input("Introdueix la latència en mil·lisegons i el percentatge de paquets perduts, separats per una coma: ").split(","))
if latencia < 0 or 100 < paquets or paquets < 0:
    print("Valor de latencia o percentatge de paquets perduts NO valida; latencia no pot ser negativa i el percentatge de paquets perduts ha de estar entre el 0-100%")
elif latencia <= 30 and paquets <= 1:
    print("Connexió excel·lent")
elif latencia <= 80 and paquets <= 3:
    print("Connexió bona")
elif latencia <= 150 and paquets <= 5:
    print("Connexió acceptable")
else:
    print("Connexió deficient")

# Exercici 11: Cost mensual d'un pla de dades
# Demana el tipus de pla (bàsic o plus) i el consum mensual en GB.
# El pla bàsic costa 10 € i inclou 10 GB; cada GB addicional costa 1,50 €.
# El pla plus costa 20 € i inclou 30 GB; cada GB addicional costa 0,75 €.
# Rebutja un consum negatiu o un tipus de pla desconegut. Calcula i mostra el
# cost total, tenint en compte que no es cobra l'excés si no se supera el límit.

tipus_pla = input("Tipus de pla (bàsic o plus): ").strip()
consum_mensual = float(input("Consum mensual en GB: ").strip())
if consum_mensual < 0 or (tipus_pla != "bàsic" and tipus_pla != "plus"):
    print("Dades introduides invalides. Recorda que: \n")
    print("El consum no pot ser negatiu, i que només existeixen dos tipus de pla: bàsic i plus.")
elif tipus_pla == "bàsic":
    if consum_mensual > 10:
        print("Cost total: ", 10+(consum_mensual-10)*1.5)
    else: 
        print("Cost total: 10")
elif tipus_pla == "plus":
    if consum_mensual > 30:
        print("Cost total: ", 20+((consum_mensual-30)*0.75))
    else: 
        print("Cost total: 20")

# Exercici 12: Accés a un compte de client
# Demana si el compte està actiu, si la contrasenya és correcta i si el codi
# de doble verificació és correcte. Demana el codi només si el compte és actiu
# i la contrasenya és correcta. Indica si l'accés es denega perquè el compte
# està desactivat, perquè la contrasenya és incorrecta o perquè falla el codi;
# si totes les comprovacions necessàries són correctes, permet l'accés.

compte_actiu = input("El compte esta actiu? (y/n): ").strip()
contraseña = input("La contrasenya es correcta? (y/n): ").strip()

if compte_actiu != "y":
    print("Acces denegat. Compte desactivat.")
elif contraseña != "y":
    print("Acces denegat. Contrasenya incorrecta.")
else:
    verif = input("El codi de doble verificació es correcte? (y/n): ")
    if verif != "y":
        print("Acces denegat. Codi de doble verificacio incorrecte.")
    else:
        print("Acces permès!")

# Exercici 13: Diagnòstic d'un router
# Demana si el router està encès, si l'indicador LOS del terminal òptic està
# encès i si l'indicador d'Internet del router està encès. Indica primer si
# cal encendre el router; si ja està encès, comprova si cal revisar el cable
# de fibra (LOS encès), si cal contactar amb el proveïdor (Internet apagat) o
# si la connexió funciona correctament. Considera els casos en aquest ordre.

router_en = input("El router està encès? (y/n)").strip()

if router_en != "y":
    print("Cal encendre el router primer.")
else:
    indicador_ter = input("El indicador LOS del terimnal òptic està encès? (y/n)").strip()
    indicador_internet = input("El indicador d'Internet del router està encès? (y/n)").strip()  
    
    if indicador_ter != "y":
        print("Cal revisar el cable de fibra.")
    elif indicador_internet != "y":
        print("Cal contactar amb el poveïdor.")
    else:
        print("Connexió funciona correctament.")

# Exercici 14: Prioritat d'una incidència de xarxa
# Demana si la incidència afecta un servei crític, el nombre d'usuaris afectats
# i si hi ha una alternativa de connexió disponible. Rebutja un nombre negatiu
# d'usuaris. Assigna prioritat crítica si afecta un servei crític i no hi ha
# alternativa, o si afecta almenys 50 usuaris i no hi ha alternativa; alta si
# afecta almenys 10 usuaris o un servei crític; en qualsevol altre cas, baixa.

servei = input("La incidenca afecta un servei crític? (y/n)").strip()
afectats = int(input("Nombre d'usuaris afectats: ").strip())

if afectats < 0:
    print("Nombre d'usuaris no pot ser negatiu.")
else: 
    alternativa = input("Hi ha una alternativa de connexió disponible? (y/n)").strip()
    if (servei == "y" or afectats >= 50) and alternativa != "y":
        print("Prioritat crítica.")
    elif afectats >= 10 or servei == "y":
        print("Prioritat alta.")
    else:
        print("Prioritat baixa.")