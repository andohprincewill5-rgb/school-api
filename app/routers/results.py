from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db import SessionLocal
from ..models import Result
from ..schemas import ResultOut

router = APIRouter()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

@router.get("/", response_model=list[ResultOut])
def list_results(student_id: str, term: str, db: Session = Depends(get_db)):
  return db.query(Result).filter(Result.student_id == student_id, Result.term == term).all()