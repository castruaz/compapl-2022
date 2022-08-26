# Dividir un numero de tres cifras, en centenas decenas unidades
#   425    4  2   5

import math

print('Dividir un numero de tres cifras, en centenas decenas unidades')
num = int(input('Dame un numero entero de 3 cifras ? '))

centenas = math.trunc(num / 100)
decenas = math.trunc( (num - centenas * 100) / 10 ) 
unidades = num - (centenas * 100 + decenas * 10)

print(f'centenas {centenas}, decenas {decenas} unidades {unidades}')