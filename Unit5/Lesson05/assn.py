grade_str = input("what is your grade?")
grade = int(grade_str)

if grade >= 9 and grade <= 12:
    print("You are a high schooler.")
if grade >= 6 and grade <= 8:
    print ("You are a middle schooler.")
if grade >= 1 and grade <= 5:
    print ("you are a elementry schooler.") 
if grade >= 13:
    print ("you are not in school.")