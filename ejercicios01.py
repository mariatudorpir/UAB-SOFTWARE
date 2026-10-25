###
# ejercicios.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí

print("Maria", end='\n')
print("Barcelona")

print("Solucion:\n")
nombre = "Pedro"  # Reemplázalo con tu nombre
ciudad = "Madrid"  # Reemplázalo con tu ciudad

print(nombre)
print(ciudad)

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí

print(type(a), type(b), type(c), type(d), type(e))

print("Solucion:\n")
print("Tipo de a:", type(a))
print("Tipo de b:", type(b))
print("Tipo de c:", type(c))
print("Tipo de d:", type(d))
print("Tipo de e:", type(e))

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí

print(int("12345"))
print(float("12345"))
print(int(3.99)) # SE ELIMINA EL DECIMAL

print("Solucion:\n")
cadena = "12345"
numero_entero = int(cadena)  # Convertir cadena a entero
numero_float = float(numero_entero)  # Convertir entero a float

print("Número entero:", numero_entero)
print("Número como float:", numero_float)

float_num = 3.99
entero_convertido = int(float_num)  # Se trunca el decimal

print("Float original:", float_num)
print("Float convertido a entero (se trunca la parte decimal):", entero_convertido)

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo Marc y tengo 38 años, mido 1.75 metros"
#name = "Marc"
#age = 38

### Completa aquí

nombre = "Maria"
edad = "19"
altura= "1.69"
print(f"Hola! Me llamo {nombre} y tengo {edad} años, mido {altura} metros.")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

### Completa aquí

print(round(3.14))
print(round(3.14)/2)

print("Solucion:\n")
resultado = int(round(3.1416) / 2) #lo haces todo de una
print("Valor de PI (aproximado):", 3.1416)
print("PI redondeado:", round(3.1416))
print("División entera de PI redondeado entre 2:", resultado)

print("\nEjercicio 6: Conversor de temperatura")
print("Pide al usuario una temperatura en grados Celsius.")
print("Convierte ese valor a Fahrenheit con la fórmula: F = (C * 9/5) + 32")
print("Muestra ambos valores con un mensaje claro.")

### Completa aquí

celcius = float(input("Introduce una temperatura en grados Celsius: \n")) #todo de una y pq se puede introducir un numero con decimales
faren = (celcius*9/5)+32
print(f"La temperatura en celcius introducida es: {celcius} i en Fahrenheit: {faren:.2f}")
#se aclara que es un float la variable con 2 decimales.

print("\nEjercicio 7: Calculadora de propina")
print("Pide el total de una cuenta y el porcentaje de propina.")
print("Calcula cuánto es la propina y el total final a pagar.")
print("Muestra los resultados con 2 decimales.")

### Completa aquí

total_cuenta=float(input("Introduce total cuenta: "))
porcentaje_propina=float(input("Introduce el porcentaje de propina: "))

propina=total_cuenta*(porcentaje_propina/100)
total_final=total_cuenta+propina

print(f"La propina sera {propina:.2f} euros, siendo en total a pagar: {total_final:.2f} euros")


print("\nEjercicio 8: Validador de contraseña simple")
print("Pide una contraseña al usuario.")
print("Comprueba si tiene al menos 8 caracteres.")
print("Muestra 'Contraseña válida' o 'Contraseña no válida'.")

### Completa aquí

contra=input("Introduce tu contraseña:")
if len(contra) >= 8:
    print("Valida")
else:
    print("Invalida")