def calculator():
    x=int(input("enter number1: "))
    r=int(input("enter number2: "))
    y=input("enter +-*/")
    if y=="+":
        s=x+r
        print(s)
    elif y=="-":
        e=x-r
        print(e)
    elif y=="/":
        d=x/r
        print(d)
    else:
        j=x*r
        print(j)
    c=input("are you test  agin ? yes or no:")
    if c=="no"or"No":
        exit()
    elif c=="yes"or"Yes":
        calculator()


        
calculator()