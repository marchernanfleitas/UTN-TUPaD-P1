#Trabajo Práctico 7: Estructuras de datos complejas
#Ejercicio 1,2 y 3
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)
#modificar
precios_frutas['Banana'] = 1330
precios_frutas['Manzana']= 1700
precios_frutas['Pera'] = 2800
print(precios_frutas)
#lista que posea productos
productos=precios_frutas.keys()
print(productos)
#Ejercicio 4 Escribí un programa que permita almacenar y consultar números telefónicos
contactos_telefonicos= {'Nombre': 'Número Teléfono'}
def agregar_contacto(nombre, numero):
    contactos_telefonicos[nombre] = numero      
    return contactos_telefonicos
for _ in range(5):
    nombre=input("Ingrese el nombre del contacto: ")
    numero=input("Ingrese el número telefónico: ")
    agregar_contacto(nombre, numero)

nombre_consulta=input("Ingrese el nombre del contacto a consultar: ")
if nombre_consulta in contactos_telefonicos:
    print(f"El número telefónico de {nombre_consulta} es {contactos_telefonicos[nombre_consulta]}")
else:
        print("Contacto no encontrado")
#Ejercicio 5
frase = input("Ingrese una frase : ")
palabras = frase.split()
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)
contador_palabras = {}
for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1
print("Cantidad de veces que aparece cada palabra:", contador_palabras)
#Ejercicio 6
#Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno.
notas_alumnos = {}
for _ in range(3):
    nombre_alumno = input("Ingrese el nombre del alumno: ")
    notas = []
    while len(notas) < 3:
        nota = float(input(f"Ingrese la nota de {nombre_alumno}: "))
        if nota < 0:
            print("Por favor, ingrese una nota válida mayor a 0")
        notas.append(nota)
    notas_alumnos[nombre_alumno] = tuple(notas)
for alumno, notas in notas_alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {alumno} es: {promedio:.2f}")
#Ejercicio 7
parcial_1 = {40, 30, 80, 92, 55}
parcial_2 = {25, 45, 60, 77, 18}
#filtro los que aprobaron
aprob_parcial_1 = {n for n in parcial_1 if n >= 40}
aprob_parcial_2 = {n for n in parcial_2 if n >= 40}
#Aplico operaciones de conjuntos
nota_ambos= aprob_parcial_1 & aprob_parcial_2
print ("Estudiantes que aprobaron ambos parciales:", nota_ambos)
nota_solo_uno= aprob_parcial_1 ^ aprob_parcial_2
print ("Estudiantes que aprobaron solo uno de los dos parciales:", nota_solo_uno)
nota_al_menos_uno= aprob_parcial_1 | aprob_parcial_2
print ("Estudiantes que aprobaron al menos un parcial:", nota_al_menos_uno)
#Ejercicio 8
#Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe.
producto_stock= {}
def consultar_stock(producto):
    return producto_stock.get(producto, "Producto no encontrado")
def agregar_o_actualizar_producto(producto, cantidad):
    if producto in producto_stock:
        producto_stock[producto] += cantidad
    else:
        producto_stock[producto] = cantidad
    return producto_stock
while True:
    accion = input("Ingrese 'consultar' para consultar stock, 'agregar' para agregar/actualizar producto, o 'salir' para terminar: ").lower()
    if accion == 'salir':
        break
    elif accion == 'consultar':
        producto = input("Ingrese el nombre del producto a consultar: ")
        print(f"Stock de {producto}: {consultar_stock(producto)}")
    elif accion == 'agregar':
        producto = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad a agregar: "))
        agregar_o_actualizar_producto(producto, cantidad)
        print(f"Producto actualizado: {producto_stock}")
    else:
        print("Acción no válida. Por favor, intente de nuevo.")
#Ejercicio 9
#Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. Ejemplo:
agenda={
    ("lunes", "10:00"): "Reunión", ("martes", "15:00"): "Clase Inglés"
}
def agregar_evento(dia, hora, evento):
    agenda[(dia, hora)] = evento
    return agenda
def consultar_evento(dia, hora):
    return agenda.get((dia, hora), "No hay evento programado") 
while True:
    accion = input("Ingrese 'consultar' para consultar evento, 'agregar' para agregar evento, o 'salir' para terminar: ").lower()
    if accion == 'salir':
        break
    elif accion == 'consultar':
        dia = input("Ingrese el día del evento a consultar: ").lower().strip()
        hora = input("Ingrese la hora del evento a consultar (formato HH:MM): ")
        print(f"Evento en {dia} a las {hora}: {consultar_evento(dia, hora)}")
    elif accion == 'agregar':
        dia = input("Ingrese el día del evento: ").lower().strip()
        while dia not in ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]:
            print("Día inválido. Por favor, ingrese un día válido de la semana.")
            dia = input("Ingrese el día del evento: ")
        hora = input("Ingrese la hora del evento (formato HH:MM): ")
        while hora not in [f"{h:02d}:00" for h in range(24)] + [f"{h:02d}:59" for h in range(24)]:
            print("Hora inválida. Por favor, ingrese una hora en formato HH:MM (00:00 a 23:59).")
            hora = input("Ingrese la hora del evento (formato HH:MM): ")
        evento = input("Ingrese el nombre del evento: ")
        agregar_evento(dia, hora, evento)
        print(f"Evento agregado/actualizado: {agenda}")
    else:
        print("Acción no válida. Por favor, intente de nuevo.")

#Ejercicio 10
atlas = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
}
ingreso_atlas= input("¿Desea agregar más países y capitales al diccionario? (s/n): ").lower()
while ingreso_atlas == 's': 
    pais = input("Ingrese el nombre del país: ").strip()
    capital = input("Ingrese el nombre de la capital: ").strip()
    atlas[pais] = capital
    ingreso_atlas = input("¿Desea agregar más países y capitales al diccionario? (s/n): ").lower()
def invertir_diccionario(diccionario):
    diccionario_invertido = {}
    for pais, capital in diccionario.items():
        diccionario_invertido[capital] = pais
    return diccionario_invertido
diccionario_invertido = invertir_diccionario(atlas)
print("Diccionario invertido (capitales como claves):")
print(diccionario_invertido)


