# app/utils.py
from passlib.context import CryptContext

# We use "argon2" because it is more modern and avoids the 
# bcrypt version incompatibility/72-byte limit errors.
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)