try:
    a=int(input("Enter a number: "))
    b=int(input("Enter a number: "))
    print("what kind of operation do you want to perform")
    o=input("enter operation symbol(+,-,*,/): ")

    match o:
        case '+':
            print(f"{a} + {b} = {a+b}")
        case '-':
            print(f"{a} - {b} = {a-b}")
        case '*':
            print(f"{a} * {b} = {a*b}")
        case '/':
            if b == 0:
                print("Division by zero is not allowed.")
            else:
                print(f"{a} / {b} = {a/b}")
        case _:
            print("Invalid operation symbol. Please use +, -, *, or /.")    
except Exception as e:
    print("enter valid values for a and b")
