from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Assignment(Base):
    __tablename__ = "assignments"   # <-- must be indented inside the class

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    due_date = Column(DateTime, nullable=False)


class Announcement(Base):
    __tablename__ = "announcements"   # <-- indented

    id = Column(Integer, primary_key=True, index=True)
    message = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False)


class Result(Base):
    __tablename__ = "results"   # <-- indented

    id = Column(Integer, primary_key=True, index=True)
    student_name = Column(String(255), nullable=False)
    subject = Column(String(255), nullable=False)
    score = Column(Integer, nullable=False)