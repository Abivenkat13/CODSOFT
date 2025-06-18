import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 for better security."
    allowed_characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(allowed_characters) for _ in range(length))
    return password

print("🔐 Welcome to the Password Generator!")

length = int(input("Enter the desired password length: "))

generated_password = generate_password(length)
print("Your secure password is:", generated_password)
