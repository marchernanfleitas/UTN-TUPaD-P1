#Ejercicio 1
print ("Hola Mundo!")

#Ejercicio 2
nombre=input("Ingrese su nombre")
print ("Hola ", nombre, "!" )

#Ejercicio 3
nombre=input("Ingrese su nombre")
apellido=input("Ingrese su apellido")
edad= int (input("Ingrese su edad"))
residencia=input("Ingrese su lugar de residencia")

print ( "Soy", nombre, apellido, ", tengo ", edad ,"años y vivo en ", residencia )

#Ejercicio 4
radio=float(input("Ingrese el radio de un circulo"))
import math
pi = math.pi
area=pi*radio**2
circunferencia=2*pi*radio
print("El área del circulo es", area , "y el perimetro de la circunferencia es ", circunferencia )

#Ejercicio 5
segundos=float(input("Ingrese una cantidad de segundos"))
horas=segundos/3600
print("Equivale a", horas, "horas")

#Ejercicio 6
nro=int(input("Ingrese un número para conocer su tabla de multiplicar"))
print(nro*1)
print(nro*2)
print(nro*3)
print(nro*4)
print(nro*5)
print(nro*6)
print(nro*7)
print(nro*8)
print(nro*9)

#Ejercicio 7
nroentero=int(input("Ingrese un número entero distinto de 0"))
nroentero2=int(input("Ingrese otro número entero distinto de 0"))
print("La suma de ambos es ", nroentero+nroentero2, ", la resta del primero menos el segundo es", nroentero-nroentero2 , ", la multiplicación del primero por el segundo es ", nroentero*nroentero2 , ", la división entre ambos es ", nroentero/nroentero2)

#Ejercicio 8
peso=float(input("Ingrese su peso en kilogramos"))
talla=float(input("Ingrese su altura en metros"))
print("Su IMC es", peso/(talla**2) , "kg/m2")

#Ejercicio 9
temperatura=float(input("Ingrese una temperatura en Celsius"))
from fractions import Fraction
print("El equivalente en grados Fahrenheit es ",  Fraction(9,5)*temperatura+32)

#Ejercicio 10
n1=float(input("Ingrese un número"))
n2=float(input("Ingrese un número"))
n3=float(input("Ingrese un número"))
print("El promedio de los números ingresados es", (n1+n2+n3)/3)