
# Python code to demonstrate naive 
# method to compute gcd ( recursion ) 
  
def hcfnaive(a,b): 
    if(b==0): 
        return a 
    else: 
        return hcfnaive(b,a%b) 
  
a,b =int(input("enter 2 numbers")),int(input())

  
# prints 12 
print ("The gcd of 60 and 48 is : ",end="") 
print (hcfnaive(a,b)) 
