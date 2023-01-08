from datetime import date
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class JobBase(BaseModel):
    title: Optional[str] = None
    company: Optional[str] = None
    company_url: Optional[str] = None
    location: Optional[str] = "Remote"
    description: Optional[str] = None
    date_posted: Optional[date] = datetime.now().date()
    is_active: Optional[bool] = True


class JobCreate(JobBase):
    title: str
    company: str
    location: str
    description: str


class ShowJob(JobBase):
    title: str
    company: str
    company_url: Optional[str]
    location: str
    date_posted: date
    description: Optional[str]
    is_active: bool

    class Config:
        orm_mode = True
