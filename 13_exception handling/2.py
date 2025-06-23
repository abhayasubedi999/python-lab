# Create a function that calculates the age of user on passing DOB. [Hint: You can get current date from datetime library, use AI tool for detail]. Note: You need to raise Exception if DOB is in invalid format, if DOB is in future. Return value of age has to be integer number

from datetime import datetime, date


def calculate_age(dob):
    """
    Calculate age based on date of birth (DOB).

    Args:
        dob (str): Date of birth in 'YYYY-MM-DD' format

    Returns:
        int: Age in years

    Raises:
        ValueError: If DOB is in invalid format or future date
    """
    try:
        # Parse the input string into a date object
        birth_date = datetime.strptime(dob, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD' format.")

    today = date.today()

    # Check if DOB is in the future
    if birth_date > today:
        raise ValueError("Date of birth cannot be in the future.")

    # Calculate age
    age = today.year - birth_date.year

    # Adjust if birthday hasn't occurred yet this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    return age


# Example usage:
try:
    age = input("Enter your date of birth (YYYY-MM-DD): ")
    print(calculate_age(f"Age: {age} years"))
except ValueError as e:
    print(f"Error: {e}")
