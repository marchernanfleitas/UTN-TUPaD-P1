#Ejercicio 1
import statistics   
mean= statistics.mean
notas= [5 , 6 , 7 , 8, 5, 9 , 8, 5, 2 , 6 ] 
nombres = [ "Sandra", "Ruperto" , "Jacinto" , "Dario" , "Beatriz", "Corina", "Beto" , "Fernando" , "Pablo", "Juana" ]
mean= mean(notas)
val_min= min(notas)
val_max= max (notas)
for n in notas:
    print (("Alumno"),(nombres[notas.index(n)]) )
    print (("Nota"),(n) )
print (("La nota promedio es"), (mean) )
print (("La nota mínima de los alumnos es "), (val_min) )
print (("La nota máxima de los alumnos es "), (val_max) )

#Ejercicio 2
lista_producto = []
for i in range (5):
 producto = (  input ("Ingrese un producto que desea comprar " ) )
 lista_producto.append(producto)
print (sorted(lista_producto))
producto_eliminado= ( input ("Ingrese el producto que desea eliminar "))
lista_producto.remove (producto_eliminado)
print (("La lista final de compra es :"), (lista_producto)) 

#Ejercicio 3
import random
list_num= []
pares= []
impares= [] 
list_num= [(random.randint(1,100)) for i in range (15)]
for n in list_num:
    if n % 2 == 0:
        pares.append(n)
    else:
        (impares.append)(impares)
print (list_num)
print ( ( "La cantidad de nros pares es :"), (len(pares) ) )
print ( ( "La cantidad de nros impares es :"), (len(impares)) )

#Ejercicio 4
list=[1,3, 5, 3, 7, 1, 9 , 5, 3]
duplicado= []
for n in list:
    if n not in duplicado:
       duplicado.append(n)
print (duplicado)

#Ejercicio 5 
nom_asistencia = ["Jorge", "Nadia", "Mariana", "Monica", "Sofia", "Alvaro", "Matias", "Jorgelina"]
asistencia = []
for i in range(8):
    estado = input(f"Ingrese si el alumno {nom_asistencia[i]} estuvo en clase: ").strip().lower()
    if estado == "presente" or estado == "si":
        asistencia.append(nom_asistencia[i])
retiro = input("Ingrese el nombre del alumno que se retiró (o escriba 'ninguno'): ").strip()
if retiro.lower() != "ninguno":
    if retiro in asistencia:
        asistencia.remove(retiro)
    else:
        print(f" El alumno {retiro} no estaba en la lista de presentes.")

print(" Los alumnos presentes fueron:", asistencia)

#Ejercicio 6
reversa= [ 100, 33, 96, 15, 22 ,-15 , 74 ]
for n in reversa:
      slicing= reversa [::-1]
print (slicing)

#Ejercicio 7
temp_max= []
temp_min= []
for t in range (7):
    temp= (float ( input "Ingrese la temperatura máxima del día: "))

#Ejercicio 8
import statistics
temp_max= []
temp_min= []
amplitudes= []
dias_semana= ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
for dia in dias_semana:
         temp=  float ( input ("Ingrese la temperatura máxima del día: "))
         temp_max.append (temp)
         temp_minima= float ( input ("Ingrese la temperatura mínima del día: "))
         temp_min.append (temp_minima)
         amplitudes.append (temp - temp_minima)
mean_max= statistics.mean (temp_max)
mean_min= statistics.mean (temp_min)
amplitud= max (amplitudes)
dia_amplitud= dias_semana [amplitudes.index(amplitud)]
print (f" La temperatura máxima promedio fue de {mean_max} °C")
print (f" La temperatura mínima promedio fue de {mean_min} °C")
print (f" El día de mayor amplitud térmica fue el {dia_amplitud} con una amplitud de {amplitud} °C ")

#Ejercicio 9



