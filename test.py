
import numpy

a = numpy.array([[7,53,183,439,863],
        [497,383,563,79,973],
        [287,63,343,169,583],
        [327,343,773,959,943],
        [767,473,103,699,303]])
print(a)
b = a[4]
print(b)
c = numpy.sort(a)
print(c)
d = numpy.max(a[0]),max(a[1]),max(a[2]),min(a[3])
print(d)
e = numpy.max(a[0])+max(a[1])+max(a[2])+max(a[3])
print(e)




print('=================')

# Different ways to test multiple
# flags at once in Python
x, y, z = 0, 1, 0

if x == 1 or y == 1 or z == 1:
    print('passed')

if 1 in (x, y, z):
    print('passed')

# These only test for truthiness:
if x or y or z:
    print('passed')

if any((x, y, z)):
    print('passed')
else:
        print('fail')

        # The get() method on dicts
# and its "default" argument

name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
}

def greeting(userid):
    return "Hi %s!" % name_for_userid.get(userid, "there")

print(greeting(382))
"Hi Alice!"

print(greeting(333333))
"Hi there!"


