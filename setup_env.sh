#!/bin/bash

# Nombre del entorno virtual
ENV_NAME="env"

# Verificar si el entorno virtual ya existe
if [ -d "$ENV_NAME" ]; then
    echo  "El entorno virtual ya existe."
else
    echo "Creando un entorno virtual..."
    python3 -m venv $ENV_NAME
    echo "Entorno virtual creado."

fi

# Activar el entorno  virtual
source $ENV_NAME/bin/activate

# Instalar dependencias
echo "Instalando dependencias..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Entorno virtual configurado y dependencias instaladas."
