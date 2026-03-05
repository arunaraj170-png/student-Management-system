students = []

while True:
    name = input("Enter student name (or exit): ")
    
    if name == "exit":
        break
        
    students.append(name)

print("Student List:", students)
