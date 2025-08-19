
import numpy as np


estudiantes = {
    "A001": {"nombre": "Ana Torres", "edad": 20, "calificaciones": [90, 85, 78]},
    "A002": {"nombre": "Luis Pérez", "edad": 22, "calificaciones": [88, 91, 79]}
}

def agregar_estudiante():
    id_est = input("Ingresa el ID del estudiante: ").upper()
    if id_est in estudiantes:
        print("Ese ID ya existe. Intenta con otro.\n")
        return
    nombre = input("Nombre completo: ")
    try:
        edad = int(input("Edad: "))
    except ValueError:
        print("Edad inválida. Debe ser un número.\n")
        return
    calificaciones = []
    while True:
        nota = input("Ingresa una calificación (o deja vacío para terminar): ")
        if nota == "":
            break
        try:
            calificaciones.append(float(nota))
        except ValueError:
            print("La calificación debe ser un número.")
    estudiantes[id_est] = {"nombre": nombre, "edad": edad, "calificaciones": calificaciones}
    print(f"Estudiante {id_est} agregado correctamente.\n")

def mostrar_estudiantes():
    if not estudiantes:
        print("No hay estudiantes registrados.\n")
        return
    for id_est, info in estudiantes.items():
        promedio = np.mean(info["calificaciones"]) if info["calificaciones"] else 0
        print(f"Estudiante {id_est} - {info['nombre']} - Promedio: {promedio:.1f}")
    print()

def promedio_estudiante():
    id_est = input("Ingresa el ID del estudiante: ").upper()
    if id_est not in estudiantes:
        print("ID no encontrado.\n")
        return
    calificaciones = estudiantes[id_est]["calificaciones"]
    if not calificaciones:
        print("Este estudiante no tiene calificaciones.\n")
        return
    promedio = np.mean(calificaciones)
    print(f"Promedio de {estudiantes[id_est]['nombre']}: {promedio:.1f}\n")

def eliminar_estudiante():
    id_est = input("Ingresa el ID del estudiante a eliminar: ").upper()
    if id_est in estudiantes:
        del estudiantes[id_est]
        print(f"Estudiante {id_est} eliminado.\n")
    else:
        print("ID no encontrado.\n")

#Menu
while True:
    print("=== Gestión de Estudiantes ===")
    print("1. Agregar estudiante")
    print("2. Mostrar todos los estudiantes")
    print("3. Calcular promedio de un estudiante")
    print("4. Eliminar estudiante")
    print("5. Salir")
    opcion = input("Elige una opción: ")
    print()
    if opcion == "1":
        agregar_estudiante()
    elif opcion == "2":
        mostrar_estudiantes()
    elif opcion == "3":
        promedio_estudiante()
    elif opcion == "4":
        eliminar_estudiante()
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intenta de nuevo.\n")
