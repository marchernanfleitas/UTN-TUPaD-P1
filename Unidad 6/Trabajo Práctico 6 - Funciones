#Trabajo Práctico 5 - Funciones

#Ejercicio 1

def imprimir_hola_mundo ():
    print ("Hola Mundo!")

imprimir_hola_mundo()

#Ejercicio 2

def saludar_usuario(nombre):
    return  (f"Hola, {nombre} !")
ingreso_nombre= input ("Ingrese su nombre")
saludo= saludar_usuario(ingreso_nombre )
print (saludo)

#Ejercicio 3

def informacion_personal(nombre, apellido, edad, residencia):
    print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre_ingresado= input ("Ingrese su nombre")
apellido_ingresado= input ("Ingrese su apellido")

while True:
    edad_ingresada= input ("Ingrese su edad")
    if edad_ingresada.isdigit():
        edad= int(edad_ingresada)
        break
    else:
        print ("Debe ingresar su edad en números enteros")
        
residencia_ingresada= input ("Ingrese su Ciudad de residencia")
informacion_personal(nombre_ingresado, apellido_ingresado, edad_ingresada, residencia_ingresada)

#Ejercicio 4

import math
def calcular_area_circulo(radio):
    return  math.pi * radio**2

def calcular_perimetro_circulo(radio):
    return  2 * math.pi * radio

radio= float (input ("Ingrese el radio del circulo") )

area=calcular_area_circulo(radio)
perimetro= calcular_perimetro_circulo(radio)

print ("El area del circulo es : ", round (area,2))
print (" El perimetro del circulo es ", round (perimetro,2))

#Ejercicio 5

def segundos_a_horas (segundos):
    return segundos / 3600

while True:
    segundos=( input ("Ingrese la cantidad de segundos que desea convertir a horas") )
    if segundos.isdigit():
        segundos= int(segundos)
        break
    else:
        print ("Debe ingresar segundos en números enteros")
horas= segundos_a_horas(segundos)
print (f" {segundos} segundos equivale a {horas:.2f} horas")

#Ejercicio 6 

def tabla_multiplicar(numero):
    for n in range (1,11):
        nro=numero * n
        print (nro)

numero= (float (input ("Ingrese un número para conocer su tabla de multiplicar del 1 al 10"))  )       
tabla_multiplicar(numero)

#Ejercicio 7

a=int ( input( "Ingrese un número entero distinto de 0") )
b=int ( input( "Ingrese otro número entero distinto de 0") )
def operaciones_basicas(a,b):
    suma=a+b
    resta=a-b
    multiplicacion=a*b
    division=a/b
    return (suma, resta, multiplicacion, division)

resultados= operaciones_basicas(a,b)
print (f"La suma de ambos es", resultados [0] )
print (f"la resta del primero menos el segundo es", resultados [1] )  
print (f"la multiplicación del primero por el segundo es", resultados [2] )
print (f"la división entre ambos es ", resultados [3] )

#Ejercicio 8

peso= float (input("Ingrese su peso") )
while True:
  altura= float (input("Ingrese su altura en metros") )
  if altura > 0:
    print("Altura debe ser mayor que 0")
    break

def calcular_imc(peso, altura):
    return peso/(altura **2)

IMC=calcular_imc(peso, altura)
print (f"Su IMC es {IMC:.2f} kg/m2")

#Ejercicio 9

celsius=float(input("Ingrese una temperatura en Celsius"))

def celsius_a_fahrenheit(celsius):
    return 9/5*celsius+32
    
grados=celsius_a_fahrenheit(celsius)
print(f" {celsius} grados Celsius equivalen a {grados} grados Fahrenheit")

#Ejercicio 10

a=float(input("Ingrese un número"))
b=float(input("Ingrese un número"))
c=float(input("Ingrese un número"))
def calcular_promedio (a,b,c):
    return (a+b+c)/3

promedio=calcular_promedio(a,b,c)
print (promedio)
    
