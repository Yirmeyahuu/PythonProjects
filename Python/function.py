# This program uses a function to collect and display basic student information.

def get_student_info():
    """
    This function prompts the user for a student's information and returns
    a dictionary containing the details.
    """
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
    
    # Return the dictionary with all the collected information
    return student_profile


# Main part of the program
enter_again = 'yes'
while enter_again.lower() == 'yes':
    # Call the function to get the student's profile
    current_student = get_student_info()

    print("\n--- Student Profile ---")
    print(f"Name:       {current_student['name']}")
    print(f"Age:        {current_student['age']}")
    print(f"Program:    {current_student['program']}")
    print(f"Year Level: {current_student['year_level']}")
    print(f"School:     {current_student['school']}")

    # Ask the user if they want to enter another student's information.
    enter_again = input("\nDo you want to enter another student? (yes/no): ")


print("\nThank you for using the program!")