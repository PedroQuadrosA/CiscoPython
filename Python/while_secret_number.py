secret_number = 777
print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

choice = int(input("Guess the secret number: "))
while choice != secret_number:
    print("Ha ha! You're stuck in my loop!")
    choice = int(input("Guess the secret number again: "))
print("Well done, muggle! You're free now!")
