#Parte 1 del ejercicio. Punto 1 y 2.

base = 9        #Variable base con valor entero 9
altura = 5      #Variable altura con valor entero 5

area = base*altura/2        #operar area. area = 22.5
area = str (area)       #convertir area en string. area pasa de ser 22.5 a '22.5'

mensaje = "El area del triangulo es igual a"        #Crear variable mensaje igual a "El area del triangulo es igual a"

print (mensaje, area)       #Imprimir valor de mensaje + area ('El area del triangulo es igual a' + '22.5')


#Parte 2 del ejercicio. Punto 3.

base = '5'      #Variable base con valor string 5 ('5')
altura = '7'        #Variable altura con valor string 7 ('7')

base = int (base)       #Debemos convertir la string base en integer base para operar
altura = int (altura)       #Debemos convertir la string altura en integer altura para operar

area = base*altura/2        #Operamos la nueva area

area = float (area)     #La variable area debe ser de tipo float

print (mensaje,area)        #Imprimimos el valor de mensaje y de area