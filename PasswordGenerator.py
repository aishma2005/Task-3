import random
import string

# Function to generate a random password
def PasswordGenerator(length):
    if length <= 0:
            print("Length should be greater than zero.")
            return
    else:
         characters = string.ascii_letters + string.digits + string.punctuation
         password = ''.join(random.choices(characters, k=length))
         print(f"Generated Password: {password}")  
     

# Main function to run the password generator
print("===== Password Generator =====")
try:
    length = int(input("Enter the desired length of the password: "))
    password = PasswordGenerator(length)
     
except ValueError:
    print("Invalid input. Please enter a valid integer.")

 
