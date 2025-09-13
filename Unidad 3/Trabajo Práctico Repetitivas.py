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