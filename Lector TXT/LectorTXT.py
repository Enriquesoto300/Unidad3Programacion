import os

def leer_estudiantes(nombre_archivo):
    estudiantes = []
    try:
        with open(nombre_archivo, "r") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea:  
                    partes = linea.split(",")
                    if len(partes) != 2:
                        print(f"Formato incorrecto en la línea: {linea}")
                        continue
                    nombre, calificacion = partes
                    try:
                        calificacion = float(calificacion)
                    except ValueError:
                        print(f"Calificación inválida para {nombre}")
                        continue
                    estudiantes.append((nombre, calificacion))
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")
    return estudiantes

def calcular_promedio(estudiantes):
    if not estudiantes:
        return 0
    total = sum(calificacion for _, calificacion in estudiantes)
    return total / len(estudiantes)

def generar_reporte(estudiantes, promedio, nombre_reporte):
    try:
        with open(nombre_reporte, "w") as archivo:
            for nombre, calificacion in estudiantes:
                archivo.write(f"{nombre},{calificacion}\n")
            archivo.write(f"Promedio general: {promedio:.2f}\n")
        print(f"Reporte generado en {nombre_reporte}")
    except Exception as e:
        print(f"Ocurrió un error al generar el reporte: {e}")


def agregar_estudiante(nombre_archivo):
    nombre = input("Ingresa el nombre del estudiante: ")
    while True:
        try:
            calificacion = float(input("Ingresa la calificación: "))
            break
        except ValueError:
            print("Calificación inválida. Intenta de nuevo.")
    try:
        with open(nombre_archivo, "a") as archivo:
            archivo.write(f"{nombre},{calificacion}\n")
        print(f"{nombre} agregado correctamente.")
    except Exception as e:
        print(f"No se pudo agregar el estudiante: {e}")


archivo_estudiantes = "ListaEstudiantes.txt"
archivo_reporte = "reporte.txt"


while True:
    print("\nOpciones:")
    print("1. Ver estudiantes y generar reporte")
    print("2. Agregar nuevo estudiante")
    print("3. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        estudiantes = leer_estudiantes(archivo_estudiantes)
        promedio = calcular_promedio(estudiantes)
        generar_reporte(estudiantes, promedio, archivo_reporte)
    elif opcion == "2":
        agregar_estudiante(archivo_estudiantes)
    elif opcion == "3":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
