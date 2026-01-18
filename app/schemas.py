from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AssignmentBase(BaseModel):
    title: str
    class_name: str
    due_date: datetime
    description: str 
    file_path: str | None 

class AssignmentCreate(BaseModel):
        pass

class AssignmentOut(BaseModel):
    id: int
class Config: from_attributes = True

class AnnouncementBase(BaseModel):
    title: str
    description: str
    due_date: datetime
    body: str
class AnnouncementCreate(BaseModel):
        pass

class AnnouncementOut(BaseModel):
    id: int

class Config: from_attributes = True

class ResultBase(BaseModel):
    student_id: str
    term: str
    subject: str
    score: int
    grade: str
class ResultCreate(BaseModel):
        pass

class ResultOut(BaseModel):
    id: int

class Config: from_attributes = True