# Create a function named larger_sum() that takes two lists of numbers as parameters named lst1 and lst2.

# The function should return the list whose elements sum to the greater number. If the sum of the elements of each list are equal, return lst1.

#Write your function here
def larger_sum(lst1, lst2):
  sum_lst1 = 0
  sum_lst2 = 0
  for index in lst1:
    sum_lst1 += index
  for index in lst2:
    sum_lst2 += index
  if sum_lst1 >= sum_lst2:
    return lst1
  return lst2

#   Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))

# Create a function named over_nine_thousand() that takes a list of numbers named lst as a parameter.

# The function should sum the elements of the list until the sum is greater than 9000. When this happens, the function should return the sum. If the sum of all of the elements is never greater than 9000, the function should return total sum of all the elements. If the list is empty, the function should return 0.

# For example, if lst was [8000, 900, 120, 5000], then the function should return 9020.

#Write your function here
def over_nine_thousand(lst):
  sum = 0
  for number in lst:
    sum += number
    if sum > 9000:
      break
  return sum
    

#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))

# Create a function named max_num() that takes a list of numbers named nums as a parameter.

# The function should return the largest number in nums

#Write your function here
def max_num(num):
  max = num[0]
  for numbers in num:
    if numbers > max:
        max = numbers
  return max

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))

# Write a function named same_values() that takes two lists of numbers of equal size as parameters.

# The function should return a list of the indices where the values were equal in lst1 and lst2.

# For example, the following code should return [0, 2, 3]

#Write your function here
def same_values(lst1, lst2):
  new_lst = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      new_lst.append(index)
  return new_lst

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

# Create a function named reversed_list() that takes two lists of the same size as parameters named lst1 and lst2.

# The function should return True if lst1 is the same as lst2 reversed. The function should return False otherwise.

# For example, reversed_list([1, 2, 3], [3, 2, 1]) should return True.

#Write your function here
def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True

#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))

