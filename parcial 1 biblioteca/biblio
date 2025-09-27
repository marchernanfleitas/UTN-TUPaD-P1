#Primer parcial Programación I
#Alumno: Fleitas Marcelo Hernan
#Comisión 4

titulos=[ ]
ejemplares=[ ]
prestamos=0
devoluciones=0
print ("Bienvenido a la biblioteca desarrollada para el primer parcial de programación. Por favor digite sólo números cuando en consola se le pida ingresar valores numéricos para acceder a las distintas funciones detalladas en consola.")
#1.Ingresar títulos → Para agregar los títulos iniciales de los libros, el usuario indica la cantidad inicial.
#2.Ingresar ejemplares → Para agregar una cantidad de copias para cada título.
#3.Mostrar catálogo → Muestra todos los libros y su stock actual.
#4.Consultar disponibilidad → Busca un título específico y muestra cuántos ejemplares hay. Agregar prestados
#5.Listar agotados → Muestra los títulos que tienen 0 ejemplares.
#6.Agregar título → Permite añadir un nuevo libro y sus ejemplares disponibles al catálogo, respetando la sincronía de los índices en las listas.
#7.Actualizar ejemplares (préstamo/devolución) → Permite modificar el stock de un libro, elegido por el usuario, para registrar préstamos o devoluciones.
#-Préstamo -> Disminuye en 1 la cantidad de ejemplares del libro seleccionado, si hay unidades suficientes.
#-Devolución -> Aumenta en 1 la cantidad de ejemplares del libro seleccionado.
#8.Salir → Termina la ejecución del programa.
opcion_elegida=""

