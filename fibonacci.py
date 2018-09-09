# fibonacci

import random as rn

# 1 1 2 3 5 8 

F_n_2 = 1
F_n_1 = 1
F_n = 0

fibArray = [F_n_2, F_n_1]

i = 0
while(i<12):
    i += 1      # i = i + 1
    F_n = F_n_1 + F_n_2
    fibArray.append(F_n)
    F_n_2 = F_n_1
    F_n_1 = F_n

print(fibArray)

rn.shuffle(fibArray)

print(fibArray)

print(fibArray.index(5))
print(fibArray[5])

def findMax(array):
    max = 0

    for j in range(0, len(array)):   # == range(0,12):
        if (array[j] > max):
            max = array[j]
            # print("found a new max:", max)
    return max

print(findMax(fibArray))
