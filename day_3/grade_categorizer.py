# Grade Categorizer which takes marks as the input and prints the grade of the student
marks = float(input("Enter the marks of a student: "))
if(marks >= 90):
    print("Grade A")
elif 80 >= marks <90:
    print("Grade B")
elif 70 >= marks <80:
    print("Grade C")
elif 60 >= marks <70:
    print("Grade D")
elif 50 >= marks <60:
    print("Grade E")
elif marks < 0:
    print("Marks cannot be negative")
else:
    print("Invalid marks")




