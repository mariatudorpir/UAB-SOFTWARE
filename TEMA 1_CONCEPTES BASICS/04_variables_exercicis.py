###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.

nom = "Maria"
ubi = "UAB"
ports = 3
ences = True

print(f"L'encaminador {nom} esta ubicat a {ubi}, te {ports} ports; engegat: {ences}")

# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.

gb_inclosos = 400
gb_consumits = 200

print(f"Dades resultats:", gb_inclosos-gb_consumits)

gb_consumits = 350
print(f"Dades restants despres de l'actualització:", gb_inclosos-gb_consumits)
