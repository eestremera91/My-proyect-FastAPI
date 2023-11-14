from fastapi import FastAPI
from fastapi.responses import HTMLResponse



app = FastAPI()  #instanciamos FastApi
app.title = "Project with FastAPI"
app.version = "1.0"
#routers: esto es para enlazar otras APIs a estas como API principal
@app.get('/', tags=['home'])
async def message():
    return HTMLResponse('<h1>Project with FastAPI</h1')

