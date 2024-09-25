#!/bin/bash

# Verificar si se ha proporcionado un paquete
if [ -z "$1" ]; then
    echo "Por favor, proporciona el nombre del paquete a instalar."
    exit 1
fi

# Activar el entorno virtual
source env/bin/activate

# Instalar el paquete
pip install "$1"

echo "Paquete '$1' instalado."
