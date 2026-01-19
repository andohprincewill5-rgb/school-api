from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from ..db import SessionLocal
from ..models import Result
from ..schemas import ResultOut

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_class=HTMLResponse)
def list_results(request: Request, db: Session = Depends(get_db)):
    results = db.query(results).all()
    return templates.TemplateResponse("results.html", {"request": request, "results": results})