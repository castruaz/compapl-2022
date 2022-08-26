# Uso de las funciones trigonometricas de python
import math

print('Uso de las funciones trigonometricas de python')
angulo = int(input('Dame un angulo en radianes ? '))
seno = math.sin(angulo)
coseno = math.cos(angulo)
tangente = math.tan(angulo)
grados = math.degrees(angulo)

# print(f'Seno {seno}, Coseno {coseno}, Tangente {tangente}, Grados {grados}')

salida = (
"Resumen de funciones trigonometricas\n"
f"El seno es {seno:.2f}\n"
f"El coseno es {coseno:.2f}\n"
f"La tangente es {tangente:.2f}\n"
f"El angulo {angulo} en radianes, equivale a {grados:.2f} grados \n"
)

print(salida)


