from fastapi import APIRouter
from app.routers.auth import auth_router
from app.routers.todo import todo_router

main_router = APIRouter()
main_router.include_router(auth_router)
main_router.include_router(todo_router)