'''
Using match case in python
User will input a number n , and we have to print the weekday against that number . If it is a valid number then print the weekday otherwise print "Invalid Input"
'''
# Input
n=int(input("Enter the number:"))
match n:
    case 1:
        print("Day is : Monday")
    case 2:
        print("Day is : Tuesday")
    case 3:
        print("Day is : Wednesday")
    case 4:
        print("Day is : Thursday")
    case 5:
        print("Day is : Friday")
    case 6:
        print("Day is : Saturday")
    case 7:
        print("Day is : Sunday")
    case _:
        print("Invalid Input")

