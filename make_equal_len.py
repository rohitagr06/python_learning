"""
28. WAP> 10 -> 000010
       100 ->  000100
      1000 ->  001000
  2345678  ->  2345678
"""
user_input=raw_input("Please Enter the number :")
if user_input.isdigit() :
    len_user_input=len(user_input)
    if len_user_input==1 :
        result="000000"+user_input
        print"%s -> %s"%(user_input,result)
    elif len_user_input==2 :
        result="00000"+user_input
        print"%s -> %s"%(user_input,result)
    elif len_user_input==3 :
        result="0000"+user_input
        print"%s -> %s"%(user_input,result)
    elif len_user_input==4 :
        result="000"+user_input
        print"%s -> %s"%(user_input,result)
    elif len_user_input==5 :
        result="00"+user_input
        print"%s -> %s"%(user_input,result)
    elif len_user_input==6 :
        result="0"+user_input
        print"%s -> %s"%(user_input,result)
    elif len_user_input==7 :
        print"%s -> %s"%(user_input,user_input)
    else :
        print"Input integer length must be from 1 to 7 only" 
else :
    sys.exit("Input should be positive integers only")
