from pydantic import BaseModel, EmailStr, field_validator

class UserBase(BaseModel):
    cpf: str
    name: str
    email: EmailStr
    
    field_validator('cpf')
    def validate_cpf(cls, v):
        if len(v) != 11:
            raise ValueError('CPF incorreto, deve ter 11 dígitos')
        pass
        

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    pass
