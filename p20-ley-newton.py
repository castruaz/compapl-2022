# segunda ley newton fuerza = masa * aceleracion

from re import A


print('Calculando los valores de la sgunda ley de newton \n')
print('[F] uerza      f = m * a')
print('[M] asa        m = f / a')
print('[A] celeracion a = f / m \n')

op = str.upper(input('Elige una opcion ? '))

if op=='F':
    print('\nCalculando la Fuerza')
    m = int(input('Dame la masa ? '))
    a = int(input('Dame la aceleracion ? '))
    f = m * a
    print(f'La fuerza es {f}')
elif op == 'M':
    print('\nCalculando la Masa')
    f = int(input('Dame la fuerza ? '))
    a = int(input('Dame la aceleracion ? '))
    m = f / a
    print(f'La masa es {m}')
elif op=='A':
    print('\nCalculando la Aceleracion')
    f = int(input('Dame la fuerza ? '))
    m = int(input('Dame la masa ? '))
    a = f / m
    print(f'La aceleracion es {a}')
else:
    print('Opcion invalida')

print('\nGracias por utilizar este programa')