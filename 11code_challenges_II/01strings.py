# 1. Count Letters
# For the first code challenge, we are going to count the number of unique letters in a string. This means that when we are looking at the word, any new letters should be counted and any duplicates should not be counted. There are a few ways to solve this, but we can use the provided alphabet string to ensure that duplicates are not counted. Here is what we need to do:

# Define the function to accept one parameter — the word whose letters we are counting
# Create a counter to keep track of unique letters
# Loop through every letter in our alphabet string. If the current letter was found in our word, increase our count
# Return the count after looping through all letters.

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
def unique_english_letters(word):
  counter = 0
  for letter in letters:
    if letter in word:
      counter += 1
  return counter
# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4

# 2. Count X
# Next, we are going to try something a bit different. This time we are going to count the number of occurrences of a certain letter within a string. Our function will accept a parameter for a string and another for the character which we are going to count. For example, providing the word "mississippi" and the character 's' would result in an answer of 4. These are the steps we need to take:

# Define the function to accept two parameters. word for the input string and x for the single character
# Create a counter to keep track of the occurrences
# Loop through every letter in the string. If the current letter is equal to the input letter, increase our counter
# Return the counter after looping through the entire string.

# Write your count_char_x function here:
def count_char_x(word, x):
  occurences = 0
  for letter in word:
    if letter == x:
      occurences += 1
  return occurences
# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1

# 3. Count Multi X
# Now let’s change our function to compare against an entire string instead of a single character. This function should accept a string and a substring to compare against. The number of occurrences of the second parameter within the first parameter string are returned. What this means is that we are checking the number of occurrences of the shorter string (second parameter) within the longer string (first parameter). One way to accomplish this is using the split function. Here is how to do that:

# Define the function to accept two parameters. word for the input string and x for the second string we are searching for
# Split the string into substrings based on the second input parameter
# Count the number of instances the substring appeared in the first input string based on the split string
# Return the result

# Write your count_multi_char_x function here:
def count_multi_char_x(word, x):
  splits = word.split(x)
  return (len(splits)-1)
# Uncomment these function calls to test your function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1

# 4. Substring Between
# Here is a challenging problem. We need a function that is able to extract a portion of a string between two characters. The function will take three parameters where the first parameter is the string we are going to extract the substring from, the second input is the starting character of our substring and the third character is the ending character of our substring. Here are the steps we can use:

# Define the function to accept three parameters, one string and two characters
# find the starting index of our substring using the second input parameter
# find the ending index of our substring using the third input parameter
# If neither of the indices are -1, return the portion of the first input parameter string between the starting and ending indices (not including the starting and ending index)
# If either of the indices are -1, that means the start or end of the substring didn’t exist in our string. Return the original string in this case.

# Write your substring_between_letters function here:
def substring_between_letters(word, start, end):
  first = word.find(start)
  last = word.find(end)
  if first > -1 and last > -1:
    return word[first + 1 :last]
  return word
# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"

# 5. X Length
# Let’s use the split method in a different way. We need a new function that is able to accept two inputs: one for a sentence and another for a number. The function returns True if every single word in the sentence has a length greater than or equal to the number provided. These are the steps:

# Define the function to accept two parameters, one string, and one number
# Split up the sentence into an array of words
# Loop through the words. If the length of any of the words is less than the provided number return False
# If we made it through the loop without returning False then return True

# Write your x_length_words function here:
def x_length_words(sentence, x):
  words = sentence.split()
  for word in words :
    if len(word) >= x:
      return True
    return False
# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True