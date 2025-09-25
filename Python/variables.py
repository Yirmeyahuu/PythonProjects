# This program collects and displays basic student information.

# We'll use a loop to allow the user to enter multiple students.
# The loop will continue as long as the 'enter_again' variable is 'yes'.
enter_again = 'yes'
while enter_again.lower() == 'yes':
    # A dictionary is a great way to store related pieces of information.
    student_profile = {}

    print("\n--- Enter Student Information ---")

    # Get the student's name (string)
    student_profile['name'] = input("Enter student's name: ")

    # Get the student's age (integer)
    # Use a try-except block to handle invalid input (e.g., text instead of a number).
    try:
        student_profile['age'] = int(input("Enter student's age: "))
    except ValueError:
        student_profile['age'] = "Invalid age"  # Set a default message on error

    # Get the student's program (string)
    student_profile['program'] = input("Enter student's program: ")

    # Get the student's year level (integer)
    try:
        student_profile['year_level'] = int(input("Enter student's year level: "))
    except ValueError:
        student_profile['year_level'] = "Invalid year level"

    # Get the student's school (string)
    student_profile['school'] = input("Enter student's school: ")


    print("\n--- Student Profile ---")
    print(f"Name:       {student_profile['name']}")
    print(f"Age:        {student_profile['age']}")
    print(f"Program:    {student_profile['program']}")
    print(f"Year Level: {student_profile['year_level']}")
    print(f"School:     {student_profile['school']}")

    # Ask the user if they want to enter another student's information.
    enter_again = input("\nDo you want to enter another student? (yes/no): ")


print("\nThank you for using the program!")