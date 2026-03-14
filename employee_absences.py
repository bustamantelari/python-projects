# Check employee attendance

# Ask how many absences the employee had
absences = int(input("Enter the number of absences for the employee: "))

# Check the attendance situation
if absences == 0:
    print("Excellent! No absences.")
elif absences <= 15:
    print("Good! Few absences.")
elif absences <= 30:
    print("Warning! Many absences.")
else:
    print("Problem! Excessive absences.")
