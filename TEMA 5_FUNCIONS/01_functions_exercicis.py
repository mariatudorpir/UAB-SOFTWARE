###
# EXERCICIS (funcions)
###

# Exercici 1: Funció de salutació
# Crea una funció saludar_a(nom, salutacio="Hola") que imprimeixi la salutació seguida del nom.
# Prova-la amb i sense el segon argument.

def saludar_a(nom, salutacio="Hola"):
    print(f"{salutacio}, {nom}!")

saludar_a("Maria")  # Prova amb el segon argument per defecte
saludar_a("Irina", "Bon dia")  # Prova amb un segon argument

# Exercici 2: Parell o senar
# Crea una funció es_parell(numero) que retorni True si el número és parell i False si no ho és.

def es_parell(numero):
    return numero % 2 == 0

print(es_parell(4))  # Prova amb un número parell
print(es_parell(7))  # Prova amb un número senar

# Exercici 3: Mitjana d'una llista
# Crea una funció mitjana(numeros) que rebi una llista de números i en retorni la mitjana.
# Fes servir un bucle for.

def mitjana(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma / len(numeros) if numeros else 0

print(mitjana([1, 2, 3, 4, 5]))  # Prova amb una llista de números

# Exercici 4: Suma amb *args
# Crea una funció sumar_tot(*args) que retorni la suma de tots els números rebuts.
# Prova-la amb 2, 5 i 10 arguments.

def sumar_tot(*args):
    suma=0
    for numero in args:
        suma += numero
    return suma

print(sumar_tot(1, 2))
print(sumar_tot(1, 2, 3, 4, 5))
print(sumar_tot(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# Exercici 5: Taula de multiplicar
# Crea una funció taula_multiplicar(numero, limit=10) que imprimeixi la taula de multiplicar
# del número fins al límit indicat, fent servir range().

def taula_multiplicar(numero, limit=10):
    for i in range(1, limit + 1):
        print(f"{numero} x {i} = {numero * i}")

taula_multiplicar(5)  # Prova amb el límit per defecte
taula_multiplicar(3, 5)  # Prova amb un límit específic

# Exercici 6: Informació amb **kwargs
# Crea una funció mostrar_perfil(**kwargs) que imprimeixi cada parella clau: valor.
# Crida-la amb les dades d'un estudiant (nom, edat, grau).

def mostrar_perfil(**kwargs):
    for clau, valor in kwargs.items():
        print(f"{clau}: {valor}")

mostrar_perfil(nom="Maria", edat=19, grau="Enginyeria")

# Exercici 7: Reconvertir exercicis anteriors
# Torna a l'exercici del factorial (while) i del màxim d'una llista (for)
# i converteix-los en funcions que retornin el resultat.

################################ CAL REPASAR AQUEST EXERCICI, NO ESTIC SEGURA

def factorial(n):
    if n<0:
        return None  # Factorial no està definit per a nombres negatius
    resultat = 1
    while n>1:
        resultat*=n
        n-=1
    return resultat

def maxim(numeros):
    if not numeros:
        return None  # Retorna None si la llista està buida
    max_valor=numeros[0]
    for numero in numeros:
        if numero>max_valor:
            max_valor=numero
    return max_valor

# Exercici 8: Comptar vocals
# Crea una funció comptar_vocals(text) que rebi una cadena de text i retorni quantes vocals
# (a, e, i, o, u) conté. Ha de funcionar tant amb majúscules com amb minúscules.

def comptar_vocals(text):
    vocals="aeiouAEIOU"
    comptador=0
    for lletra in text:
        if lletra in vocals:
            comptador+=1
    return comptador

# Exercici 9: Retorn múltiple (mínim i màxim)
# Crea una funció minim_i_maxim(numeros) que rebi una llista de números i retorni tant el valor
# mínim com el valor màxim alhora. Desempaqueta el resultat en dues variables.

def minim_i_maxim(numeros):
    if not numeros:
        return None, None
    min_valor=numeros[0]
    max_valor=numeros[0]
    for numero in numeros:
        if numero<min_valor:
            min_valor=numero
        if numero>max_valor:
            max_valor=numero
    return min_valor, max_valor

# Exercici 10: Palíndrom
# Crea una funció es_palindrom(text) que retorni True si una paraula es llegeix igual d'esquerra a dreta
# que de dreta a esquerra (ignorant majúscules i minúscules), i False en cas contrari.

def es_palindrom(text):
    text=text.lower()
    return text==text[::-1]

print(es_palindrom("Maria"))
print(es_palindrom("Adeu"))