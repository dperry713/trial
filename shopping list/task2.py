def remove_from_list(my_list, item):
  """
  Removes the first occurrence of 'item' from the list 'my_list'

  Args:
      my_list: The list to remove the item from.
      item: The item to remove.
  """
  try:
      my_list.remove(item)
  except ValueError:
      # Item not found in the list
      pass  # Or you can raise your own exception here

my_list = [1, 2, 3, 4, 2]
remove_from_list(my_list, 2)
print(my_list)  # Output: [1, 3, 4, 2]