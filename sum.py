a=input("Enter a number: ") 
b=input("Enter another number: ")   
    
#sum= a+b   # a=2, b=3 -> output 23  because both a and b are strings hence gets concatinated 

sum= int(a)+ int(b)  # converting a and b to integers before adding them
print("The sum is: ",sum)   

sum2= float(a)+ float(b)
print("The sum is: ",sum2)    
