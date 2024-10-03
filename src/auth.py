import jwt
import datetime
import os

SECRET_KEY = "secret_key"

# Funcion para login
def login(username, password):
    if username == 'admin' and password == 'admin':
        token = jwt.encode({
            'user_id': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, SECRET_KEY, algorithm="HS256")
        return {'Token': token}
    return {'Error': 'Credenciales incorrectas'}

# Funcion para generar un token
def generate_token(user_id):
    token = jwt.encode({
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    }, SECRET_KEY, algorithm="HS256")
    return token



# Decorador para proteger funciones con autenticacion
def token_required(f):
    def decorated(*args, **kwargs):
        # Leer el token desde un archivo
        token = get_stored_token()

        if not token:
            print("Token faltante. Por favor inicie sesión.")
            return "Token faltante."
        
        try:
            # Decodificar el token
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            current_user = data['user_id']
        except jwt.ExpiredSignatureError:
            print("El token ha expirado.")
            return "El token ha expirado."
        except jwt.InvalidTokenError:
            print("Token inválido.")
            return "Token inválido."
        
        # Llamar a la funcion original pasando el usuario actual
        return f(current_user, *args, **kwargs)

    return decorated

# Funcion para almacenar el token en un archivo
def store_token(token):
    with open("token.txt", "w") as token_file:
        token_file.write(token)

# Funcion para obtener el token almacenado
def get_stored_token():
    if os.path.exists("token.txt"):
        with open("token.txt", "r") as token_file:
            return token_file.read()
    return None

# Funcion para eliminar el token
def clear_token():
    if os.path.exists("token.txt"):
        os.remove("token.txt")