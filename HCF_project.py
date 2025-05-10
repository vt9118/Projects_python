# This is the program of the HCF
def hcf(x,y):
    if x >y :
        min = y 
    else :
        min = x 

        for i in range (1, min + 1):
            if (x%i ==0) and (y%i ==0):
                hcf = i
    print(f"The HCF of {x} and {y} is {hcf}")
                

x = int(input("Enter the  first number : "))
y = int (input ("Enter the second number : "))

hcf(x,y)
