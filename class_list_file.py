# Class List Program with File Saving

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

    student = {
        "name": name,
        "grade": grade,
        "favorite_subject": favorite_subject
    }

    class_list.append(student)

# Display the collected class list
print("\n🎓 Class List 🎓")
print("----------------")
for student in class_list:
    print(f"Name: {student['name']}, Grade: {student['grade']}, Favorite Subject: {student['favorite_subject']}")

# Save the list to a file
with open("class_list.txt", "w") as file:
    file.write("🎓 Class List 🎓\n")
    file.write("----------------\n")
    for student in class_list:
        file.write(f"Name: {student['name']}, Grade: {student['grade']}, Favorite Subject: {student['favorite_subject']}\n")
    file.write(f"\nTotal students: {num_students}\n")
    file.write("Created with the Class List Creator 🐍\n")

print("\n✅ Your class list has been saved to 'class_list.txt'!")

