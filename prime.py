def is_prime(number) :
    i=2
    while i<number :
        if number % i ==0 :
            break
        i=i+1
    if i==number :
        return True
    else :
        return False

input1=int(raw_input("Enter starting number"))
input2=int(raw_input("Enetr limit number"))

if input1<input2 :
    i=input1
    while i<=input2 :
        result=is_prime(i)
        if result==True :
            print i
        i=i+1
