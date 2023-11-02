# str1 = input("Enter string:")
# print(str1.upper())
# print(str1.lower())
# print(str1.title())
# str2 = input("Enter string:")
# str3 = str1 + str2
# print(str3)

# list1 = ["a","b","c","d"]
# elem = input("Enter an element:")
# list1.insert(1,elem)
# print(list1)

##Intersection between two sets##

# set1 = {1,4,6,7}
# set2 = {2,3,4,1}
# set3 =set()
# intersection = set1.intersection(set2)
# print(intersection)
# print(type(set3))


studentInfo = {}

for key in ["name", "rollno", "class", "schoolname"]:
    studentInfo[key] = input(f"Enter {key} : ")

for key, value in studentInfo.items():
    print(key,value)


index = 0 
for elem in list(studentInfo.keys()):
    if index == 1:
        del studentInfo[elem]
    index += 1

print(studentInfo)