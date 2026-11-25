# Unit-4B Task-7: Robust Input Validation

class InvalidMarksError(Exception):
    pass

try:
    marks = float(input("Enter marks (0-100): "))

    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100!")

    if marks >= 40:
        print("Result: Pass")
    else:
        print("Result: Fail")

except InvalidMarksError as e:
    print("Error:", e)

except ValueError:
    print("Error: Please enter a valid number!")

finally:
    print("Validation completed")
