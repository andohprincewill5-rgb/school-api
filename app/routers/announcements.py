from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db import SessionLocal
from ..models import Announcement
from ..schemas import AnnouncementOut

router = APIRouter()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

@router.get("/", response_model=list[AnnouncementOut])
def list_announcements(db: Session = Depends(get_db)):
  return db.query(Announcement).all()