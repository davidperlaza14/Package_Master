import os
import jwt
import datetime
from functools import wraps

SECRET_KEY = os.getenv('SECRET_KEY', '000666')

# Funcion para generar un token
def generate_token(user_id):
    token = jwt.encode({
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
    }, SECRET_KEY, algorithm="HS256")
    return token

# Decorador para proteger funciones con autenticacion
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = kwargs.get('token')
        if not token:
            raise Exception("Token is missing!")
        
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            current_user = data['user_id']
        except jwt.ExpiredSignatureError:
            raise Exception("Token has expired!")
        except jwt.InvalidTokenError:
            raise Exception("Token is invalid!")
        
        return f(current_user, *args, **kwargs)
    
    return decorated