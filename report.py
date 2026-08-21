Name = input("Enter student name: ")
Mark = float(input("Enter marks (0-100): "))

if not Name:
    print("Error: name required")
else:
    if Mark >= 80:
        print(f"{Name}: {Mark:.2f} marks, Grade A - Pass")
    elif Mark >= 60:
        print(f"{Name}: {Mark:.2f} marks, Grade B - Pass")
    elif Mark >= 40:
        print(f"{Name}: {Mark:.2f} marks, Grade C - Pass")
    else:
        print(f"{Name}: {Mark:.2f} marks, Grade D - Fail")
