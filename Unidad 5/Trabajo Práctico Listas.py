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
