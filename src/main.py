from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from auth.base_config import auth_backend, fastapi_users
from auth.schemas import UserRead, UserCreate, UserUpdate
from alembic import command
# from src.auth.base_config import auth_backend, fastapi_users
# from src.auth.schemas import UserRead, UserCreate, UserUpdate

# from operations.router import router as router_operation
from services.router import router as router_services
# from src.services.router import router as router_services
app = FastAPI(
    title="Trading App"
)

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://techotes.onrender.com",
    "https://client-i54l.onrender.com"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    # allow_methods=["*"],
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["*"],
)


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

# app.include_router(router_operation)
app.include_router(router_services)



def run_migrations_automatically():
    command.upgrade('8ca3d3c445a4')

if __name__ == "__main__":
    run_migrations_automatically()