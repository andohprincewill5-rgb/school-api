from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session
from ..db import SessionLocal
from ..models import Assignment
from ..schemas import AssignmentOut
from datetime import date
import os

router = APIRouter()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

@router.get("/", response_model=list[AssignmentOut])
def list_assignments(db: Session = Depends(get_db)):
  return db.query(Assignment).all()

@router.post("/", response_model=AssignmentOut)
def create_assignment(
    title: str = Form(...),
    class_name: str = Form(...),
    due_date: date = Form(...),
    file: UploadFile | None = File(None),
    db: Session = Depends(get_db)
):
  file_path = None
  if file:
    os.makedirs("app/storage", exist_ok=True)
    file_path = os.path.join("app/storage", file.filename)
    with open(file_path, "wb") as f:
      f.write(file.file.read())
  a = Assignment(title=title, class_name=class_name, due_date=due_date, file_path=file_path)
  db.add(a); db.commit(); db.refresh(a)
  return a