from typing import Optional
from fastapi import FastAPI, Request, Form
from sqlalchemy.exc import SQLAlchemyError
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import RedirectResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from src.db.db_config import SessionLocal, engine, Base
from src.exception.global_exception_handler import resource_not_found_exception_handler, sqlalchemy_exception_handler
from src.exception.resource_not_found_exception import ResourceNotFoundException
from src.middleware.auth import Auth
from src.model import Dream, Admin
from src.service.admin_service import AdminService
from src.service.dream_service import DreamService
from src.utils.password import hash_password

app = FastAPI()
app.mount("/static", StaticFiles(directory="src/static"), name="static")

app.add_exception_handler(ResourceNotFoundException, resource_not_found_exception_handler)
app.add_exception_handler(SQLAlchemyError, sqlalchemy_exception_handler)

app.add_middleware(Auth)
app.add_middleware(SessionMiddleware, secret_key="My Secret Key")

templates = Jinja2Templates(directory="src/templates")

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/")
async def home_page(request: Request):
    return templates.TemplateResponse(request, "index.html", {"request": request})

@app.get("/create-dream")
async def create_dream_page(request: Request, message: Optional[str] = None):
    return templates.TemplateResponse(request, "create-dream.html", {"request": request, "message": message})

@app.post("/create-dream")
async def create_dream(request: Request,
                        title: str = Form(...),
                        description: Optional[str] = Form(None),
                        mood: str = Form(...)):
    async with SessionLocal.begin() as session:
        dream = Dream(title=title, description=description, mood=mood)
        dream_service = DreamService(session)
        dream = await dream_service.save(dream)
        return RedirectResponse("/create-dream?message=Dream saved successfully..", status_code=303)

@app.get("/dream-list")
async def get_dream_list(request: Request, message: Optional[str] = None):
    async with SessionLocal() as session:
        dream_service = DreamService(session)
        dream_list = await dream_service.get_all_dreams()
        return templates.TemplateResponse(request, "dream-list.html",
                                           {"request": request, "dream_list": dream_list, "message": message})

@app.get("/delete-dream/{id}")
async def delete_dream(request: Request, id: int):
    async with SessionLocal.begin() as session:
        dream_service = DreamService(session)
        await dream_service.delete_dream(id)
        return RedirectResponse("/dream-list?message=Dream deleted successfully", status_code=303)

@app.get("/update-dream/{id}")
async def update_dream_page(request: Request, id: int):
    async with SessionLocal() as session:
        dream_service = DreamService(session)
        dream = await dream_service.get_dream_by_id(id)
        return templates.TemplateResponse(request, "update_dream.html", {"request": request, "dream": dream})

@app.post("/update-dream")
async def update_dream(request: Request, id: int = Form(...),
                        title: str = Form(...),
                        mood: str = Form(...),
                        description: str = Form(...)):
    async with SessionLocal.begin() as session:
        dream_service = DreamService(session)
        dream = Dream(id=id, title=title, description=description, mood=mood)
        await dream_service.update_dream(dream)
        return RedirectResponse("/dream-list", status_code=303)

@app.get("/signup")
async def signup_page(request: Request):
    return templates.TemplateResponse(request, "signup.html", {"request": request})

@app.post("/signup")
async def signup(request: Request, email: str = Form(...),
                  password: str = Form(...)):
    async with SessionLocal.begin() as session:
        admin = Admin(email=email, password=hash_password(password))
        admin_service = AdminService(session)
        await admin_service.save(admin)
        return RedirectResponse("/signin", status_code=303)

@app.get("/signin")
async def signin_page(request: Request):
    return templates.TemplateResponse(request, "signin.html", {"request": request})

@app.post("/signin")
async def signin(request: Request, email: str = Form(...), password: str = Form(...)):
    async with SessionLocal() as session:
        admin = Admin(email=email, password=password)
        admin_service = AdminService(session)
        status = await admin_service.authenticate(admin)
        if status:
            request.session["is_logged_in"] = True
            request.session["current_user_email"] = email
            return RedirectResponse("/", status_code=303)
        else:
            return RedirectResponse("/signin", status_code=303)

@app.get("/signout")
async def signout(request: Request):
    request.session.clear()
    return RedirectResponse("/", status_code=303)
