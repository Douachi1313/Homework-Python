num = int(input("Enter number "))
fact = 1
total = 0 
  
for i in range(1,num+1):
    fact = fact * i
    
print ("The factorial of", num ,"is : ",fact)

for i in range(len(str(fact))):
    degit = fact % 10 
    fact = fact //10
    total +=  degit 
print (total)