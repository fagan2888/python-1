
print('2'+'3')
print (2+3)
print('hello')
print(int("3"+"4"))
#print(float(input("enter number"))+float(input("enter number ")))
x=5
print(x)
print(x+5)
x='this is a string'
print(x)
print(x*3)
print(x+"!")
tih_gayan=5
print(tih_gayan)
print("hello")
array = [1,2,3,4,5,6,7,8,9,10,11]
for i in array:
    if i == 3:
        print("bummer")
        continue
    print(i)
    for letter in 'abc':
        print(i,letter)
for i in range(1,10):
    print (i)
    
 #sorting highest and lowest, number of timesa letter appears,
 # leter  count, check if anything from the alphabet is there  
    srt = "edureka"
    print(max(srt))
    print(min(srt))
    
    print(srt.count('d'))
    print(srt.isalpha())

#data types. numbers strings and tuples    
my_tup = ('edu', 2.4 , 5 , "python")
print(my_tup)

#mutable data types: lists; dictionaries and sets
#key, values, get a value, update dictionary, pop a word out

mylist = ['green','blue','red','yellow','black']
print(mylist)
mylist.append('grey')
print(mylist)
mylist.extend(['blue','white'])
print(mylist)
myDict = {1:'josh', 2:'gayan', 3:'anya', 4:'alyce',5:[2,4,5]}
print(myDict[4])
print(len(myDict))
print(myDict.keys())
print(myDict.values())
print(myDict[4])
print(len(myDict))
print(myDict.items())
print(myDict.get(4))
print(myDict[4])
myDict.update({6:'hello'})
print(myDict)
print(myDict[6])
myDict.pop(3)
print(myDict)
mySet = {1,2,3,4,5,6,'a','b','c'} #define a set curly brackets
print(mySet)
ms1 = {1,2,'a','b',3,4,5}
ms2 = {3,4,5,'a','b','c','d'}
print("union = ", ms1 | ms2) #union of sets
print("intersectoin = ", ms1 & ms2) #intersection of sets
print("difference = " , ms1 - ms2) #difference in sets

