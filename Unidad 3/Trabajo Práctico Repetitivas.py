#Ejercicio 1
for num in range (0, 101):
    print(num)  
#Ejercicio 2
num=int(input("Ingrese un número entero"))
contadordigito= len(str(num))
print("El número tiene", contadordigito, "dígitos")
#Ejercicio 3
num1=int(input("Ingrese un número entero"))
num2=int(input("Ingrese otro número entero"))
mayor= max(num1,num2)
menor= min(num1,num2)
suma=0
for i in range (mayor-menor+1):
    suma+=i
print("La suma de los números comprendidos entre", menor, "y", mayor, "es", suma)
#Ejercicio 4
num_suma=0
while True:
    num=int(input ("Ingrese un número entero"))
    num_suma+=num
    if num==0:
        break
print("La suma total es", num_suma)
#Ejercicio 5
intentos=0
import random
num_aleatorio= random.randint(0,9)    
while True:
    num_ingresado=int(input("Ingrese un número entre 0 y 9"))
    intentos+=1
    if num_ingresado==num_aleatorio:
        break   
print("¡Felicidades! Adivinaste el número en", intentos, "intentos")
#Ejercicio 6
for numero in range (100, -1, -1):
    if numero % 2 == 0:
        print(numero)
#Ejercicio 7
num_positivo = int(input("Ingrese un número entero positivo: "))
while num_positivo <= 0:
    num_positivo = int(input("Por favor, ingrese un número entero positivo: "))
suma = 0
for i in range(num_positivo + 1):
    suma += i
print("La suma de los números comprendidos entre 0 y", num_positivo, "es", suma)
#Ejercicio 8
num_entero= int(input("Ingrese un número entero"))
iterador=0
contador_positivos=0
contador_negativos=0
contador_pares=0
contador_impares=0
for iterador in range (99):
     iterador+=1
     num_entero=int(input ("Ingrese un número entero"))
     if num_entero<0:
      contador_negativos=contador_negativos+1
     else:contador_positivos=contador_positivos+1
     if num_entero % 2 == 0:
      contador_pares=contador_pares+1
     else:
      contador_impares=contador_impares+1
print(f"El total de números positivos es",contador_positivos, "el total de números negativos es",contador_negativos, "el total de números pares es",contador_pares, "el total de números impares es",contador_impares)
#Ejercicio 9
#Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media
import statistics
num_int=int(input ("Ingrese un número entero"))
lista_numeros=[num_int]
for i in range (99):
    i+=1
    num_int=int(input ("Ingrese un número entero"))
    lista_numeros.append(num_int)
print("La media de los números ingresados es", statistics.mean(lista_numeros))
#Ejercicio 10
#Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
num_dig=int(input("Ingrese un número entero"))
for digito in str(num_dig)[::-1]:
    print(digito, end="")
