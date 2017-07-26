"""
16. Take the input from the user for(Total number of people, toatl number of busses, Number of seats for bus). Based on the input
Deside whether there is sufficient busses or not and give solution for how many extra busses required.
"""
import sys
#Taking input from User
no_of_people=raw_input("Please Enter total number of people:")
if no_of_people.isdigit() :
    no_of_people=int(no_of_people)#Converting user input to integer number
else :
    sys.exit("Input should be in integers")
no_of_buses=raw_input("Please Enter total number of buses")
if no_of_buses.isdigit() :
    no_of_buses=int(no_of_buses)#Converting user input to integer number
else :
    sys.exit("Input should be in integers")
no_of_seats=raw_input("Please Enter total number of seats per bus")
if no_of_seats.isdigit():
    no_of_seats=float(no_of_seats)#Converting user input to Float number
else :
    sys.exit("Input should be in integers")
#Calculating how many buses required
total_required_bus=no_of_people/no_of_seats
if no_of_buses>=total_required_bus : # Result will be on float but we need output in whiole number
    print"There is sufficient number of buses"
    if total_required_bus==int(total_required_bus) : # Comparing No of buses in float and whole are equal or not, if they are equal then print as it is otherwise add 1 and print
        print "Total buses required are:",int(total_required_bus)
    else :
        print "Total buses required are:",int(total_required_bus)+1
    print"Total passengers:",no_of_people
else :
    extra_buses=total_required_bus-no_of_buses
    if extra_buses==int(extra_buses) : # Comparing No of buses in float and whole are equal or not, if they are equal then print as it is otherwise add 1 and print
        print"Extra buses required to carried all passengers are:",int(extra_buses)
    else:
        print"Extra buses required to carried all passengers are:",int(extra_buses)+1


