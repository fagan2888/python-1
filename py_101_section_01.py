#py_101_ch_01
print('hello from python')
print('''           
       +++++++++
                      ''')
#creating strings in python 
my_string = 'Welcome to Python!'
another_string = 'This bright red fox jumped the fence.'
a_long_string = '''this is a
multi line string. It covers more than
one line'''
print(my_string)
print(another_string)
print(a_long_string)
print('''
      ===================
  ''')

#how to embed quotes within a string. 
my_string = "I'm a python prorammer!"
otherString = 'the word "python" usually refers to a snake'
tripleString = """Here's another way to embed "quotes" in a string"""
print(my_string)
print(otherString)
print(tripleString)
print('''
===============   
   ''')
#3rd way to create a string - turning an integer into string - known as "casting"
# casting some data type onto another - numbers to string and string to numbers
my_number = 123
my_string = str(my_number) 
print(my_string)
print('''
======
''')
#showing the ID of the string. everytime you change the string
#it will change ID
my_string = "abc"
print(id(my_string))
print('''
===
''')
#string Concatenation - ie. adding strings together
string_one = 'my dog ate '
string_two = 'my homework'
string_three = string_one + string_two
print(string_three, '''

=====

''')
#making string upper case and lower case
print(my_string.upper())
print(my_string.lower())
print('this is a string'.upper())
print('this is a string'.swapcase(), '''

===

''')
# all string methods   print(dir(my_string))
#introspection - asking python to answer a question
print(my_string.capitalize()) # - capitalize the first letter
print(type(my_string)) #asking python what type of variable my_string is