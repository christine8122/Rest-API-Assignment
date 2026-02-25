from fastapi import APIRouter, HTTPException
from models import Student
from database import get_connection
from database import dict_from_row

router = APIRouter()

@router.get("/students")
def get_all_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()

    students = []

    for row in rows:
        student = dict_from_row(row)
        students.append(student)

    return {
        "students": students,
        "count": len(students)
}


@router.get("/students/by-major")
def get_students_by_major(major: str):
    if not major or not major.strip():
        raise HTTPException(status_code=400, detail="Major cannot be found")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE major = ?", (major,))
    rows = cursor.fetchall()
    conn.close()

    students = []
    for row in rows:
        student = dict_from_row(row)
        students.append(student)
    return {
        "students": students,
        "count": len(students),
        "major": major
    }

@router.get("/students/by-gpa")
def get_students_by_gpa(min_gpa: float):
    if min_gpa < 0.0 or min_gpa > 4.0:
        raise HTTPException(status_code=400, detail="GPA must be between 0.0 and 4.0")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE gpa = ?", (min_gpa,))
    rows = cursor.fetchall()
    conn.close()
    
    students = []
    for row in rows:
        student = dict_from_row(row)
        students.append(student)
    return {
        "students": students,
        "count": len(students),
        "gpa": min_gpa
    }
    
@router.get("/students/{student_id}") 
def get_student(student_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    row = cursor.fetchone()
    conn.close()
    
    if not row:
        raise HTTPException(status_code=404, detail=f"Student with ID {student_id} not found")
    return dict_from_row(row)

@router.post("/students", status_code=201)
def create_student(student: Student):
    if not student.name or not student.name.strip():
        raise HTTPException(status_code=400, detail="Name cannot be null")
    if not student.major or not student.major.strip():
        raise HTTPException(status_code=400, detail="Major cannot be null")
    if student.gpa < 0.0 or student.gpa > 4.0:
        raise HTTPException(status_code=400, detail="GPA must be between 0.0 and 4.0")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, email, major, gpa, enrollment_year) VALUES (?, ?, ?, ?, ?)",(student.name, student.email, student.major, student.gpa, student.enrollment_year))

    student_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return {
        "id": student_id,
        "name": student.name,
        "email": student.email,
        "major": student.major,
        "gpa": student.gpa,
        "enrollment_year": student.enrollment_year
    }
    
@router.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    if not student.name or not student.name.strip():
        raise HTTPException(status_code=400, detail="Name cannot be null")
    if not student.major or not student.major.strip():
        raise HTTPException(status_code=400, detail="Major cannot be null")
    if student.gpa < 0.0 or student.gpa > 4.0:
        raise HTTPException(status_code=400, detail="GPA must be between 0.0 and 4.0")
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    if not cursor.fetchone():
        conn.close()
        raise HTTPException(status_code=404, detail=f"Student with ID {student_id} not found")
    
    cursor.execute( "UPDATE students SET name= ?, email= ?, major= ?, gpa= ?, enrollment_year= ? WHERE id=?", (student.name, student.email, student.major, student.gpa, student.enrollment_year, student_id))
    conn.commit()
    conn.close()
    
    student_data = student.dict()
    student_data["id"] = student_id

    return student_data


@router.delete("/students/{student_id}") 
def delete_student(student_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    if not cursor.fetchone():
        conn.close()
        raise HTTPException(status_code=404, detail=f"Student with ID {student_id} not found")
    
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()
    return {"message": "Student deleted successfully"}
