import sys
import random
from typing import Callable, Any

def generar_numeros(cantidad: int, generador: Callable[[], Any]) -> list:
    """
    Función de orden superior que genera una lista de elementos usando la función generadora
    
    Args:
        cantidad: Número de elementos a generar
        generador: Función que genera cada elemento
        
    Returns:
        Lista con los elementos generados
    """
    return [generador() for _ in range(cantidad)]

def generar_numero_aleatorio() -> int:
    """Genera un número aleatorio entre 1 y 100"""
    return random.randint(1, 100)

def formatear_salida(lista: list, formateador: Callable[[Any], str]) -> str:
    """
    Función de orden superior que formatea la salida según la función proporcionada
    
    Args:
        lista: Lista a formatear
        formateador: Función que convierte cada elemento a string
        
    Returns:
        Cadena formateada
    """
    return ' '.join(map(formateador, lista))

def formateador_default(elemento: Any) -> str:
    """Convierte un elemento a string"""
    return str(elemento)

def main(*args):
    """
    Función principal que maneja los argumentos variables
    
    Args:
        args: Argumentos de línea de comandos
    """
    try:
        if len(args) == 0:
            cantidad = 5  # Valor por defecto
        else:
            cantidad = int(args[0])
            
        numeros = generar_numeros(cantidad, generar_numero_aleatorio)
        salida = formatear_salida(numeros, formateador_default)
        print(salida)
        
    except ValueError:
        print("Error: El argumento debe ser un número entero")
        sys.exit(1)

if __name__ == "__main__":
    # Obtener argumentos de la línea de comandos (excluyendo el nombre del script)
    argumentos = sys.argv[1:]
    main(*argumentos)