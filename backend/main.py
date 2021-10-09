from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base_class import Base

app=FastAPI(title=settings.PROJECT_TITLE,version=settings.PROJECT_VERSION)

def create_tables():
    Base.metadata.create_all(bind=engine)




def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE,version=settings.PROJECT_VERSION)
    create_tables()

    return app

@app.get("/")
def hello_api():
    return {"detail":"hello fam"}

app = start_application()