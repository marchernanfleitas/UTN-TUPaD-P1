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

#Ejercicio 8
import statistics
estudiantes = ["Marco", "Diana", "Marilu", "Facundo", "Antonio"]
notas = [(5, 7, 4), (10, 9, 7), (8, 6, 9), (4, 2, 5), (7, 8, 3)]
materias = ["Música", "Percusión", "Canto"]
for m in range(3):
    print(f" La materia es: {materias[m]}")
    for e in range(5):
        print(f" Estudiante: {estudiantes[e]}")
        print(f" Nota: {notas[e][m]}")
        promedio_estudiante = statistics.mean(notas[e])
        print(f" El Promedio general de {estudiantes[e]}: {promedio_estudiante:.2f}")
print(f" El promedio en Música es: {statistics.mean([notas[e][0] for e in range(5)]):.2f}")
print(f" El promedio en Percusión es: {statistics.mean([notas[e][1] for e in range(5)]):.2f}")
print(f" El promedio en Canto es: {statistics.mean([notas[e][2] for e in range(5)]):.2f}")

#Ejercicio 9
# Creo un tablero vacío con espacios
tablero = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
# Inicializo el tablero con guiones "-"
for i in range(3):
    for j in range(3):
        tablero[i][j] = "-"
# Turnos: máximo 9 (voy reemplazando guiones por X y O)
for turno in range(9):
    # Determino el jugador
    if turno % 2 == 0:
        jugador = "X"
    else:
        jugador = "O"

    # Solicito jugada al jugador
    jugada = input("Ingrese su jugada (0 a 2) separando con una coma " + jugador + " (fila,columna): ")

    # Convertir entrada en dos números: fila y columna
    fila, columna = map(int, jugada.split(","))

    # Verifico si la casilla está libre
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
    else:
        print("¡Casilla ocupada! Pierdes el turno.")
        continue
 # Mostrar el tablero actualizado
    for f in tablero:
        print(" ".join(f))
    print()

#Ejercicio 10
productos = ["leche", "pan", "queso", "salame"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
ventas = []

print("Ingrese la cantidad vendida por cada producto en cada día:")

for p in productos:
    ventas_producto = []
    for dia in dias:
        while True:
            cantidad = input(f"Ingrese cantidad de '{p}' vendida el {dia}: ")
            if cantidad.replace(".", "", 1).isdigit():
                cantidad = float(cantidad)
                if cantidad >= 0:
                    cantidad_entera = round(cantidad)
                    ventas_producto.append(cantidad_entera)
                    break
                else:
                    print("El número no puede ser negativo.")
            else:
                print("Debe ingresar un número válido (positivo).")
    ventas.append(ventas_producto)

# Total vendido por producto
print("Total vendido por producto:")
for i, p in enumerate(productos):
    total = sum(ventas[i])
    print(f"  {p}: {total} unidades")

# Día con mayores ventas totales
ventas_dia = [0] * 7
for i in range(7):  # Días
    for j in range(4):  # Productos
        ventas_dia[i] += ventas[j][i]

indice_dia_mayor = ventas_dia.index(max(ventas_dia))
print(f"El día con mayores ventas fue el {dias[indice_dia_mayor]} con {ventas_dia[indice_dia_mayor]} unidades vendidas.")

# Producto más vendido en la semana
totales_productos = [sum(producto) for producto in ventas]
indice_producto_mayor = totales_productos.index(max(totales_productos))
print(f"El producto más vendido fue '{productos[indice_producto_mayor]}' con {totales_productos[indice_producto_mayor]} unidades.")


