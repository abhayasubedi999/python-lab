# Get input of DOB from user and display in form: 2025******JUN*13. [Note: Three stars prior to June as its 6th month. 1 star prior to 13 as its first digit is 1)
from datetime import datetime


def format_dob():
    dob_str = input("Enter your date of birth (YYYY-MM-DD): ")

    try:
        dob = datetime.strptime(dob_str, "%Y-%m-%d")

        year = dob.year
        month = dob.strftime("%b").upper()
        day = dob.day

        formatted = (
            f"{year}" + "*" * 3 + f"{month}" + "*" * (1 if day < 10 else 0) + f"{day}"
        )

        print("Formatted DOB:", formatted)

    except ValueError:
        print("Invalid date format! Please use YYYY-MM-DD")


if __name__ == "__main__":
    print("=== DOB Formatter ===")
    format_dob()
