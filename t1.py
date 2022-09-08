# Dividir un numero de tres cifras, en centenas decenas unidades
#   1425    1  4  2   5

import math

print('Dividir un numero de tres cifras, en centenas decenas unidades')
num = int(input('Dame tu año de nacimient (número de 4 cifras) ? '))

millares = math.trunc(num/1000)
centenas = math.trunc( (num - (millares*1000) ) / 100 )
decenas = math.trunc(  (num - (millares*1000 + centenas*100)) / 10 )
unidades = num - (millares* 1000 + centenas * 100 + decenas * 10)

print(f'El numero de la suerte es {millares + centenas + decenas + unidades}')