# Usar una imagen base de Python más pequeña
FROM python:3.10-alpine

# Crear un nuevo usuario no root
RUN adduser -D myuser

# Configurar el directorio de trabajo
WORKDIR /app

# Copiar solo el archivo de requerimientos y luego instalar las dependencias en una sola capa
COPY requirements.txt .
RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto
COPY src/ ./src/

# Cambiar al usuario no root
USER myuser

# Comando para ejecutar el script principal
CMD ["python", "src/main.py"]
