#flow control statements 7 of them
#if / if else / if elif else (multiple) / for and while / break and continue
marks = int(input('enter a mark'))
if(marks > 80): 
    print("Grade A")  #common if else flow. defining a grade based on a MArk
elif(marks > 60):
    print ('Grade B')
elif(marks > 40):
    print("Grade FAIL")
else:
    print('Grade = dumbass')        

#looping - While and for
#while loop is unknown number of loops or iterations until the condiion is met false
#For loop is for a known number of iterations
num =  int(input('Enter the value of N = ')) #all inputs are in strings. so need to convert to integer
if(num <= 0):
    print('Enter a valid value') #input was zero or less
else:
    sum = 0 #setting the totla sum at zero initially
    while(num > 0): #while the total sum is grater than zero
        sum +=num #add the previous sum to the number from the input and make the new sum
        num -= 1   #next number is the prevous minus 1. (zeor plus input) - 1
print(sum)        #while loop now runs till number reduces to zero and prints a sumation

#for loop - known number of iterations. for 99 beer song
for quant in range(5,0,-1):
    if quant > 1:
        print(quant, ' - bottles of beers on the wall')
        if quant > 2:
            suffix = str(quant-1)+ " - bottles of the beer on the wall"
        else:
            suffix = '1 bottle of beer on the wall'
    elif quant == 1:
        suffix = 'no more beers on the wall'
    print('take one down and pass it on', suffix)
    print('**********************************') 
#test modification of the for loop from above. BOOM my own little concisising
for quant in range(5,0,-1):
    if quant > 1:
        print(quant, ' - bottles of beers on the wall')
        suffix = str(quant-1)+ " - bottles of the beer on the wall"
    else:
        print(quant,' - bottle left on the wall' )
        suffix = 'no more beers on the wall'
   
    print('take one down and pass it on', suffix)
    print('***___**___***__*_*_*__*_*') 


# break statement to come out of a loop
count = 0
while True:
    print(count)
    count +=1
    if(count > 10):
        break

for x in range(20): #printing odds or even numbers
    if(x % 2) != 0:
        continue
    print(x)

def add(a, b): #defining your own functions
    co = a + b
    return co

arg1 = 50000000
arg2 = 1000000000
print(add(arg1, arg2))

print('''-----------------
        ----------------''')
def fibo(n):
    a = 0
    b = 1
    for _ in range(n):
        c = a + b
        a = b
        b = c
        print(a, '\n')
    return c
num = int(input('enter a number - '))
print(fibo(num))
