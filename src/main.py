import os
import subprocess
from sqlalchemy import create_engine

# Obtener la URL de la base de datos desde las variables de entorno
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///default.db')

# Crear una conexión a la base de datos
engine = create_engine(DATABASE_URL)

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
        print(f"Error al intentar actualizar el paquete '{paquete}': {e.stderr}")

def desinstalar_paquete(paquete):
    try:
        resultado = subprocess.run(
            ['pip', 'uninstall', '-y', paquete],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
            
        )
        print(f"Paquete '{paquete}' disinstalado correctamente.")
        print(resultado.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error al intentar desinstalar el paquete '{paquete}': {e.stderr}")

def listar_paquetes():
    try:
        resultado = subprocess.run(
            ['pip', 'list' ],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(f"Lista de paquetes instalados {resultado.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error al intentar listar paquetes {e.stderr}")



def main():
    print("¡Bienvenido al sistema de gestion de paqueteria!")
    print("Opciones:")
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
        desinstalar_paquete(paquete)
    elif opcion == "4":
        listar_paquetes()
    else:
        print("Opcion no valida. Por favor, selecciona 1, 2, 3 ó 4.")


if __name__ == "__main__":
    main()