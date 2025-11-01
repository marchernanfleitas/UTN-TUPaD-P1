#Ejercicio 1

def factorial(n):
    if n == 0
        return 1
    else:
        return n * factorial(n - 1)
num = int(input("Ingrese un número entero positivo: "))
for i in range(1, num + 1):
    print(f"El factorial de {i} es {factorial(i)}")

#Ejercicio 2

def fibonacci (n):
    if n <=0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
pos_fibonacci = int(input("Ingrese la posición hasta donde desea ver la serie de Fibonacci: "))
for i in range(pos_fibonacci):
    print(f"Fibonacci en la posición {i} es {fibonacci(i)}")

#Ejercicio 3

def potencia (base, exponente):
    #caso base
    if exponente == 0:
        return 1
    # Llamada recursiva
    else:
        return base * potencia (base, exponente - 1)
while True:
    base = float (input("Ingrese el número base: "))
    base= int(base)
    if base < 0:
        print("La base debe ser un número real positivo. Intente nuevamente.")
        continue
    else:
        break

while True:
    exponente = float (input("Ingrese el exponente (entero positivo): "))
    exponente= int(exponente)
    if exponente < 0:
        print("El exponente debe ser un entero positivo. Intente nuevamente.")
        continue
    else:
        break
print(f"{base} elevado a la {exponente} es {potencia(base, exponente)}")

#Ejercicio 4

def decimal_a_binario(n):
    #uso los casos base 0 y 1 para cortar la recursión
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    #guardo los retornos de la función recursiva para concatenar(+) los resultados con el resto de la división. 
    return decimal_a_binario(n // 2) + str(n % 2)
while True:
        input_numero = int(input("Ingrese un número entero positivo en base decimal: "))
        if input_numero < 0:
            print("Error, debe ingresar un número entero positivo.")
        else:
            n = input_numero
            break
binario = decimal_a_binario(n)
print(f"La representación en binario de {n} es: {binario}")

#Ejercicio 5

def es_palindromo(palabra):
# Caso base: si la palabra tiene 0 o 1 letra, es un palindromo
    if len(palabra) <= 1:
        return True
    # Comparo la primera y la última letra
    if palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    else:
        return False
palabra = input("Ingrese una palabra para saber si es un palíndromo: ").strip ().lower()
if es_palindromo(palabra):
    print(f"La palabra '{palabra}' es un palíndromo.")
else:
    print(f"La palabra '{palabra}' no es un palíndromo.")

#Ejercicio 6

def suma_digitos(n):
    #si el nro es menor a 10 la suma es el mismo número
    if n < 10:
        return n
    else:
        #suma el último dígito (n % 10) y llama recursivamente a la función con el número sin el último dígito (n // 10) concatenando los resultados
        return n % 10 + suma_digitos(n // 10)
numero_entero_positivo = int(input("Ingrese un número entero positivo: "))
print(f"La suma de los dígitos de {numero_entero_positivo} es {suma_digitos(numero_entero_positivo)}")

#Ejercicio 7

def contar_bloques(n):
    #caso base primario
    if n == 0:
        return 0
    #caso base de corte
    if n == 1:
        return 1
    else:
        #recursivamente cuento el número de bloques en el nivel actual (n*n) y llamo a la función con el siguiente nivel (n-1)
        return n * n + contar_bloques(n - 1)
fila_nivel_inferior = int (input ("Ingrese la cantidad de bloques en el nivel más bajo de la pirámide: "))
print(f"El total de bloques necesarios para construir la pirámide es: {contar_bloques(fila_nivel_inferior)}")

#Ejercicio 8

def contar_digito(numero, digito):
    # Caso base 
    if numero == 0:
        return 0
    else:
        # Verifico si el último dígito del número es igual al dígito buscado
        if numero % 10 == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)
#Valido las entradas del usuario
while True:
    num_entero_str = input("Ingrese un número entero positivo : ")
    if num_entero_str.isdigit() and int(num_entero_str) >= 0:
        numero = int(num_entero_str)
        break
    else:
        print("Error. Ingrese un número entero positivo válido.")
while True:
    digito_str = input("Ingrese un dígito entre 0 y 9 : ")
    if digito_str.isdigit() and len(digito_str) == 1 and 0 <= int(digito_str) <= 9:
        digito = int(digito_str)
        break
    else:
        print("Error. Ingrese un dígito simple entre 0 y 9.")
# Llamo a la función y muestro el resultado
cantidad = contar_digito(numero, digito)
print(f"El dígito {digito} aparece {cantidad} veces en el número {numero}.")
