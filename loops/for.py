# Print numbers 1 to 20 using a for loop.
# for i in range(21):
#     # print(i + 1)

# Print only even numbers from 1 to 50.

for i in range(2,50,2):
    print(i)


# Loop through the word "PYTHON" and print each character separately.

s = "Python"

for char in s:
    print(char)

# Use break to stop a loop when the number reaches 7.

for i in range(10):
    if i == 7:
        break
    print(i)