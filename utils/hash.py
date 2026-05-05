from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(user_password: str):
    return pwd_context.hash(str(user_password))

def verify_password(user_password, hashed_password):
    return pwd_context.verify(str(user_password), hashed_password)