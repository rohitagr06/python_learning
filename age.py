# 21. Given an age, figure out whether someone's a baby, toddler, child, teenager, adult or old codger.
age=raw_input("Please Enter the age:")
if age.isdigit() :
    age=int(age)#Converting user input to integer number
else :
    sys.exit("Input should be in positive integers only")
if age != 0 :
    if age < 5 :
        print"User is a Baby"
    elif age < 10 :
        print"User is a toddler"
    elif age < 18 :
        print"User is a Child"
    elif age < 21 :
        print"User is a Teenager"
    elif age < 55 :
        print"User is a Adult"
    else :
        print"User is a Old Codger"
else :
    print"Age should be non zero"
