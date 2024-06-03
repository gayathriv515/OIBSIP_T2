def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 24.9:
        return "Normal Weight"
    elif bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
        weight = float(input("Enter weight in kilograms: "))
        height = float(input("Enter height in meters: "))

        if weight <= 0 or height <= 0:
            print("Invalid Weight and height must be greater than zero.")
        else:
            bmi = calculate_bmi(weight, height)
            category = classify_bmi(bmi)

            print(f"Your BMI is: {bmi:.2f}")
            print("Category:", category)

main()
