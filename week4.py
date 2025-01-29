'''
 >= , >
 <=,  <
 ==
 and 
 or
 not

if (condition):
    condition true code run
else:
    condition false code run

if (condition 1):
    condition 1 true code run
elif(condition 2):
    condition 2 true code run
else:
    condition 1 and condition 2 false code run
'''

#convert numberical grade to a letter
grade = int(input("What is your grade:"))

if grade > 90:
    print("grade A")
elif grade > 80:
    print("grade B")
elif (grade > 70):
    print("grade +C")
elif (grade > 60):
    print("grade C ")
elif (grade > 50):
    print("grade +D")
elif (grade > 40):
    print("grade D")
elif (grade > 30):
    print("grade E")
elif( grade <= 30):
    print("grade F")
else:
    print("N/A")

age = int(input("Enter your age: "))
status = input("Did you pass high school: (yes/no)").lower()

if (age >= 16 or status == "yes" ):
    #code that happen if the condition is true
    print("You can attend college")

else:
    #will happen when the condition is false
    print("You cannot attend college")
