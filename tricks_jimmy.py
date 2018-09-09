'''#hexa numbers Here is how we convert binary to/from hex:
print(b'hello world')
print(b'hello world'.hex())
print(bytes.fromhex('68656c6c6f20776f726c'))


#excercise
print(bytes.fromhex('b010a49c82b4bc84cc1dfd6e09b2b8114d016041efaf591eca88959e327dd29a'))

print('----------------------')
h = 'b010a49c82b4bc84cc1dfd6e09b2b8114d016041efaf591eca88959e327dd29a'
print(bytes.fromhex(h))# convert to binary (bytes.fromhex)

print(h[::-1]) # reverse ([::-1])
print(b'convert to hex'.hex()) # convert to hex()

print('-----------------')

#Converting from bytes to integer requires learning about Big and Little Endian encoding.
#In Python we can convert an integer to big or little endian using a built-in method:



n = 1234567890
big_endian = n.to_bytes(4, 'big')  # b'\x49\x96\x02\xd2'
little_endian = n.to_bytes(4, 'little')  # b'\xd2\x02\x96\x49'
print(big_endian)
print(little_endian)

big_endian = b'I\x96\x02\xd2'
little_endian = b'\xd2\x02\x96I'
n = int.from_bytes(big_endian, 'big') #1234567890
print(n)
n = int.from_bytes(little_endian, 'little') #1234567890
print(n)

print("----------------------------")
n = 1234567890
big_endian = n.to_bytes(4, 'big') #define big endian
little_endian = n.to_bytes(4, 'little') #define little endian

print(big_endian.hex()) #print big endian in hexa
print(little_endian.hex()) #print little ndian in hexa

print(int.from_bytes(big_endian, 'big')) #convert big endian in bytes integer
print(int.from_bytes(little_endian, 'little')) #conver little endian in bytes to integer



def little_endian_to_int(b):
       
        little_endian = b
        little_endian_to_int = int.from_bytes(b, 'little')
        
        return little_endian_to_int
b = b'\x11\x22\x33\x44\x55'
print(little_endian_to_int(b))

print('------------------')

def int_to_little_endian(n, length):
    
        int_to_little_endian = n.to_bytes(length, 'little')   
        return int_to_little_endian

n = 1234567890
print(int_to_little_endian(n,4))

import pip


prime = 31
# 2+15=?
print((2+15) % prime)
# 17+21=?
print((17+21) % prime)
# 29-4=?
print((29-4) % prime)
# 15-30=?
print((15-30) % prime)

points = ((-2,4),(3,7),(18,77))
for x, y in points:
    if y**2 == x**3 + 5*x + 7:
        print('({},{} is on the curve'.format(x,y))')
    else:
        print('({},{} is not the curve'.format(x,y))')
# for x, y in points:
    # determine whether (x,y) is on the curve

 def merkle_parent_level(hashes):
    #Takes a list of binary hashes and returns a list that's half the length
    if len(hashes) == 1:     # if the list has exactly 1 element raise an error
        raise RuntimeError('Cannot take a parent level with only 1 item')
    parent_level = []     # initialize next level
    for i in range(0, len(hashes), 2):    # loop over every pair (use: for i in range(0, len(hashes), 2))
        parent = merkle_parent(hashes[i], hashes[i+1])         # get the merkle parent of i and i+1 hashes
        parent_level.append(parent)         # append parent to parent level
    return parent_level     # return parent level
# Verify curve Example
'''
prime = 137
x, y = 73, 128
print(y**2)
print(y**2 % prime)
print(x**3 + 7)
print((x**3 + 7) % prime)

print('----------')
a = "hello world"
print(a)
zzz = a.encode()
print(zzz)
print(zzz.hex())
new_bytes = []
for letter in a:
    new_bytes.append(letter.encode().hex())
print(new_bytes)
print('\\x' + '\\x'.join(new_bytes))
print("\x68\x65\x6c\x6c\x6f\x20\x77\x6f\x72\x6c\x6455555!!")
print(bytes.fromhex("68656c6c6f20776f726c64").decode())

print('----------')

print("\x3f")
print("?")
print(b'?'.hex())
print("\x3f" == "?")
a = '\xb0\x10\xa4\x9c\x82\xb4\xbc\x84\xcc\x1d\xfd\xb2\xb8\x11\x01\xef\xaf\x1e\xca\x88\x95\x9e\xd2\x9a'
print(a)

print('\xb1\xb2\xb3\xb4\xb5\xb6\xb7')
g =  'hello world'
print('ell')

print(b'&'[0]) # 38 since & charcter #38
print(bytes([38])) # b'&'

print('----------')
n = 1234567890
print(n.to_bytes(4, 'big', signed=True))
print(n.to_bytes(8, 'big', signed=True))
print((-n).to_bytes(4, 'big', signed=True))

print(n.to_bytes(4, 'big').hex())


# "\xb6i\xfd."
print("\xb6\x69\xfd\x2e")
