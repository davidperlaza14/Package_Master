import os
import subprocess
from auth import generate_token, token_required, store_token, clear_token



# Obtener la URL de la base de datos desde las variables de entorno
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///default.db')

# Crear una conexión a la base de datos
# zengine = create_engine(DATABASE_URL)

# Simulamos un pequeño sistema de usuarios
USERS = {
    'admin': 'password123',
}

def login(username, password):
    """Simula un proceso de inicio de sesion básico"""
    if USERS.get(username) == password:
        # Si las credenciales son correctas, generamos un token
        token = generate_token(user_id=username)
        store_token(token) # Almacena el token
        return f"Login exitoso. Token almacenado."
    else:
        return "Credenciales inválidas"



# Aquí podrías realizar operaciones sobre la base de datos
print(f"Conectado a la base de datos: {DATABASE_URL}")

@token_required
def instalar_paquete(current_user, paquete):
    try:
        # Ejecutamos el comando pip install para instalar el paquete
        resultado = subprocess.run(
            ['pip', 'install', paquete],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
            
        )
        print(f"Paquete '{paquete}' instalado correctamente.")
        print(resultado.stdout)
    except subprocess.CalledProcessError as e:
        print(F"Error al intentar instalar el paquete '{paquete}': {e.stderr}")    

@token_required
def actualizar_paquete(current_user, paquete):
    try:
        resultado = subprocess.run(
            ['pip', 'install', '--upgrade', paquete],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(f"Paquete '{paquete}' actualizado correctamente.")
        print(resultado.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error al intentar actualizar el paquete '{paquete}': {e.stderr}")

@token_required
def desinstalar_paquete(current_user, paquete):
    try:
        resultado = subprocess.run(
            ['pip', 'uninstall', '-y', paquete],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
            
        )
        print(f"Paquete '{paquete}' disinstalado correctamente por el usuario '{current_user}'.")
        print(resultado.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error al intentar desinstalar el paquete '{paquete}': {e.stderr}")

@token_required
def listar_paquetes(current_user):
    """Funcion protegida para listar paquetes, requiere autenticacion"""
    try:
        resultado = subprocess.run(
            ['pip', 'list' ],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(f"Lista de paquetes instalados para el usuario {current_user}:")
        print(resultado.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error al intentar listar paquetes {e.stderr}")



def main():
    print("¡Bienvenido al sistema de gestion de paqueteria!")
    print("Por favor, inicie sesión.")

    # Solicitar login para generar token
    username = input("Usuario: ")
    password = input("Contraseña: ")

    # Proceso de login
    message_login = login(username, password)
    print(message_login)

    # Continuar si el login fue exitoso
    if "Token almacenado" not in message_login:
        return

    print("\nOpciones:")
    print("1. Instalar paquete")
    print("2. Actualizar paquete")
    print("3. Desinstalar paquete")
    print("4. Listar paquetes")
    print("5. Cerrar sesión")

    opcion = input("Seleccione una opcion (1/2/3/4/5): ")

    if opcion == "1":
        paquete = input("Introduce el nombre del paquete que deseas instalar: ")
        instalar_paquete(paquete=paquete)
    elif opcion == "2":
        paquete = input("Introduce el nombre del paquete que deseas actualizar: ")
        actualizar_paquete(paquete=paquete)
    elif opcion == "3":
        paquete = input("Introduce el nombre del paquete que deseas desinstalar: ")
        desinstalar_paquete(paquete=paquete)
    elif opcion == "4":
        listar_paquetes()
    elif opcion == "5":
        clear_token()
        print("Sesión cerrada. El token ha sido eliminado.")
    else:
        print("Opcion no valida. Por favor, selecciona 1, 2, 3, 4 ó 5.")



if __name__ == "__main__":
    main()