#Ejercicio 3
#Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par"
numero = int(input("Ingrese un número par: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#Ejercicio 4
#scribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece
edad= int (input ("Ingrese su edad:"))
if edad <12: 
    print ("Pertenece a la categoria niño/a")
elif edad >=12 and edad <=18:
    print ("Pertenece a la categoria adolescente")
elif edad >=18 and edad <30: 
        print ("Pertenece a la categoria adulto joven")
else: 
    print ("Pertenece a la categoria adulto")

#Ejercicio 5
# Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres"
password = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")
if len(password) >= 8 and len(password) <= 14:
    print("Ha ingresado una contraseña correcta")   
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio 6
import random
from statistics import mode, mean, median
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda=mode(numeros_aleatorios)
media=mean(numeros_aleatorios)
mediana=median(numeros_aleatorios)
print(f"Moda: {moda}, Media: {media}, Mediana: {mediana}")
if media > mediana > moda:
    print("Distribución sesgada a la derecha")
elif moda > mediana > media:
    print("Distribución sesgada a la izquierda")
else: print("Distribución sin sesgo ")    

#Ejercicio 7
#Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.   
frase = input("Ingrese una frase o palabra: ")
if frase[-1].lower() in 'aeiou':
    print(frase, "!")
else:
    print(frase)
#Ejercicio 8
#Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
nombre= input("Ingrese su nombre: ")
opcion= int (input ("Ingrese 1, 2 o 3: "))
if opcion == 1:
    print (nombre.upper())
elif opcion == 2:
    print (nombre.lower())
elif opcion == 3:
    print (nombre.title())

#Ejercicio 9
magnitud_terremoto= int (input ("Ingrese la magnitud del terremoto: "))
if magnitud_terremoto < 3:
    print ("El terremoto fue muy leve")
elif magnitud_terremoto >=3 and magnitud_terremoto <4: 
    print ("El terremoto fue leve")
elif magnitud_terremoto >=4 and magnitud_terremoto <5:
    print ("El terremoto fue moderado")
elif magnitud_terremoto >=5 and magnitud_terremoto <6: 
    print ("El terremoto fue fuerte")
elif magnitud_terremoto >=6 and magnitud_terremoto <7:
    print ("El terremoto fue muy fuerte")
else: print ("El terremoto fue extremo")  
#Ejercicio 10
hemisferio= input ("Ingrese el hemisferio en el que se encuentra (Norte/Sur): ")
mes= input ("Ingrese el mes actual: ")
dia= int (input ("Ingrese el día del mes: "))
if hemisferio.lower() == "norte":
    if (mes.lower() == "diciembre" and dia >= 21) or (mes.lower() in ["enero", "febrero"]) or (mes.lower() == "marzo" and dia <= 20):
        print("Es invierno")
    elif (mes.lower() == "marzo" and dia >= 21) or (mes.lower() in ["abril", "mayo"]) or (mes.lower() == "junio" and dia <= 20):
        print("Es primavera")
    elif (mes.lower() == "junio" and dia >= 21) or (mes.lower() in ["julio", "agosto"]) or (mes.lower() == "septiembre" and dia <= 20):
        print("Es verano")
    elif (mes.lower() == "septiembre" and dia >= 21) or (mes.lower() in ["octubre", "noviembre"]) or (mes.lower() == "diciembre" and dia <= 20):
        print("Es otoño")
    else:
        print("fecha no válida")
if hemisferio.lower() == "sur":
            if (mes.lower() == "junio" and dia >= 21) or (mes.lower() in ["julio", "agosto"]) or (mes.lower() == "septiembre" and dia < 20):
                print("Es invierno")
            elif (mes.lower() == "septiembre" and dia >= 21) or (mes.lower() in ["octubre", "noviembre"]) or (mes.lower() == "diciembre" and dia <=20):
                print("Es primavera")
            elif (mes.lower() == "diciembre" and dia >= 21) or (mes.lower() in ["enero", "febrero"]) or (mes.lower() == "marzo" and dia <= 20):
                print("Es verano")
            elif (mes.lower() == "marzo" and dia >= 21) or (mes.lower() in ["abril", "mayo"]) or (mes.lower() == "junio" and dia <= 20):
                print("Es otoño")
            else:
                print("fecha no válida"):
    