while opcion_elegida != "8":
    print("--- Menú ---")
    print("1. Ingresar títulos")
    print("2. Ingresar ejemplares")
    print("3. Mostrar catálogo")
    print("4. Consultar disponibilidad")
    print("5. Listar agotados")
    print("6. Agregar título")
    print("7. Actualizar ejemplares (préstamo/devolución)")
    print("8. Salir")
    opcion_elegida = input("Ingrese una opción (1-8): ").strip()
    #Debo validar que la opción ingresada sea correcta(sin espacios y un número del 1 al 8)
    if not opcion_elegida.isdigit() or opcion_elegida not in ["1","2","3","4","5","6","7","8"]:
        print("Por favor verifique de ingresar un valor de opción válido (1 al 8)")
        continue

    match opcion_elegida:
        
        case "1":
            print("Ingrese los títulos iniciales de su biblioteca")
            
            while True:
                num_titulos_str = input("Ingrese la cantidad de títulos distintos que desea agregar: ").strip()
                if num_titulos_str.isdigit() and int(num_titulos_str) > 0:
                    num_titulos = int(num_titulos_str)
                    break
                print("Por favor ingrese un número entero mayor a cero.")
            for _ in range(num_titulos):
                while True:
                    ingreso_titulos = input("Ingrese el título a agregar: ").strip()
                    
                    if ingreso_titulos == "":
                        print("No se pueden agregar títulos vacíos. Intente nuevamente.")
                        continue

                    if ingreso_titulos.lower() in [t.lower() for t in titulos]:
                        print(f"El título '{ingreso_titulos}' ya tiene existencias en el catálogo.")
                        break 

                    while True:
                        ejem_iniciales_str = input(f"Ingrese la cantidad inicial de ejemplares del título '{ingreso_titulos}': ").strip()
                        
                        if ejem_iniciales_str.isdigit() and int(ejem_iniciales_str) > 0:
                            ejem_iniciales = int(ejem_iniciales_str)
                            break
                        
                        print("Se ha ingresado una cantidad inválida. Ingrese un número entero mayor a cero.")
                    
                    titulos.append(ingreso_titulos)
                    ejemplares.append(ejem_iniciales)
                    print(f"-> Título '{ingreso_titulos}' agregado con {ejem_iniciales} ejemplares.")
                    break 

        case "2":
            if len(titulos) == 0:
                print("Todavía no se han ingresado títulos. Primero cárguelos en la opción 1")
                continue

            for t in range(len(titulos)):
                entrada_tit = input(f"Ingrese la cantidad de ejemplares a agregar del título '{titulos[t]}': ").strip()

                #Me aseguro que la entrada sea un número 
                while not entrada_tit.isdigit():
                    print("Lo ingresado no es una cantidad válida. Por favor ingrese un número entero mayor o igual a cero. (Ej: 2)")
                    entrada_tit = input(f"Ingrese nuevamente la cantidad de ejemplares a agregar del título '{titulos[t]}': ")
                
                nuevos_ejemplares = int(entrada_tit)
                
                if nuevos_ejemplares <= 0:
                    print("Cantidad inválida. No se pueden agregar ejemplares negativos o cero.")
                else:
                    ejemplares[t] += nuevos_ejemplares
                    print(f"Se han agregado {nuevos_ejemplares} ejemplares al título '{titulos[t]}'")

        case "3":
            if len(titulos)==0:
               print ("Todavía no se han ingresado títulos. Primero cárguelos en la opción 1")

               continue

            print("--- Catálogo de libros ---")
            for i in range(len(titulos)):
                print(f"{titulos[i]} - Ejemplares disponibles: {ejemplares[i]}")
                if ejemplares[i] == 0:
                    print("(Agotado)")
            
        case "4":
            busqueda_titulo = input("Ingrese el título a buscar: ")
            titulos_lower = [titulo.lower() for titulo in titulos]
            if busqueda_titulo.lower() in titulos_lower:
                #Uso una variable auxiliar para evitar problemas con mayúsculas y minúsculas.
                indice = titulos_lower.index(busqueda_titulo.lower())

                print("Su búsqueda arrojó los siguientes resultados:")

                print(f"El título '{titulos[indice]}' tiene {ejemplares[indice]} ejemplares disponibles.")

            else:
                print(f"El título '{busqueda_titulo}' no se encuentra en el catálogo.")

        case "5":
            tit_agotados= False
            for a in range (len(ejemplares)):
               if ejemplares[a] ==0:
                  print (f" El {titulos[a]} ")
                  tit_agotados=True
            if not tit_agotados:
               print ("No se encuentran títulos agotados en el sistema.")

        case "6":
            nuevo_titulo = input("Ingrese el título a agregar: ")
            if nuevo_titulo == "":
               print ("No se pueden agregar títulos vacíos")
               continue   
            
            existencia = False

            for n in titulos:
                if nuevo_titulo.lower() == n.lower():
                    print(f"El título '{nuevo_titulo}' ya tiene existencias en el catálogo.")
                    existencia = True
                    break  

            if not existencia:
                # Validación de entrada
                cant_ejemplares = input(f"Ingrese la cantidad de ejemplares del título '{nuevo_titulo}': ")
                while not cant_ejemplares.isdigit() or int(cant_ejemplares) <= 0:
                    print("Entrada inválida. Por favor ingresar un número entero mayor a cero.")
                    cant_ejemplares = input(f"Ingrese nuevamente la cantidad de ejemplares del título '{nuevo_titulo}': ")

                # Convierto a entero y cargo en listas
                cant_ejemplares = int(cant_ejemplares)
                titulos.append(nuevo_titulo)
                ejemplares.append(cant_ejemplares)
                print(f"El título '{nuevo_titulo}' con {cant_ejemplares} ejemplares se ha agregado al catálogo.")

        case "7":
           if len(titulos)==0:
            print ("Todavía no se han ingresado títulos. Primero cárguelos en la opción 1")  
            continue
            
           titulo_usuario = input("Ingrese el título que desea prestar o devolver: ").strip()
           encontrado = False
            
           señalador=-1
           for i in range(len(titulos)):
            if titulo_usuario.lower() == titulos[i].lower():
             señalador=i
             encontrado = True

           if not encontrado:
            print(f"El título '{titulo_usuario}' no se encuentra en el catálogo.")
            continue

           modif_stock = input("Digite la opción que desea realizar: Préstamo (1) o Devolución (2): ")
           while modif_stock not in ["1", "2"]:
             print("Opción inválida. Ingrese 1 para Préstamo o 2 para Devolución.")
             modif_stock = input("Digite la opción que desea realizar: Préstamo (1) o Devolución (2): ")

           if modif_stock == "1":
            if ejemplares[señalador] > 0:
                ejemplares[señalador] -= 1
                prestamos += 1
                print(f"El título '{titulos[señalador]}' ha sido prestado. Ejemplares restantes: {ejemplares[señalador]}")
            else:
                print(f"No hay ejemplares disponibles para préstamo del título '{titulos[señalador]}'.")
           elif modif_stock == "2":
            if prestamos <= 0:
                print("No se puede devolver ejemplares porque no se registraron préstamos anteriores.")
                #Cada vuelta del bucle principal modifica los valores de variables y al solo tener dos listas no es posible sincronizar los datos de las listas con los prestamos y devoluciones por eso se deja la opción considerada más eficiente siempre que el usuario lleve un control o registro paralelo.
                #Si existe solución posible u otros métodos que pude haber omitido por favor comentenlo en la devolución.
                print("Notas del desarrollo: El sistema no puede verificar si el ejemplar devuelto corresponde a uno prestado anteriormente si el usuario no lleva un registro externo.")

            else:
                ejemplares[señalador] += 1
                devoluciones += 1
                print(f"Se ha devuelto el ejemplar del título '{titulos[señalador]}'.")
        
        case "8":
         print("Se ha salido del programa")
         break
         
