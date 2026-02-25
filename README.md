## setup instructions

1. clone the repo  

2. make a virtual environment

3. install dependencies
bash
pip install -r requirements.txt


4. run the server
uvicorn main:app --reload

---

## endpoints

### get all students
GET /students
Returns all students in the db and count

### get students by major
GET /students/by-major
Returns all students with that major and count

### get students by gpa
GET /students/by-gpa
returns students with gpa = min_gpa

### get student by id
GET /students/{student_id}
Returns single student if exists

### create a student
POST /students
Returns student object with new id

### update student
PUT /students/{student_id}
Updates student info if exists, returns updated student

### delete student
DELETE /students/{student_id}
Deletes the student, returns simple message


