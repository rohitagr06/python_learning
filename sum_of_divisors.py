# 22. Find the sum of all the divisors of 3 or 5 below user input
user_input=raw_input("Please Enter the number :")
if user_input.isdigit() :
    user_input=int(user_input)#Converting user input to integer number
else :
    sys.exit("Input should be positive integers only")
if user_input != 0 :
    result=0
    for iteration in range(1,user_input) :
        if ((iteration%3)==0) or ((iteration%5)==0) :
            result = result+iteration
    print"Sum of all the divisors of 3 or 5 below %s is %s"%(user_input,result)
else :
    print"Input should be non zero"      
