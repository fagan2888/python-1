from fibonacci import findMax

print("Don't")
print("Hello\
ghhhfgh world!") #printing text
a = 10 # int
b = 1.6 # float
c = a + b
print(c)
print(a<b)
print(b**a) # b to the power a
print(True and False and True and False) # boolean operator
print(9%4) # = 1 modulo
print(9//4) # = 2 (int)
print(9/4) # float
i = 5
print(i == 4)
print(i != 4)

while(i > 1):
    print('i is', i)
    i = i-1

i = 3

if(i == 5):
    print("this will end")
elif(i == 4):
    print('do other things')
else:
    print('nothing above happend')

k = 0
for j in range(1,5): # [1,2,3,4]
    k = k + j
print(k)

exampleList = [1,5,2,7,8,3,5]
print(findMax(exampleList))

print('-----------------')

g = len(exampleList)
print(g)

for j in [1,5,6,8,9,5]:
    if (j == 5):
        print("is 5")
        continue        # continue with next iteration
    j += 1
    print(j)
    if(j == 9):
        break
        

def someFunc(a, b, c, d):
    print(a,b,c,d)
    k = 99
    return k

someVariable = someFunc(66, 'hello', 7, g)
print(someVariable)

# datastructures: list, tuple, dictionary
exList = [2, 5, 7, "some string", 99.7]
ex2List = ["nice", "list"]
exList.append(ex2List)
print(exList)
exList[4] # element with index 4, which is 99.7

# tuples are like lists but unchangable
exTuple = ("monkey", "wolf", "koala")
ex2Tuple = ("bird", "snake")
ex3Tuple = (exTuple, ex2Tuple, "another animal")
newTuple = exTuple + ex2Tuple
print(ex3Tuple)
print(newTuple)

#dictionary
myDic = {"hans": "0846837354", "anna": "anna@gmail.com", "tomas": ex3Tuple} # key: value; kez must be unique
print(myDic["anna"])
print(myDic["tomas"])

for name, detail in myDic.items():
    print(name, detail)
    print("The name of the person is", name, "and its value is", detail)
    print("The name of the person is %s and its value is %s with number %i"%(name, detail, 6))
