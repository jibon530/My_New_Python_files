'''
# List Operation
mylist = ["Jibon", "Moron", 300537]
print(mylist)
mylist[0] = "Sujon"
print(mylist)
mylist.append("Payel")
print(mylist)
mylist.insert(3,"Rahul")
print(mylist)
mylist.remove("Payel")
print(mylist)
del mylist[3]
print(mylist)
'''
# Set Operation
myset1 = {1,2,3,4} 
myset2 = {3,4,5,6}
x = (myset1 - myset2)
print(x)
x = (myset1.difference(myset2))
print(x)
x = (myset1 & myset2)
print(x)
x = (myset1 | myset2)
myset1.add(5)
print(myset1)