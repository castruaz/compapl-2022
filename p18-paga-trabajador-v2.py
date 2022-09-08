# Calcular la paga total de un trabajador v2 

print('Calculando la paga de un trabajor \n\n')

# Entrada
nombre = input('Dame el nombre ? ')
horas = int(input('Dame las horas trabajadas? '))
paga = float(input('Dame paga por hora? '))
tasa = 0.3

# Calculo
if horas <=40:
    pagabruta = horas * paga
else:
    extra = horas - 40
    pagabruta = (40 * paga) + (extra * paga * 2)


impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto

# Salida
print('\nResumen de pagos \n')
print(f'El trabajador {nombre}, trabajo {horas}, con una paga de {paga} pesos la hora\n')
print(f'Paga bruta = {pagabruta}')
print(f'Impuesto   = {impuesto}')
print(f'Paga neta  = {paganeta}')