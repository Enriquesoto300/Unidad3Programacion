import numpy as np

def leer_matriz():
    f = int(input("Número de filas: "))
    c = int(input("Número de columnas: "))
    matriz = []
    for i in range(f):
        fila = input(f"Fila {i+1} (números separados por espacio): ").split()
        fila = [float(x) for x in fila]
        matriz.append(fila)
    return np.array(matriz)

while True:
    print("\n=== Calculadora de Matrices ===")
    print("1. Suma de matrices")
    print("2. Resta de matrices")
    print("3. Multiplicación de matrices")
    print("4. Transposición de matriz")
    print("5. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("Matriz A")
        A = leer_matriz()
        print("Matriz B")
        B = leer_matriz()
        if A.shape == B.shape:
            print("Resultado:")
            print(A + B)
        else:
            print("No se pueden sumar, deben tener el mismo tamaño")

    elif opcion == "2":
        print("Matriz A")
        A = leer_matriz()
        print("Matriz B")
        B = leer_matriz()
        if A.shape == B.shape:
            print("Resultado:")
            print(A - B)
        else:
            print("No se pueden restar, deben tener el mismo tamaño")

    elif opcion == "3":
        print("Matriz A")
        A = leer_matriz()
        print("Matriz B")
        B = leer_matriz()
        if A.shape[1] == B.shape[0]:
            print("Resultado:")
            print(A @ B)
        else:
            print("No se pueden multiplicar, columnas de A ≠ filas de B")

    elif opcion == "4":
        print("Matriz A")
        A = leer_matriz()
        print("Resultado:")
        print(A.T)

    elif opcion == "5":
        print("Saliendo...")
        break

    else:
        print("Opción no válida")

#facilito        
