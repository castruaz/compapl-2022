# Calcular el area de un circulo
import math

print('Calculando el area de un circulo')
radio = float(input('Dame el valor del radio ? '))

#area = 3.1416 * radio * radio
area = math.pi * radio ** 2

print(f'El circulo de radio {radio} tiene un area de {area}')
