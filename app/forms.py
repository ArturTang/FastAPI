from pydantic import BaseModel

class UserLoginForm():
    email: str
    password: str