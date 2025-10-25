from fastapi import FastAPI
# routes
from routes.Users import router as users


# setting
app = FastAPI(title="FastAPI Project", version="1.0.0")

# includes routes
app.include_router(users)


# default root
@app.get("/")
def read_root():
    return {"message": "Hello World"}
