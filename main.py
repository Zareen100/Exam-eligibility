# Function to check exam eligibility
def check_exam_eligibility(age, attendance_percentage):
    # Conditions for eligibility
    if age >= 18 and attendance_percentage >= 75:
        return "You are eligible to take the exam."
    elif age < 18:
        return "You are not eligible due to age restrictions."
    else:
        return "You are not eligible due to low attendance."

# Input from user
age = int(input("Enter your age: "))
attendance_percentage = float(input("Enter your attendance percentage: "))

# Call the function and print the result
result = check_exam_eligibility(age, attendance_percentage)
print(result)
