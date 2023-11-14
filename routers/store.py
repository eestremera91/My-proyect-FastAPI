from fastapi import APIRouter


router = APIRouter(prefix = "/store", # esto incluye el prefix en la URL   users
                   tags=["store"], responses={404: {"message": "No encontrado"}})