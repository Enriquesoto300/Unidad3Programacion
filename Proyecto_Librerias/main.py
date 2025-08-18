# main.py

import libreria1_ascii
import libreria2_calculos
import libreria3_mensajes

print(libreria3_mensajes.mensaje_bienvenida)
print()

# Uso de la librería ASCII
print("Arte ASCII de corazones:")
libreria1_ascii.corazones(3)
print()

# Uso de la librería de cálculos
numeros = [2, 4, 6]
print(f"Lista de números: {numeros}")
print("Suma:", libreria2_calculos.sumar_lista(numeros))
print("Multiplicación:", libreria2_calculos.multiplicar_lista(numeros))
print()

print(libreria3_mensajes.mensaje_despedida)
