
# Por último, para el Switch, deberás crear la variable estacion, y distintos case para las cuatro estaciones del año. Dependiendo del valor de la variable 
# estacion se deberá mandar un mensaje por consola informando de la estación en la que está. También habrá que poner un default para cuando el valor de la variable no sea una estación.


#En python es diferente : 

def switch(estacion):
    if estacion ==  'invierno' :
        return 'Estacion invierno '
    elif estacion == 'Primavera' : 
        return 'Estacion Primavera'
    elif estacion == 'verano' :
        return 'Estacion Verano'
    elif estacion == 'otono' :
        return 'Estacion Verano'
    #default
    else :
        return 'No as escrito una estacion'


invierno = switch('invierno')
primareva = switch('Primavera')
verano = switch('verano')
otrono = switch('Otroño')



print(invierno)
