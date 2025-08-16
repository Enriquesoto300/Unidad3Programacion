# main.py
# Calculadora simple en Python

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: división entre cero"
    return a / b

if __name__ == "__main__":
    print("Calculadora simple")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    
    opcion = int(input("Elige una opción: "))
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    
    if opcion == 1:
        print("Resultado:", suma(a, b))
    elif opcion == 2:
        print("Resultado:", resta(a, b))
    elif opcion == 3:
        print("Resultado:", multiplicacion(a, b))
    elif opcion == 4:
        print("Resultado:", division(a, b))
    else:
        print("Opción no válida")
