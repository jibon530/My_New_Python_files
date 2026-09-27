# v_list = ["a","e","i","o","u"]
# print(v_list)
# num = str(input().lower())
# if num in v_list:
#     print("Yes")
# else:
#     print("No")
vowels = ["a","e","i","o","u"]
name = input("Enter:").lower()
found = False
for ch in name:
    if ch in vowels:
        found = True
        break
if found:
    print("Yes")
else:
    print("No")