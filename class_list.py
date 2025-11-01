# Class List Program

print("Welcome to the Class List Creator!")

# Empty list to store students
class_list = []

# Ask how many students to enter
num_students = int(input("How many students are in your class? "))

# Loop to collect details
for i in range(num_students):
    print("\nEnter details for student", i + 1)
    name = input("Name: ")
    grade = input("Grade: ")
    favorite_subject = input("Favorite subject: ")

    # Store each student's details in a dictionary
    student = {
        "name": name,
        "grade": grade,
        "favorite_subject": favorite_subject
    }

    # Add to class list
    class_list.append(student)

# Print all details
print("\n🎓 Class List 🎓")
print("----------------")
for student in class_list:
    print(f"Name: {student['name']}, Grade: {student['grade']}, Favorite Subject: {student['favorite_subject']}")

print("\nGreat job! You created a class list of", num_students, "students!")

