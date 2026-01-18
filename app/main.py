from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.db import get_db,SessionLocal, Base, engine
from app.models import Assignment
from app import models, schemas
from app.routers import assignments, results, announcements

app = FastAPI()
app.include_router(assignments.router)
app.include_router(results.router)
app.include_router(announcements.router)



@app.get("/")
def read_root():
    return {"message": "welcome to the school portal API"}

@app.get("/assignments")
def list_assignments():
    return {"data": "Here are all assignments"}

@app.get("/results")
def list_results():
    return {"data": "Here are all results"}

@app.get("/announcements")
def list_announcements():
    return {"data": "Here are all announcements"}

@app.get("/assignments")
def list_assignments(db: Session = Depends(get_db)):
    return db.query(Assignment).all()

@app.get("/results")
def list_results(db: Session = Depends(get_db)):
    return db.query(Results).all()

@app.get("/announcements")
def list_announcements(db: Session = Depends(get_db)):
    return db.query(models.Announcement).all()

@app.post("/assignments", response_model=schemas.AssignmentOut)
def create_assignment(assignment:schemas.AssignmentCreate, db: Session = Depends(get_db)):
    db_assignment = models.Assignment(**assignment.dict())
    db.add(db_assignment)
    db.commit()
    db.refresh(db_assignment)
    return db_assignment  

@app.get("/assignments", response_model=list[schemas.AssignmentOut])
def list_assignments(db: Session = Depends(get_db)):
    return db.query(models.Assignment).all()

@app.get("/assignments/{id}", response_model=schemas.AssignmentOut)
def get_assignment(id: int, db: Session = Depends(get_db)):
    return db.query(models.Assignment).filter(models.Assignment.id == id).first()

@app.put("/assignments/{id}", response_model=schemas.AssignmentOut)
def update_assignment(id: int, assignment: schemas.AssignmentCreate, db: Session = Depends(get_db)):
    db_assignment = db.query(models.Assignment).filter(models.Assignment.id == id).first()
    for key, value in assignment.dict().items():
        setattr(db_assignment, key, value)
    db.commit()
    db.refresh(db_assignment)
    return db_assignment

@app.delete("/assignments/{id}")
def delete_assignment(id: int, db: Session = Depends(get_db)):
    db_assignment = db.query(models.Assignment).filter(models.Assignment.id == id).first()
    db.delete(db_assignment)
    db.commit()
    return {"message": "Assignment deleted"}

@app.post("/results", response_model=schemas.ResultOut)
def create_result(result:schemas.ResultCreate, db: Session = Depends(get_db)):
    db_result = models.Result(**result.dict())
    db.add(db_result)
    db.commit()
    db.refresh(result)
    return result  

@app.get("/results", response_model=list[schemas.ResultOut])
def list_results(db: Session = Depends(get_db)):
    return db.query(models.Result).all()

@app.get("/results/{id}", response_model=schemas.ResultOut)
def get_result(id: int, db: Session = Depends(get_db)):
    return db.query(models.Result).filter(models.Result.id == id).first()

@app.put("/results/{id}", response_model=schemas.ResultOut)
def update_result(id: int, result: schemas.ResultCreate, db: Session = Depends(get_db)):
    db_result = db.query(models.Result).filter(models.Result.id == id).first()
    for key, value in result.dict().items():
        setattr(db_result, key, value)
    db.commit()
    db.refresh(db_result)
    return db_result

@app.delete("/results/{id}")
def delete_result(id: int, db: Session = Depends(get_db)):
    db_result = db.query(models.Result).filter(models.Result.id == id).first()
    db.delete(db_result)
    db.commit()
    return {"message": "Result deleted"}

@app.post("/announcements", response_model=schemas.AnnouncementOut)
def create_announcement(announcement:schemas.AnnouncementCreate, db: Session = Depends(get_db)):
    db_announcement = models.Announcement(**announcement.dict())
    db.add(db_announcement)
    db.commit()
    db.refresh(announcement)
    return announcement  

@app.get("/announcements", response_model=list[schemas.AnnouncementOut])
def list_announcements(db: Session = Depends(get_db)):
    return db.query(models.Announcement).all()

@app.get("/announcements/{id}", response_model=schemas.AnnouncementOut)
def get_announcement(id: int, db: Session = Depends(get_db)):
    return db.query(models.Announcement).filter(models.Announcement.id == id).first()

@app.put("/announcements/{id}", response_model=schemas.AnnouncementOut)
def update_announcement(id: int, announcement: schemas.AnnouncementCreate, db: Session = Depends(get_db)):
    db_announcement = db.query(models.Announcement).filter(models.Announcement.id == id).first()
    for key, value in announcement.dict().items():
        setattr(db_announcement, key, value)
    db.commit()
    db.refresh(db_announcement)
    return db_announcement

@app.delete("/announcements/{id}")
def delete_announcement(id: int, db: Session = Depends(get_db)):
    db_announcement = db.query(models.Announcement).filter(models.Announcement.id == id).first()
    db.delete(db_announcement)
    db.commit()
    return {"message": "Announcement deleted"}

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()