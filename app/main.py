from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.responses import HTMLResponse
app=FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"),name = "static")
@app.get("/", response_class=HTMLResponse)
async def read_root(req:Request):
    return templates.TemplateResponse("home.html",{"request":req})

@app.get("/about", response_class=HTMLResponse)
async def read_root(req:Request):
    return templates.TemplateResponse("aboutUs.html",{"request":req})

@app.get("/maps", response_class=HTMLResponse)
async def read_root(req:Request):
    return templates.TemplateResponse("maps.html",{"request":req})


@app.get("/IOT", response_class=HTMLResponse)
async def read_root(req:Request):
    return templates.TemplateResponse("IOT.html",{"request":req})

@app.get("/addDevice", response_class=HTMLResponse)
async def read_root(req:Request):
    return templates.TemplateResponse("addDevice.html",{"request":req})


@app.get("/addFarm", response_class=HTMLResponse)
async def read_root(req:Request):
    return templates.TemplateResponse("addFarm.html",{"request":req})

@app.get("/addProduces", response_class=HTMLResponse)
async def read_root(req:Request):
    return templates.TemplateResponse("addProduces.html",{"request":req})

@app.get("/addUser", response_class=HTMLResponse)
async def read_root(req:Request):
    return templates.TemplateResponse("addUser.html",{"request":req})
