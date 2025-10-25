from fastapi import APIRouter, HTTPException
from schemas.Users import UserCreate, UserResponse
from fastapi_utils.cbv import cbv

router = APIRouter(prefix="/users",tags=["users"])

# Simula um "banco" na memória
fake_users_db = {}


class UserAPI:
    @router.post("/", response_model=UserResponse)
    def create_user(user: UserCreate):
        try:
            if user.email in fake_users_db:
                raise HTTPException(status_code=400, detail="Email já cadastrado")
            fake_users_db[user.email] = user
            return user
        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail="Erro interno")


    @router.get("/{email}", response_model=UserResponse)
    def get_user(email: str):
        user = fake_users_db.get(email)
        if not user:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        return user
