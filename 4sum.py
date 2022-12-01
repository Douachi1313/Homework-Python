
number = int(input("Enter number "))
total = 0 
for i in range(len(str(number))):
    degit = number % 10 
    number = number //10
    total +=  degit 
print(total)