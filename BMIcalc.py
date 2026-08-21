weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

def calculate_bmi(weight, height):
    """Return BMI from weight in kg and height in metres."""
    return weight / (height ** 2)

def bmi_category(bmi):
    """Return the category name for a BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

print(f"You are classified as: {bmi_category(calculate_bmi(weight, height))}")