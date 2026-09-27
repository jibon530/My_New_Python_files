my_file = open("Student_info.txt",'a')

name = input("Enter your name:")
roll = input("Enter your roll:")
gpa = input("Enter your grade:")

my_file.write("Name:")
my_file.write(name)
my_file.write("\n")
my_file.write("Roll:")
my_file.write(roll)
my_file.write("\n")
my_file.write("GPA:")
my_file.write(gpa)

my_file.close()
my_file = open("Student_info.txt",'r')
print(my_file.read())
my_file.close()