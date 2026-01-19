from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from ..db import SessionLocal
from ..models import Assignment
from ..schemas import AssignmentOut

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_class=HTMLResponse)
def list_assignments(request: Request, db: Session = Depends(get_db)):
    assignments = db.query(Assignment).all()
    return templates.TemplateResponse("assignments.html", {"request": request, "assignments": assignments})