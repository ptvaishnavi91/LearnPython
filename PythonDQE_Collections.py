# List of random number of dicts (from 2 to 10)
""" Dict's random numbers of keys should be letter
dict's values should be a number (0-100)
"""
import random
from random import choice, randint
from string import ascii_lowercase
#final_dict, indexes_dict = {}, {}
random_dict = dict()
#for c in range(0, random_count[0]):
random_list = [{choice(ascii_lowercase): randint(0, 100) for i in range(len(ascii_lowercase))} for j in range(2,10)]
print("random list:\n" , random_list)

final_dict, tmp_dict = {},  {}

#Transform from list of dicts into dict of lists.
for dictionary in random_list:
  for k, v in dictionary.items():
    tmp_dict.setdefault(k, []).append(v)
#print("Tmp dict items:\n", tmp_dict.items())
#Now choose only the biggest one
for k, v in tmp_dict.items():
  if len(v) > 1:
    final_dict[k+"_"+str(v.index(max(v))+1)] = max(v)
  else: final_dict[k] = v[0]

print("final_dict:\n",final_dict)



