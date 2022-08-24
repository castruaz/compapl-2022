# Lee datos y envia un saludo

print('Leyendo datos y enviar saludo')
nombre = input('Dame tu nombre ? ') # leer una cadena
edad = int(input('Dame tu edad ? ')) # leer una cadena, luego la convierto entero
peso = float(input('Dame tu peso ? ')) # leer una cadena, luego convertir a flotante

print('Hola', nombre,'bienvenido a Python, tu edad es', edad ,'tu peso es',peso)
print(f'Hola {nombre} bienvenido a Python, tu edad es {edad}, tu peso es {peso}')

print(type(nombre))
print(type(edad))
print(type(peso))