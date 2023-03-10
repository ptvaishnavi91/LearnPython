# List of random number of dicts (from 2 to 10)
""" Dict's random numbers of keys should be letter
dict's values should be a number (0-100)
"""
import random
from random import choice, randint
from string import ascii_lowercase

random_dict = dict()

random_list = [{choice(ascii_lowercase): randint(0, 100) for i in range(len(ascii_lowercase))} for j in range(2,10)]
print("random list:\n" , random_list)
keys_list = []
final_dict = {}

# Creating a list of all the keys in the dictionaries
for i in random_list:
    for k in i.keys():
        keys_list.append(k)

# Creating a set of unique keys
unique_keys = set(keys_list)
#print(unique_keys)

# Creating a list of keys that occur in more than one dictionary
multiple_occurrence_list = [key for key in unique_keys if keys_list.count(key) > 1]
#print(multiple_occurrence_list)

# Iterating over the set of unique keys
for key in unique_keys:
    # Checking if the key occurs in more than one dictionary
    if key in multiple_occurrence_list:
        # Finding the maximum value of the key among all dictionaries and the index
        max_value = float('-inf')
        max_dict_index = -1
        for i, d in enumerate(random_list):
            if key in d:
                if d[key] > max_value:
                    max_value = d[key]
                    max_dict_index = i
            # Adding the index to the key and add it to the final dictionary
        final_dict[key + "_" + str(max_dict_index + 1)] = max_value
    else:
        # If the key occurs in only one dictionary, add it to the final dictionary as is
        for d in random_list:
            if key in d:
                final_dict[key] = d[key]
                print(final_dict)
                break

# Print the final dictionary
print("\nFinal Dictionary:\n", final_dict)
