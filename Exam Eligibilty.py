attendance=int(input("enter the attendance of the student:"))
medicalcase=str(input("Are you really sick:"))
if medicalcase =="yes":
    print("you are allowed")
else:
    print("you arent allowed")

    if attendance <75:
        print("not allowed")
    else:
        print("allowed")