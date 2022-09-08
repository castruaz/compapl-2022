# Verificar si la suma de dos numeros es igual a un terero
# 4 5 9   . son iguales
# 1 3 5   . son distintos

print('Verificar si la suma de dos numeros es igual a un terero\n')
print('Dame 3 numeros enteros, separados por Enter ')
n1, n2, n3 = int(input()), int(input()), int(input())

if n1 + n2 == n3:
    print('Son iguales')
else:
    print('Son distintos')



