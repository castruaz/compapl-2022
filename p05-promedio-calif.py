# Calcular la suma y el promedio de tres calificaciones 

print('Calcular la suma y el promedio de tres calificaciones\n')
#c1 = int(input('Dame calificacion 1 ?'))
#c2 = int(input('Dame calificacion 2 ?'))
#c3 = int(input('Dame calificacion 3 ?'))
print('Dame tres calificaciones separadas por un espacio ?')
c1,c2,c3 = input().split()
c1,c2,c3 = [int(c1),int(c2),int(c3)]
suma = c1 + c2 + c3
prom = suma / 3
print(f'Los numeros fueron {c1}, {c2}, {c3}')
print(f'La suma {suma}')
print(f'El promedio {prom}')

