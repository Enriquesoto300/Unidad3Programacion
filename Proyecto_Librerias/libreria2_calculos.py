# libreria2_calculos.py

def sumar_lista(lista):
    """Suma los números de una lista"""
    return sum(lista)

def multiplicar_lista(lista):
    """Multiplica los números de una lista"""
    resultado = 1
    for num in lista:
        resultado *= num
    return resultado
