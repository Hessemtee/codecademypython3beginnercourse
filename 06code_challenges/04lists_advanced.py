# Create a function called every_three_nums that has one parameter named start.

# The function should return a list of every third number between start and 100 (inclusive). For example, every_three_nums(91) should return the list [91, 94, 97, 100]. If start is greater than 100, the function should return an empty list.

#Write your function here
def every_three_nums(start):
  return list(range(start, 101, 3))

#Uncomment the line below when your function is done
print(every_three_nums(91))

# Create a function named remove_middle which has three parameters named lst, start, and end.

# The function should return a list where all elements in lst with an index between start and end (inclusive) have been removed.

# For example, the following code should return [4, 23, 42] because elements at indices 1, 2, and 3 have been removed:

#Write your function here
def remove_middle(lst, start, end):
  return lst[:start] + lst[end+1:]

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

# Create a function named more_frequent_item that has three parameters named lst, item1, and item2.

# Return either item1 or item2 depending on which item appears more often in lst.

# If the two items appear the same number of times, return item1.

#Write your function here
def more_frequent_item(lst, item1, item2):
  if lst.count(item2) > lst.count(item1):
    return item2
  return item1
#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

# Create a function named double_index that has two parameters: a list named lst and a single number named index.

# The function should return a new list where all elements are the same as in lst except for the element at index. The element at index should be double the value of the element at index of the original lst.

# If index is not a valid index, the function should return the original list.

# For example, the following code should return [1,2,6,4] because the element at index 2 has been doubled:

#Write your function here
def double_index(lst, index):
  if index > len(lst):
    return lst
  else:
   lst2 = lst[0:index]
   lst2.append(lst[index] * 2)
   lst2 = lst2 + lst[index+1:]
   return lst2

#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))


# Create a function called middle_element that has one parameter named lst.

# If there are an odd number of elements in lst, the function should return the middle element. If there are an even number of elements, the function should return the average of the middle two elements.

#Write your function here
def middle_element(lst):
  if len(lst) % 2 != 0:
    return lst[int(len(lst) / 2 )]
  else:
    return (lst[int(len(lst) / 2)] + lst[int(len(lst) / 2) - 1]) / 2

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))