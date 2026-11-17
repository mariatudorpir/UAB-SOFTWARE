###
# exercicis-basics.py
# Exercicis per practicar els conceptes apresos a les lliçons.
###

print("\nExercici 1: Imprimir missatges")
print("Escriu un programa que imprimeixi el teu nom i la teva ciutat en línies separades.")

############################ Completa aquí ############################

print("Maria", end='\n')
print("Barcelona")

print("\nExercici 2: Mostra els tipus de dades de les variables següents:")
print("Utilitza la comanda 'type()' per determinar el tipus de dades de cada variable.")
a = 15
b = 3.14159
c = "Hola món"
d = True
e = None

############################ Completa aquí ############################

print(type(a), type(b), type(c), type(d), type(e))

print("Solucion:\n")
print("Tipo de a:", type(a))
print("Tipo de b:", type(b))
print("Tipo de c:", type(c))
print("Tipo de d:", type(d))
print("Tipo de e:", type(e))

print("\nExercici 3: Conversió de tipus")
print("Converteix la cadena \"12345\" a un enter i després a un float.")
print("Converteix el float 3.99 a un enter. Què passa?")

############################ Completa aquí ############################

print(int("12345"))
print(float("12345"))
print(int(3.99)) # SE ELIMINA EL DECIMAL

print("\nExercici 4: Variables")
print("Crea variables per al teu nom, edat i alçada.")
print("Utilitza f-strings per imprimir una presentació.")

# "Hola! Em dic Marc, tinc 40 anys i faig 1.75 metres"
#name = "Marc"
#age = 40

############################ Completa aquí ############################

nombre = "Maria"
edad = "19"
altura= "1.69"
print(f"Hola! Me llamo {nombre} y tengo {edad} años, mido {altura} metros.")

print("\nExercici 5: Nombres")
print("1. Crea una variable amb el nombre PI (sense assignar una variable)")
print("2. Arrodoneix el nombre amb round()")
print("3. Fes la divisió entera entre el nombre resultant i el nombre 2")
print("4. El resultat hauria de ser 1")

############################ Completa aquí ############################

print(round(3.14))
print(round(3.14)/2)

print("\nExercici 6: Conversor de temperatura")
print("Demana a l'usuari una temperatura en graus Celsius.")
print("Converteix aquest valor a Fahrenheit amb la fórmula: F = (C * 9/5) + 32")
print("Mostra els dos valors amb un missatge clar.")

############################ Completa aquí ############################

celcius = float(input("Introduce una temperatura en grados Celsius: \n")) #todo de una y pq se puede introducir un numero con decimales
faren = (celcius*9/5)+32
print(f"La temperatura en celcius introducida es: {celcius} i en Fahrenheit: {faren:.2f}")
#se aclara que es un float la variable con 2 decimales.


print("\nExercici 7: Calculadora de propina")
print("Demana el total d'un compte i el percentatge de propina.")
print("Calcula quant és la propina i el total final que s'ha de pagar.")
print("Mostra els resultats amb 2 decimals.")

############################ Completa aquí ############################

total_cuenta=float(input("Introduce total cuenta: "))
porcentaje_propina=float(input("Introduce el porcentaje de propina: "))

propina=total_cuenta*(porcentaje_propina/100)
total_final=total_cuenta+propina

print(f"La propina sera {propina:.2f} euros, siendo en total a pagar: {total_final:.2f} euros")

print("\nExercici 8: Validador de contrasenya simple")
print("Demana una contrasenya a l'usuari.")
print("Comprova si té almenys 8 caràcters.")
print("Mostra 'Contrasenya vàlida' o 'Contrasenya no vàlida'.")

############################ Completa aquí ############################

contra=input("Introduce tu contraseña:")
if len(contra) >= 8:
    print("Valida")
else:
    print("Invalida")