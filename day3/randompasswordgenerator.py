import random
import string
chars = string.ascii_letters + string.digits + "!@#$%^&*"
def generate_passwords(n):
    return (''.join(random.choice(chars) for _ in range(8)) for _ in range(n))
passwords = generate_passwords(3)
for password in passwords:
    print(password)
