# Print the first 100 odd numbers
import sys
user_input=raw_input("Please Enter total number of people:")
if user_input.isdigit() :
    user_input=int(user_input)#Converting user input to integer number
else :
    sys.exit("Input should be in integers")
count=0
while count<100 :
    if (user_input%2) != 0:
        count=count+1
        print "%s odd no. is: %s"%(count,user_input)
        user_input=user_input+2
    else :
        user_input=user_input+1
