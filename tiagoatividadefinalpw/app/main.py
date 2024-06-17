from fastapi import FastAPI, Form, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from models import Book, User

# Criar aplicação FastAPI
app = FastAPI()

# Configurar o banco de dados SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./biblioteca_database.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criar templates Jinja2
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Criar tabelas
Base.metadata.create_all(bind=engine)

# Funções auxiliares
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_user(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

# Rotas
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/register", response_class=HTMLResponse)
async def show_register_form(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/register", response_class=HTMLResponse)
async def register(request: Request, username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    # Verificar se o usuário já existe
    user = get_user(db, username)
    if user:
        raise HTTPException(status_code=400, detail="User already registered")
    
    # Registrar o usuário
    new_user = User(username=username, password=password)
    db.add(new_user)
    db.commit()

    return templates.TemplateResponse("registered.html", {"request": request, "username": username})

@app.get("/login", response_class=HTMLResponse)
async def show_login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login", response_class=HTMLResponse)
async def login(request: Request, username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    # Verificar se o usuário existe e a senha está correta
    user = get_user(db, username)
    if not user or user.password != password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/index", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/add_book", response_class=HTMLResponse)
async def add_book_form(request: Request):
    return templates.TemplateResponse("add_book.html", {"request": request})

@app.post("/add_book", response_class=HTMLResponse)
async def add_book(request: Request, title: str = Form(...), author: str = Form(...), db: Session = Depends(get_db)):
    # Cadastrar livro
    new_book = Book(title=title, author=author)
    db.add(new_book)
    db.commit()
    return templates.TemplateResponse("book_added.html", {"request": request, "title": title, "author": author})

@app.get("/books_added", response_class=HTMLResponse)
async def added_books(request: Request, db: Session = Depends(get_db)):
    # Obter todos os livros adicionados
    books = db.query(Book).all()
    return templates.TemplateResponse("books_added.html", {"request": request, "books": books})

@app.get("/edit_book/{book_id}", response_class=HTMLResponse)
async def edit_book_form(request: Request, book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    return templates.TemplateResponse("edit_book.html", {"request": request, "book": book})

@app.post("/edit_book/{book_id}", response_class=HTMLResponse)
async def edit_book(request: Request, book_id: int, title: str = Form(...), author: str = Form(...), db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    book.title = title
    book.author = author
    db.commit()
    return RedirectResponse(url="/books_added", status_code=303)

@app.get("/delete_book/{book_id}", response_class=HTMLResponse)
async def delete_book(request: Request, book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    db.delete(book)
    db.commit()
    return RedirectResponse(url="/books_added", status_code=303)


# Executar a aplicação com o servidor Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
