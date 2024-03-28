x=int(input("Enter the value of x : "))

match x:
    case 10:
        print("X is 10")
    case 20:
        print("X is 20")
    case 30:    
        print("X is 30")
    case _:
        print("X is not present")