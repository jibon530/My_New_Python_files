def student(name, age=18, *subjects):
    
    print("Name:", name)
    print("Age:", age)
    print("Subjects:", subjects)

student("Jibon", 19, "Math", "Physics", "Python", "DSA")

def student(name, age=18, **marks):
    
    print("Name:", name)
    print("Age:", age)
    print("Marks:", marks)

student("Jibon", 19, Math = 81, Physics = 89, Python = 59, DSA = 58)
