a = [[7,53,183,439,863],
        [497,383,563,79,973],
        [287,63,343,169,583],
        [327,343,773,959,943],
        [767,473,103,699,303]]

for row in range(5):
    print(a[row])

print("-------")

sum = 0
for row in range(5):
    max = 0
    for column in range(5):
        if (a[row][column] > max):
            max = a[row][column]
    print(max)
    sum = sum + max
print(sum)

print("-------")
       
sum = 0
for lis in a:
    max = 0
    for elem in lis:
        if (elem > max):
            max = elem
    print(max)
    sum = sum + max
print(sum)

print("----Get the index of the maximum in the matrix---")

max = 0
i = -1
j = -1
for row in range(5):
    for column in range(5):
        if (a[row][column] > max):
            max = a[row][column]
            i = row
            j = column
print('The index of', max, 'is (', i, ',', j, ')')
print('The index of %s is (%i, %i)'%(max, i, j))
