"""
Entradas 
    base - numero decimal 
    altura - numero decimal 

Salidas 
    area - numero decimal 

Proceso:
    1- Pedir base 
    2- Pedir altura 
    3- Multiplicar base * altura  y guardar en mult
    4- Dividir mult / 2 y guardar en area
    5- Mostrar area

Casos de prueba

Entradas 
    base = 5
    altura = 15


Salida esperada 
    area = 37.5 
Resultado obtenido
    area = 37.5 



"""
"""
Entrada
    precio - numero decimal 

Salida 
    mensaje - es valido/invalido

Proceso 
    1- Pedir precio 
    2- Si el precio es mayor a 0, mostrar "El precio es valido "
    3- Si el precio es menor o igual a 0, mostrar "El precio es invalido "

"""

precio = float(input("Ingrese el precio del producto: "))
 
if precio > 0 :
    print("El precio es valido ")
else:
    print("El precio es invalido ")



