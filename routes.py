from fastapi import APIRouter, HTTPException
from models import Student
from database import get_connection
router = APIRouter()
@router.get("???") # TODO: Replace ??? with correct endpoint path
def get_all_students():
# TODO: Implement this pass
@router.get("???") # TODO: Replace ??? with correct endpoint path
def get_students_by_major(major: str):
# TODO: Implement this pass
@router.get("???") # TODO: Replace ??? with correct endpoint path
def get_students_by_gpa(min_gpa: float):
# TODO: Implement this pass
@router.get("???") # TODO: Replace ??? with correct endpoint path
def get_student(student_id: int):
# TODO: Implement this pass
@router.post("???", status_code=201) # TODO: Replace ??? with correct endpoint path
def create_student(student: Student):
# TODO: Implement thispass
@router.put("???") # TODO: Replace ??? with correct endpointpath
def update_student(student_id: int, student: Student):
# TODO: Implement this pass
@router.delete("???") # TODO: Replace ??? with correct endpoint path
def delete_student(student_id: int):
# TODO: Implement this pass