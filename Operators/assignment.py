# 1. Write a program that takes a number and prints whether it’s even or odd (use %).

num = int(input("Enter any number to check even or odd: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 2. Compare two numbers and print which is greater (use if + comparison).

num1 = 23
num2 = 31

if num1 > num2:
    print(num1)
else:
    print(num2)

# 3. Check if a number is between 10 and 50 using chained comparison.
# (1 < 3 < 4)  chained comparison
n1 = 29
print(10 < n1 < 50)


# 4. Try and and or with numbers (e.g., 0 and 100, 100 or 0). Write what you observe.
print( 0 and 100)
print(100 or 0)


# 5. Use membership: ask user for a character, check if it exists in "openai".

char = str(input("Input any string: "))

print("z" in char)

