"""
10. Show the below menu to the user until and until user select quit and display corresponding os message
'''
Menu:
1. windows
2. Linux
3. Mac
4. quit
'''
"""
while 1 :
    print"'''"
    print"Menu:"
    print"1. Windows"
    print"2. Linux"
    print"3.Mac"
    print"4.quit"
    print"'''"
    user_response=raw_input("Enter the name of OS which you want to select")
    if user_response=="1" :
        print"You are in Windows Operating System"
    elif user_response=="2" :
        print"You are in Linux Operating System"
    elif user_response=="3" :
        print"You are in Mac Operating System"
    elif user_response=="4" :
        break
    else :
        print"You entered wrong input, please enter from 1 - 4"
