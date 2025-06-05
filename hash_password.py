from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def encode_password(password: str) -> str:
    return password_context.hash(password)

def very_encoded_password(password: str, hash_password: str) -> bool:
    return password_context.verify(password, hash_password)

