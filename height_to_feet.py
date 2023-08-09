def cm_to_feet_and_inches(cm):
    feet = cm / 30.48
    inches = (feet - int(feet)) * 12
    feet = int(feet)
    return feet, inches

try:
    cm = float(input("Enter length in centimeters: "))
    if cm < 0:
        raise ValueError("Please enter a non-negative value.")
    
    feet, inches = cm_to_feet_and_inches(cm)
    print("Length in feet and inches: {} feet {} inches".format(feet, inches))

except ValueError as e:
    print("Error:", e)
