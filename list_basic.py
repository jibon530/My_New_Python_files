# vowel = [1,2,1]
# # In = vowel.count("P")
# print(vowel)
# re = list(reversed(vowel))

# print(vowel)
# if vowel == re :
#     print("YES")
# else:
#     print("NO")
# vowel.sort()
# print(vowel)

# numbers = [3,5,6,9,33,51,5,8,44,32,71]
# sum = 0
# for i in numbers:
#     sum += i
#     print(sum)

my_list = [3,5,2,6,2,9,3,7,1,8]
# my_list.sort(reverse = True)
# print(my_list)
# Even_numbers = []
# Odd_numbers = []
# for num in my_list:
#     if num % 2 == 0:
#         Even_numbers.append(num)
#     else:
#         Odd_numbers.append(num)
# print("Even numbers:",Even_numbers)
# print("Odd numbers:", Odd_numbers)
# info = ["a","e","i","o","u"]
# num = str(input())
# for x in info:
#     if num in info: 
#         print("Yes")
#         break
#     else:
#         print("NO")
#         break
vowel = ["a","e","i","o","u"]
name = str(input())
name1 = name.lower()
has_vowel = False
for letter in name1:
    if letter in vowel:
        has_vowel = True
if has_vowel == True:
    print("Yes,",name," It's a bad monster kill it..")
else:
    print("NO,", name," It isn't a good monster don't kill it..")