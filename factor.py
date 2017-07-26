# 18. Determine the factors of a number entered  by the user
import sys
user_input=raw_input("Please Enter total number of people:")
if user_input.isdigit() :
    user_input=int(user_input)#Converting user input to integer number
else :
    sys.exit("Input should be positive integers only")
if user_input != 0 :
    divisor=2
    print"Factor of Entered number %s is 1*%s"%(user_input,user_input)
    while divisor <= ((user_input/2)+1) :
        if (user_input%divisor)==0 :
            temp_number=user_input/divisor
            print"Factor of Entered number %s is %s*%s"%(user_input,divisor,int(temp_number))
            divisor=divisor+1
        else :
            divisor=divisor+1
else :
    print"Please enter the number except 0"
