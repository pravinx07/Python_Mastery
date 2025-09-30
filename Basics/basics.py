# 1
# print('Hello World')

# 2
# name = input("Enter your name: ");
# print("Hello", name + "!")

a = 10
b = 10

# import this
# print(id(a))
# print(id(b))




# print(0.1 + 0.2)
# s = "hello"
# s[2] = "H"  # give error bcos str are immutable
# print(s[0])


#  Boolean 
# Secret: In Python, values have truthiness:
# 0, "", [], {}, None → False
# everything else → True
# hot = True
# cold = False
# print(hot and not cold)   # && and ~ (not) operator


# x = None
# print(type(x))


#  Assignment
# 1.Store your age in a variable. Print it.
age = 24
print("age:",age)


# 2. Find the type of: 42, 3.14, "Python", True, None.
a = 42
b = 3.14
c = "str"
d = True
e = None
print(type(a), type(b), type(c), type(d), type(e))

# 1. Convert string "100" to int and add 50.
num = "100"
print(int(num) + 50)

# 3. Reverse a string "DEV" using indexing ([::-1]).
s = "DEV"
print(s[::-1])

# 4. Check truthiness of these: 0, 1, "", "Hi", [], [1,2].
x = 0
y = 1
z = ""
a = "Hi"
b = []
c = [1,2]
print(bool(x))
print(bool(y))
print(bool(z))
print(bool(a))
print(bool(b))
print(bool(c))

# 5. Print the binary, hex, and ASCII value of some numbers/characters.
print(bin(4))
print(hex(255))
print(ord("A"))
print(chr(59))