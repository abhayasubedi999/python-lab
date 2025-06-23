# Get input of DOB from user and display number of days passed since birth

from datetime import datetime, date


def calculate_days_since_birth():
    dob_str = input("Enter your date of birth (YYYY-MM-DD): ")

    try:
        dob = datetime.strptime(dob_str, "%Y-%m-%d").date()

        today = date.today()

        if dob > today:
            print("Error: Birth date cannot be in the future!")
        else:
            days_passed = (today - dob).days
            print(f"\nYou have lived for {days_passed:,} days since your birth!")

    except ValueError:
        print("Invalid date format! Please enter in YYYY-MM-DD format.")


if __name__ == "__main__":
    print("=== Days Since Birth Calculator ===")
    calculate_days_since_birth()
