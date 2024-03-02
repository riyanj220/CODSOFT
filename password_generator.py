import random
import string

def generate_passwords(length):
    chunk = string.digits + string.punctuation + string.ascii_letters 

    password = []
    for _ in range(length):
        value = random.choice(chunk)
        password+=value
    return password


def main():
    while True:
        try:
            user = int(input("Enter length of your required passsword: "))
            output = generate_passwords(user)
            password_string = "".join(output)

        except ValueError :
            print("Warning: Please enter a valid integer! ")
    
        else:
            print(f"Password generated:  {password_string}")
            break

if __name__ == "__main__":
    main()