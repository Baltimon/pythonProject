def menu():
    print (" 1. Function \n 2. Function 2 \n 3. PI approximation \n 4. Factorial \n 5. Multiplication \n 6. Exit")

def function1(inp):
    ret = 1
    for i in range (inp):
        ret = ret *2*(i+1)
    print("\n---the Resunlt is",ret,"\n")

def function2(inp):
    ret = 10
    count =9
    for i in range (inp):
        count=count+1
        if(i%2==1):
            ret=ret-count
        if (i%2 == 0 and i!=0):
            ret= ret+count        
    print("\n---the Resunlt is",ret,"\n")

def PIaprr(inp):
    ret = 4
    count =-1
    for i in range (inp):
        count=count+2
        if(i%2==1):
            ret=ret-(4/count)
        if (i%2 == 0 and i!=0):
            ret= ret+(4/count)  
    print("\n---the Resunlt is",ret,"\n")


def Factorial(inp):
    ret=1
    for i in range (1,inp+1): 
        ret = ret *i
    print("\n---the Resunlt is",ret,"\n")

def multiplicstion(x,y):
    ret=0
    while(x>0):
        ret=ret+y
        x=x-1
    print("\n---the Resunlt is",ret,"\n")



def main():
    run = True
    while(run == True):
        menu()
        choice = int(input("type Number of your choice:"))
        if(choice == 1):
            inp = int(input("Type Number biger then 0:"))
            function1(inp)
        if(choice == 2):
            inp = int(input("Type Number biger then 0:"))
            function2(inp)
        if(choice ==3):
            inp = int(input("Type Number biger then 0:"))
            PIaprr(inp)
        if(choice ==4):
            inp = int(input("Type Number biger then 0:"))
            Factorial(inp)
        if(choice==5):
            inp1 = int(input("Type 1.Number biger then 0:"))
            inp2 = int(input("Type 2.Number biger then 0:"))
            multiplicstion(inp1,inp2)
        if(choice == 6):
            run = False
    
main()