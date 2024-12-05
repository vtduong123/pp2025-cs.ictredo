def input_number_of_units(entity):
    """Function to input the number of units (e.g., students, courses)."""
    while True:
        try:
            count = int(input(f"Enter the number of {entity}: "))
            if count > 0:
                return count
            else:
                print("The number must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def input_student_info():
    """Function to input student information."""
    student = {
        'id': input("Enter Student ID: "),
        'name': input("Enter Student Name: "),
        'DoB': input("Enter Student Date of Birth (DoB): "),
        'marks': {}
    }
    return student