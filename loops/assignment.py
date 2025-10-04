# 1. Multiplication Table 📊

# num = int(input("Enter any number: "))

# for i in range(1,11):
#     print(f"{num} X {i} = {num * i}")



# 2. Number Guessing Game 🎯

# secret = 7
# guess = 0

# while guess != secret:
#     guess = int(input("Enter any number: "))
#     if guess > secret:
#         print("To high")
#     elif guess < secret:
#         print("too Low")
#     else:
#         print("🎉 Correct! You guessed it!")


# 3. Password Attempts 🔐

# password = "python123"
# attempts = 3

# while attempts > 0:
#     user_pass = input("Enter password: ")
#     if user_pass == password:
#         print("Access Granted")
#         break
#     else:
#         attempts -= 1
#         print(f"Wrong Password. {attempts} attempts left")


# if attempts == 0:
#     print("Account Locked")


# 🔹 5. Pattern Printing ⭐

rows = 5
for i in range(1, rows+1):
    print("*" * i)