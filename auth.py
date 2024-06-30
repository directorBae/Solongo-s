import jwt
import datetime

# 비밀 키 설정
SECRET_KEY = 'secret_solongos_'

def generate_token(user_id):
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),  # 만료 시간 (1일)
        'iat': datetime.datetime.utcnow(),  # 토큰 발행 시간
        'sub': user_id  # 토큰에 포함될 사용자 ID
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

def decode_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'