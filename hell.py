import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
API_TOKEN = os.getenv('API_TOKEN')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
ENCRYPTION_SALT = os.getenv('ENCRYPTION_SALT')




print(f"Secret Key: {SECRET_KEY}")
print(f"API Token: {API_TOKEN}")
print(f"Database Password: {DATABASE_PASSWORD}")
print(f"AWS Access Key: {AWS_ACCESS_KEY}")
print(f"Encryption Salt: {ENCRYPTION_SALT}")


# Function to find vowels in a string
def find_vowels(string):
    # Define vowels
    vowels = 'aeiouAEIOU'
    # Initialize empty list to store found vowels
    found_vowels = []
    
    # Loop through each character in string
    for char in string:
        # Check if character is vowel
        if char in vowels:
            # Add to list if not already present
            if char not in found_vowels:
                found_vowels.append(char)
                
    return found_vowels

# Test string
test_string = "Hello World and Hello World here how are you i am fine and you are fine "
result = find_vowels(test_string)
print(f"Vowels found in '{test_string}': {result}")


# JavaScript equivalent:
#
# function findVowels(str) {
#     // Define vowels (both lowercase and uppercase)
#     const vowels = 'aeiouAEIOU';
#     
#     // Initialize empty array for found vowels
#     let foundVowels = [];
#     
#     // Process each character in the string
#     for (let char of str) {
#         // Check if character is a vowel and not already found
#         if (vowels.includes(char) && !foundVowels.includes(char)) {
#             foundVowels.push(char);
#         }
#     }
#     
#     // Return the array of found vowels
#     return foundVowels;
# }
#
# // Example usage:
# // const testString = "Hello World and Hello World here how are you i am fine and you are fine";
# // const result = findVowels(testString);
# // console.log(`Input string: ${testString}`);
# // console.log(`Found vowels: ${result}`);



# Requirements (add to requirements.txt):
# python-dotenv==1.0.0

# Install packages:
# pip install -r requirements.txt
# or directly:
# pip install python-dotenv

# Import and load environment variables
# from dotenv import load_dotenv
# import os

# Load environment variables from .env file
# load_dotenv()

# Now you can access environment variables using os.getenv()
# Example:
# secret_key = os.getenv('SECRET_KEY')
# api_token = os.getenv('API_TOKEN')
