from fastapi import APIRouter


router = APIRouter(prefix = "/user", # esto incluye el prefix en la URL   users
                   tags=["user"], responses={404: {"message": "No encontrado"}})