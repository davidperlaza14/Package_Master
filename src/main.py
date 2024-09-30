import os
import subprocess
from sqlalchemy import create_engine
from auth import generate_token, token_required


# Obtener la URL de la base de datos desde las variables de entorno
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///default.db')

# Crear una conexión a la base de datos
engine = create_engine(DATABASE_URL)

# Simulamos un pequeño sistema de usuarios
USERS = {
    'admin': 'password123',
}

def login(username, password):
    """Simula un proceso de inicio de sesion básico"""
    if USERS.get(username) == password:
        # Si las credenciales son correctas, generamos un token
        token = generate_token(user_id=username)
        return f"Token: {token}"
    else:
        return "Credenciales inválidas"



# Aquí podrías realizar operaciones sobre la base de datos
print(f"Conectado a la base de datos: {DATABASE_URL}")


def instalar_paquete(paquete):
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

def actualizar_paquete(paquete):
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
def desinstalar_paquete(current_user, token, paquete):
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
def listar_paquetes(current_user, token):
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
    token_response = login(username, password)
    print(token_response)

    if "Token: " in token_response:
        token = token_response.split("Token: ")[1]
        
        print("\nOpciones:")
        print("1. Instalar paquete")
        print("2. Actualizar paquete")
        print("3. Desinstalar paquete")
        print("4. Listar paquetes")

    opcion = input("Seleccione una opcion (1/2/3/4): ")

    if opcion == "1":
        paquete = input("Introduce el nombre del paquete que deseas instalar: ")
        instalar_paquete(paquete)
    elif opcion == "2":
        paquete = input("Introduce el nombre del paquete que deseas actualizar: ")
        actualizar_paquete(paquete)
    elif opcion == "3":
        paquete = input("Introduce el nombre del paquete que deseas desinstalar: ")
        desinstalar_paquete(current_user=username, token=token, paquete=paquete)

    elif opcion == "4":
        user_token = input("Ingrese su token: ")
        try:
            listar_paquetes(token=user_token)
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Opcion no valida. Por favor, selecciona 1, 2, 3 ó 4.")


if __name__ == "__main__":
    main()