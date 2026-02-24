from typing import Optional
from pydantic import BaseModel, EmailStr

class Student(BaseModel):
    id: Optional[int] = None
    name: str
    email: EmailStr # Automatic email validation
    major: str
    gpa: float
    enrollment_year: int