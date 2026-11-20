###
# EXERCICIS (diccionaris)
###

# Exercici 1: Crear un diccionari
# Crea un diccionari anomenat estudiant amb les claus "nom", "edat" i "assignatures"
# (aquesta última, una llista amb tres assignatures). Imprimeix-lo.

estudiant={
    "nom": "maria",
    "edat": 19,
    "assignatures": ["sistemas", "software", "xarxes"]
}
print(estudiant)

# Exercici 2: Accedir i modificar
# Imprimeix la segona assignatura de l'estudiant i canvia'n l'edat a un valor nou.

print(estudiant["assignatures"][1]) # 0, 1, 2, 3... RECORDAR
estudiant["edat"]="20"
print(estudiant["edat"])

# Exercici 3: Afegir i eliminar
# Afegeix la clau "grau" a l'estudiant i elimina després la clau "edat" amb del.

estudiant["grau"]="Enginyeria de Electrónica de Telecomunicació" # Corregit
del estudiant["edat"]
print(estudiant)

# Exercici 4: Comprovar claus
# Comprova amb in si existeixen les claus "nom" i "email" i imprimeix el resultat.

print("nom" in estudiant)
print("email" in estudiant)
# Ja es imprimeix True i False respectivament!

# Exercici 5: Recórrer un diccionari
# Recorre el diccionari amb un bucle for i items() i imprimeix cada parella com "clau: valor".

for clau, valor in estudiant.items():
    print(f"{clau}: {valor}")

# Exercici 6: Comptar paraules
# Donada la llista de paraules:
# paraules = ["sol", "lluna", "sol", "estrella", "lluna", "sol"]
# Crea un diccionari que indiqui quantes vegades apareix cada paraula.

paraules = ["sol", "lluna", "sol", "estrella", "lluna", "sol"]
recompte={} #el diccionari esa buit pperque encara no hem comptat res
for paraula in paraules: # Exemple: Primera PARAULA de la llista de PARAULES
    if paraula in recompte: # Comprova que la PARAULA estigui en el diccionari RECOMPTE (com que sol no esta, suma 1 per sol, pero quan ho fa per la tercera paraula, veu que ja existeix en el diccionari per tant li suma 1 al valor de la clau corresponent)
        recompte[paraula]+=1 # Si hi és, suma 1 al valor de la clau corresponent
    else:
        recompte[paraula]=1 #Si no hi és, crea la clau amb valor 1
print(recompte)

# Obtindriem una cosa com: {'sol':3, 'lluna':2, 'estrella':1}
# El sol apareix 3 cops en la llista, la lluna 2 cops i l'estrella 1 cop.
