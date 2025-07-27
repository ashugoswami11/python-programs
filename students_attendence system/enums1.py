#practice program for enum :-- student attendance marking system
"""agenda :-- to create an attendance system using enumerators,
              A program which contains a list of student iterate
              those student names along with their role number
              and ask student are they present or not and later print all of the list with this information

1. we have list of student
2. we have to show every student name along with roll number
3. ask user whether is he absent or present
4. update student names and absent present remarks in the dictionary{"student name" : "absent or present"}
5.later print that whole dictionary inside a loop and iterate every dict.items() of dictionary
"""


list_students = ["ashu","riya","ankit","alex","kevin","suraj","nitin"]

enum_list_student = list(enumerate(list_students, start=1)) #start means from which number starting assign values
remark_dict = {}

present_student = 0
absent_student = 0

for index, student in enum_list_student:
    print("enter 'p' for present and 'A' for absent:")
    print(f"roll no.{index}: {student}")
    while True:
        user_input = input().upper()
        if user_input == "P":
            remark_dict.update({student: "present"})
            present_student += 1
            break
        elif user_input == "A":
            remark_dict.update({student: "absent"})
            absent_student += 1
            break
        else:
             print("wrong input please enter 'P' or 'A' for:", student)


print()
for key,value in remark_dict.items():  #  '.items()' is used to retrieve items of the list : this is a whole item=  {"key":"value"}
    print(f"{key} is {value}")

print("\ntotal student present:" ,present_student)
print("total student absent :" ,absent_student)



