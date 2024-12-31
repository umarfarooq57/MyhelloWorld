
# Let's break down how this code works step by step:

# 1. Function Definition:
#    - The function 'find_vowels' is defined that takes one parameter 'string'
#    - This function will search for vowels in the input string

# 2. Vowels Definition:
#    - A string 'vowels' is created containing all vowels (both lowercase and uppercase)
#    - vowels = 'aeiouAEIOU'
#    - This will be used to check if a character is a vowel

# 3. Initialize Empty List:
#    - An empty list 'found_vowels' is created
#    - This list will store unique vowels found in the input string
#    - Using a list allows us to maintain the order of discovery

# 4. String Processing:
#    - The function uses a for loop to iterate through each character in the input string
#    - 'for char in string:' - each character is temporarily stored in 'char' variable

# 5. Vowel Check:
#    - For each character, it checks 'if char in vowels:'
#    - This determines if the current character is a vowel
#    - The 'in' operator checks if the character exists in our vowels string

# 6. Duplicate Prevention:
#    - Before adding a vowel, it checks 'if char not in found_vowels:'
#    - This ensures each vowel is only added once to the result
#    - Prevents duplicate vowels in the output

# 7. Adding Vowels:
#    - If a character is a vowel and not already in the list
#    - It's added using found_vowels.append(char)

# 8. Return Result:
#    - The function returns the found_vowels list
#    - Contains all unique vowels found in the input string

# 9. Testing the Function:
#    - A test string is created with multiple words
#    - The function is called with this test string
#    - Results are printed using f-string formatting
#    - Shows both the input string and the vowels found

# Example Output Explanation:
# - For the test string "Hello World and Hello World here how are you i am fine and you are fine"
# - The function will find these unique vowels: ['e', 'o', 'a', 'i', 'u']
# - Each vowel appears only once in the result, even if it appears multiple times in the string
# - The order in the result list reflects the order in which unique vowels were first encountered

