from core.manager import add_student
from models.student import create_student

# LOAD
with open("data/database.json", "r") as f:
    students = json.load(f)

# MODIFY
del students[0]

# SAVE
with open("data/database.json", "w") as f:
    json.dump(students, f)
