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
                print("fecha no válida")
