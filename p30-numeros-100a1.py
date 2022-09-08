# Imprime numeros de 100 a n usando while

print('Imprime los numeros de 100 a n')
n = int(input('Hasta donde quieres los numeros? '))
c = 100
while c >= n :
    print(c, end=" ")
    c -= 2