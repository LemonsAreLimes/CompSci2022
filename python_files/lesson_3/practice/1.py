def checkGrade(mark=None):
    if mark==None: return False

    if mark >= 80:
        return "A"
    elif mark >= 65 and mark <= 79:
        return "B"
    elif mark >= 50 and mark<=64:
        return "C"
    else:
        return "F"
    
for i in range(0, 100):
    x = checkGrade(i)

    print(f"grade: {i} results to: {x}")
