# Generar numeros de 1 a 200, sumarlos hasta obtener 100

# print('Generar n numeros para obtener una ganancia ')
# ganar = int(input('Cuanto quieres ganar ? '))
# c = 0
# suma = 0
# while suma < ganar:
#     c += 1
#     suma += c
# print('Suma = ',suma)
# print(f'Use {c} nuemeros')


print('Generar n numeros para obtener una ganancia ')
ganar = int(input('Cuanto quieres ganar ? '))
c = 0
suma = 0
while c < 500:
    c += 1
    suma += c
    print(c, end=' ')
    if suma >= ganar:
        print('\n')
        break

print('Suma > ', suma)