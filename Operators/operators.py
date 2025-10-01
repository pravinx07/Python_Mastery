
# Arithmetic Operators
# x = 10
# y = 4
# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)
# print(x // y)
# print(x % y)
# print(x  ** y)

# Comparison Operators

a = 5
b = 10

print(a == b)   # False
print(a != b)   # True
print(a > b)    # False
print(a < b)    # True
print(a >= 5)   # True
print(b <= 5)   # False


print(1 < 5 < 10)

# Assignment Operators
x = 10
x += 5   # same as x = x + 5
x -= 3   # same as x = x - 3
x *= 2   # same as x = x * 2
x /= 4   # same as x = x / 4

print(x)

# Identity Operators
a = [1,2,3]
b = a
c = [1,2,3]

# is checks identity (same object).
# == checks equality (same values).
print(a is b)
print(a == b)
print(b is c)
print(b == c)

# Membership Operators
s = "python"
print("p" in s)
print("z" not in s)