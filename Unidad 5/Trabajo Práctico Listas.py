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
