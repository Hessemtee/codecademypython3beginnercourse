# 1. Sum Values
# For the first code challenge, we are going to look at only the values in a dictionary. This function should sum up all of the values from the key-value pairs in the dictionary. Here are the steps we need:

# Define the function to accept one parameter for our dictionary
# Create a variable to keep track of our sum
# Loop through every value in the dictionary
# Inside the loop, add each value to the sum
# Return the sum

# Write your sum_values function here:
def sum_values(my_dictionnary):
  sum = 0
  for item in my_dictionnary.values():
    sum += item
  return sum
# Uncomment these function calls to test your sum_values function:
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6

# 2. Even Keys
# Next, we are going to do something similar, but we are going to use the keys in order to retrieve the values. Additionally, we are going to only look at every even key within the dictionary. Here are the steps:

# Define the function to accept one parameter for our dictionary
# Create a variable to keep track of our sum
# Loop through every key in the dictionary
# Inside the loop, if the key is even, add the value from the even key
# After the loop, return the sum

# Write your sum_even_keys function here:
def sum_even_keys(my_dictionnary):
  sum = 0
  for key in my_dictionnary.keys():
    if key % 2 == 0:
      sum += my_dictionnary[key]
  return sum
# Uncomment these function calls to test your  function:
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6

# 3. Add Ten
# Let’s loop through the keys again, but this time let’s modify the values within the dictionary. Our function should add 10 to every value in the dictionary and return the modified dictionary. Here is what we need to do:

# Define the function to accept one parameter for our dictionary
# Loop through every key in the dictionary
# Retrieve the value using the key and add 10 to it. Make sure to re-save the new value to the original key.
# After the loop, return the modified dictionary

# Write your add_ten function here:
def add_ten(my_dictionary):
  for key in my_dictionary.keys():
    my_dictionary[key] += 10
  return my_dictionary
# Uncomment these function calls to test your  function:
print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}

# 4. Values That Are Keys
# We are making a program that will create a family tree. Using a dictionary, we want to return a list of all the children who are also parents of other children. Using dictionaries we can consider those people to be values which are also keys in our dictionary of family data. Here is what we need to do:

# Define the function to accept one parameter for our dictionary
# Create an empty list to hold the values we find
# Loop through every value in the dictionary
# Inside the loop, test if the current value is a key in the dictionary. If it is then append it to the list of values we found
# After the loop, return the list of values which are also keys

# Write your values_that_are_keys function here:
def values_that_are_keys(my_dictionary):
  value_keys = []
  for value in my_dictionary.values():
    if value in my_dictionary:
      value_keys.append(value)
  return value_keys
# Uncomment these function calls to test your  function:
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]

# 5. Largest Value
# For the last challenge, we are going to create a function that is able to find the maximum value in the dictionary and return the associated key. This is a twist on the max algorithm since it is using a dictionary rather than a list. These are the steps:

# Define the function to accept one parameter for our dictionary
# Initialize the starting key to a very low number
# Initialize the starting value to a very low number
# Iterate through the dictionary’s key/value pairs.
# Inside the loop, if the current value is larger than the current largest value, replace the largest key and largest value with the current ones you are looking at
# Once you are done iterating through all key/value pairs, return the key which has the largest value

# Write your max_key function here:
def max_key(my_dictionnary):
  starting_key = 1
  starting_value = 1
  for key,value in my_dictionnary.items():
    if value > starting_value:
      starting_value = value
      starting_key = key
  return starting_key

# Uncomment these function calls to test your  function:
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"