
students_dict = {}

with open("students.txt", "r") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        parts = line.split(",")
        student_id = parts[0]
        last_name = parts[1]
        first_name = parts[2]
        major = parts[3]
        gpa = float(parts[4])
        students_dict[student_id] = [last_name, first_name, major, gpa]


def search_by_last_name():
    last_name_input = input("Enter last name to search for: ")
    found = False
    for student_id, info in students_dict.items():
        if info[0] == last_name_input:
            print(f"{student_id},{info[0]},{info[1]},{info[2]},{info[3]}")
            found = True
    if not found:
        print("No students found with that last name.")

def search_by_major():
    major_input = input("Enter major to search for: ")
    found = False
    for student_id, info in students_dict.items():
        if info[2] == major_input:
            print(f"{student_id},{info[0]},{info[1]},{info[2]},{info[3]}")
            found = True
    if not found:
        print("No students found with that major.")


while True:
    print("\nChoose an option:")
    print("1) Search by Last Name")
    print("2) Search by Major")
    print("3) Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "3":
        print("Goodbye!")
        break
    elif choice == "1":
        search_by_last_name()
    elif choice == "2":
        search_by_major()
    else:
        print("Invalid choice, please try again.")