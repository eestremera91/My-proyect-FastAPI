from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from routers import user, products, store


app = FastAPI()  #instanciamos FastApi
app.title = "Project with FastAPI"
app.version = "1.0"
#routers: esto es para enlazar otras APIs a estas como API principal
@app.get('/', tags=['home'])
async def message():
    return HTMLResponse('<h1>Project with FastAPI</h1')

app.include_router(user.router)
app.include_router(store.router)
app.include_router(products.router)