# Bytes to Int & more Python tips and tricks

#Python Tricks
#Here is how we convert binary to/from hex:


print(b'hello world'.hex())
print(bytes.fromhex('68656c6c6f20776f726c64'))
# 68656c6c6f20776f726c64
# b'hello world'

# Reverse this hex dump: b010a49c82b4bc84cc1dfd6e09b2b8114d016041efaf591eca88959e327dd29a
# Hint: you'll want to turn this into binary data, reverse and turn it into hex again


h = 'b010a49c82b4bc84cc1dfd6e09b2b8114d016041efaf591eca88959e327dd29a'
print(bytes.fromhex(h))# convert to binary (bytes.fromhex)
​
print(h[::-1]) # reverse ([::-1])
print(b'convert to hex'.hex()[::-1]) # convert to hex() and reverse
​
a = '\xb0\x10\xa4\x9c\x82\xb4\xbc\x84\xcc\x1d\xfdn\t\xb2\xb8\x11M\x01`A\xef\xafY\x1e\xca\x88\x95\x9e2}\xd2\x9a'
print(a)
b = a.split("\\x")
print(b)
print('\xb1\xb2\xb3\xb4\xb5\xb6\xb7')
​
b'\xb0\x10\xa4\x9c\x82\xb4\xbc\x84\xcc\x1d\xfdn\t\xb2\xb8\x11M\x01`A\xef\xafY\x1e\xca\x88\x95\x9e2}\xd2\x9a'
# a92dd723e95988ace195fafe140610d4118b2b90e6dfd1cc48cb4b28c94a010b
# 87568602f6470247275667e6f636
# °¤´¼Ìýn	²¸M`Aï¯YÊ2}Ò
# ['°\x10¤\x9c\x82´¼\x84Ì\x1dýn\t²¸\x11M\x01`Aï¯Y\x1eÊ\x88\x95\x9e2}Ò\x9a']
# ±²³´µ¶·
# Converting from bytes to int and back
# Converting from bytes to integer requires learning about Big and Little Endian encoding. Essentially any number greater than 255 can be encoded in two ways, with the "Big End" going first or the "Little End" going first.

# Normal human reading is from the "Big End". For example 123 is read as 100 + 20 + 3. Some computer systems encode integers with the "Little End" first.

# A number like 500 is encoded this way in Big Endian:

0x01f4 (256 + 244)

But this way in Little Endian:

0xf401 (244 + 256)

In Python we can convert an integer to big or little endian using a built-in method:

n = 1234567890
big_endian = n.to_bytes(4, 'big')  # b'\x49\x96\x02\xd2'
little_endian = n.to_bytes(4, 'little')  # b'\xd2\x02\x96\x49'
We can also convert from bytes to an integer this way:

big_endian = b'\x49\x96\x02\xd2'
n = int.from_bytes(big_endian, 'big')  # 1234567890
little_endian = b'\xd2\x02\x96\x49'
n = int.from_bytes(little_endian, 'little')  # 1234567890

n = 1234567890
big_endian = n.to_bytes(4, 'big')
little_endian = n.to_bytes(4, 'little')
​
print(big_endian)
print(big_endian.hex())
m = 126207244316550804821666916
print(m.to_bytes(16, 'little'))
print(m.to_bytes(16, 'big'))
print(m.to_bytes(16, 'big').hex())
​
​
print(little_endian)
print(little_endian.hex())
​
print(int.from_bytes(big_endian, 'big'))
print(int.from_bytes(b'hello world', 'big'))
​
print(int.from_bytes(little_endian, 'little'))
b'I\x96\x02\xd2'
499602d2
b'dlrow olleh\x00\x00\x00\x00\x00'
b'\x00\x00\x00\x00\x00hello world'
000000000068656c6c6f20776f726c64
b'\xd2\x02\x96I'
d2029649
1234567890
126207244316550804821666916
1234567890
Try it
Convert the following:

8675309 to 8 bytes in big endian
interpret b'\x11\x22\x33\x44\x55' as a little endian integer

n = 8675309
# print n in 8 big endian bytes
big_endian = n.to_bytes(8, 'big')
print(big_endian)
little_endian = b'\x11\x22\x33\x44\x55'
print(little_endian)
print(int.from_bytes(little_endian, 'little'))
# print little endian in decimal
b'\x00\x00\x00\x00\x00\x84_\xed'
b'\x11"3DU'
366216421905
Test Driven Exercise
Add little_endian_to_int() and int_to_little_endian() methods to your library.


'''def little_endian_to_int(b)
    little_endian_to_int takes byte sequence as a little-endian number.
    Returns an integer'''
    # use the from_bytes method of int
def little_endian_to_int(little_endian):
       
        little_endian_to_int = int.from_bytes(little_endian, 'little')
        
        return little_endian_to_int
    
    
    
b = b'\x11\x22\x33\x44\x55'
print(little_endian_to_int(b))  
   
    
​
'''def int_to_little_endian(n, length)
    endian_to_little_endian takes an integer and returns the little-endian
    byte sequence of length'''
    # use the to_bytes method of n
def int_to_little_endian(n):
    
        int_to_little_endian = n.to_bytes(4, 'little')   
        return int_to_little_endian
​
n = 1234567890
print(int_to_little_endian(n))
print(int_to_little_endian(128788875))
m = 50392
print(int_to_little_endian(m))
​
​
        
366216421905
b'\xd2\x02\x96I'
b'\x8b)\xad\x07'
b'\xd8\xc4\x00\x00'

def little_endian_to_int(b):
       
        little_endian_to_int = int.from_bytes(b, 'little')
        
        return little_endian_to_int

def int_to_little_endian(number, length_byte):
    
        int_to_little_endian = number.to_bytes(length_bytes, 'little')   
        return int_to_little_endian
    
n = 1234567890
print(int_to_little_endian(n,4))
print(int_to_little_endian(1287888758888, 8))
print(int_to_little_endian(88676786576586586757658675685, 20))
​
b'\xd2\x02\x96I'
b'h\xe8&\xdc+\x01\x00\x00'
b'\xe5\x89qd\xb7\xcf\xb7\xc4\xf8\xb7\x87\x1e\x01\x00\x00\x00\x00\x00\x00\x00'

​