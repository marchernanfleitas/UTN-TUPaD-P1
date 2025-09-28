#Trabajo Práctico Integrador Matemáticas y Programación 1
#Alumno: Fleitas Marcelo Hernan
#Comisión 4

#Conversión de Números:
#Desarrollen un programa que convierta números decimales a binarios y, de forma opcional, también de binario a decimal.
opcion=0
while opcion!="3":
    print("Conversor de Números Decimales a Binarios y viceversa (solo para números enteros)")
    print ("1-Decimal a binario")
    print ("2-Binario a decimal")
    print ("3-Salir")  
    opcion=((input("Ingrese la opción deseada: ")))
    #Verifico que sean válidos.
    if not opcion.isdigit() or opcion not in ["1","2","3"]:
        print("Por favor verifique de ingresar un valor de opción válido (1 al 3)")
        continue
        #Luego convierto a entero
    opcion=int(opcion)
        
    if opcion==1:
        while True:
            nro_decimal=(input("Ingrese un número decimal positivo: "))
            #Verifico que sea válido
            if not nro_decimal.isdigit():
                    print("Por favor ingrese un número decimal válido")
                    continue
                #Convierto a entero
            nro_decimal=int(nro_decimal)
            #Verifico que sea mayor a 0
            if nro_decimal<0:
                    print("Por favor ingrese un número decimal positivo")
                    continue
            else:
                    break
        binario=bin(nro_decimal).replace("0b","")
        print(f"El número decimal {nro_decimal} en binario es: {binario}")
    elif opcion==2:
            binario=input("Ingrese un número binario: ")
        #Verifico que sean 1 o 0 y que no se ingrese un valor vacío que crashearía mi ejecución
            if not all(digit in "01" for digit in binario) or binario=="":
                print("Por favor ingrese un número binario válido")
                continue
            nro_decimal=int(binario,2)
            print(f"El número binario {binario} en decimal es: {nro_decimal}")
    elif opcion==3:
            print("Salida exitosa. Gracias por usar el conversor")
            break
