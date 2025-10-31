#Trabajo Práctico 8: Manejo de archivos csv
import os

#Ejercicio 1
#1. Crear archivo inicial con productos: Crear un archivo de texto llamado productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad
def crear_archivo_inicial():
    if not os.path.exists('productos.txt'):
        with open('productos.txt', 'w') as archivo:
            archivo.write("Queso,7500,10\n")
            archivo.write("Pan,2600,20\n")
            archivo.write("Vino,1500,15\n")

#Ejercicio 2

with open('productos.txt', 'r') as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(',')
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

#Ejercicio 3

nuevo_producto = input("Ingrese un nuevo producto (nombre,precio,cantidad) separado por comas: ")
with open('productos.txt', 'a') as archivo:
    archivo.write(nuevo_producto + '\n')
print("Producto agregado exitosamente.")

#Ejercicio 4
#Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en una lista llamada productos
# , donde cada elemento sea un diccionario con claves: nombre, precio, cantidad.
productos = []
with open('productos.txt', 'r') as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(',')
        producto = {
            'nombre': nombre,
            'precio': float(precio),
            'cantidad': int(cantidad)
        }
        productos.append(producto)

#Ejercicio 5
#Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un producto. Recorrer la lista de productos y, si lo encuentra, 
# mostrar todos sus datos. Si no existe, mostrar un mensaje de error.
nombre_producto = input("Ingrese el nombre del producto a buscar: ")
encontrado = False
for producto in productos:
    if producto['nombre'].lower() == nombre_producto.lower():
        print(f"Producto encontrado: {producto}")
        encontrado = True
        break
    else:
        encontrado = False
if not encontrado:
    print("Producto no encontrado.")
#Ejercicio 6
#Guardar los productos actualizados: Después de haber leído, buscado o agregado productos, 
# sobrescribir el archivo productos.txt escribiendo nuevamente todos los productos actualizados desde la lista.
with open('productos.txt', 'w') as archivo:
    for producto in productos:
        linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
        archivo.write(linea)
print("Archivo productos.txt actualizado exitosamente.")

