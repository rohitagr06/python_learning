# 20. Take two numbers from the user a,b check whether a is divisible by b or not?
user_input1=raw_input("Please Enter the number a:")
if user_input1.isdigit() :
    user_input1=int(user_input1)#Converting user input to integer number
else :
    sys.exit("Input should be positive integers only")
user_input2=raw_input("Please Enter the number b:")
if user_input2.isdigit() :
    user_input2=int(user_input2)#Converting user input to integer number
else :
    sys.exit("Input should be positive integers only")
if (user_input1%user_input2)==0 :
    print"%s is divisible by %s"%(user_input1,user_input2)
else :
    print"%s is not divisible by %s"%(user_input1,user_input2)
