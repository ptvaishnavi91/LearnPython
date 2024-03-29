# Python for DQE Functions Home task

#Module 2
# List of random number of dicts (from 2 to 10)
#Dict's random numbers of keys should be letter dict's values should be a number (0-100)
if __name__ == '__main__':
    print("Module 2 Collections: Listing random number of dicts and final dict with keys and values:\n")
    import random
    random_dict = dict()



def random_func():
    from random import choice, randint
    from string import ascii_lowercase
    ascii_lower = ascii_lowercase
    random_list = [{choice(ascii_lower): randint(0, 100) for i in range(len(ascii_lower))} for j in range(2,10)]
    return random_list
    if __name__ == '__main__':
        print("random list:\n" , random_func())

def keys_func():
    keys_list = []
    for i in random_func():
        for k in i.keys():
            keys_list.append(k)
    return keys_list

def unique_key_func():
    unique_keys = set(keys_func())
    return unique_keys

def multiple_occurrence_func():
    multiple_occurrence_list = [key for key in unique_key_func() if keys_func().count(key) > 1]
    return multiple_occurrence_list

#Now choose only the biggest one
def final_func():
    final_dict = {}
    for key in unique_key_func():
        # Checking if the key occurs in more than one dictionary
        if key in multiple_occurrence_func():
            # Finding the maximum value of the key among all dictionaries and the index
            max_value = float('-inf')
            max_dict_index = -1
            for i, d in enumerate(random_func()):
                if key in d:
                    if d[key] > max_value:
                        max_value = d[key]
                        max_dict_index = i
                # Adding the index to the key and add it to the final dictionary
            final_dict[key + "_" + str(max_dict_index + 1)] = max_value
        else:
            # If the key occurs in only one dictionary, add it to the final dictionary as is
            for d in random_func():
                if key in d:
                    final_dict[key] = d[key]
                    if __name__ == '__main__':
                        print(final_dict)
                    break
    return final_dict

if __name__ == '__main__':
    print("final_dict:\n",final_func())


#Module 3
if __name__ == '__main__':
    print("\n\nModule 3 Strings: Normalize multiline string, append and replace values, count whitespace\n")
# 1. This is your homework, copy these text to variable.

homework = """homEwork:

  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# 2. You need to normalize it from letter cases point of view.

def norm_func(text):
    normalized_text = []
    Sentence = text.splitlines()
    for i in range(0, len(Sentence)):
        Line = Sentence[i].strip(' ').capitalize()
        normalized_text.append(Line)
    Task = '\n'.join(normalized_text)
    return Task

# 3. Create one more sentence with last words of each existing sentence and add it to the end of this paragraph.

def new_line():
    Tasklist = (norm_func(homework).split('.'))
    Lastwords = []
    for i in range(0, len(Tasklist)):
        a = (Tasklist[i].split(' ')[-1])
        Lastwords.append(a)
    New_sentence = ' '.join(Lastwords).capitalize()
    return New_sentence


# 4. It is misspelling here. fix“iz” with correct “is”, but only when it is a mistake.

def replace_func(old,new):
    result = norm_func(homework).replace(old,new)
    return result

def replaced_func(old,new):
    replaced_line = replace_func(' iz ', ' is ')
    replaced_line.replace(old,new)
    return  replaced_line

new_text = replaced_func(' Iz ', ' Is ')


# 5. Last is to calculate number of whitespace characters in this tex. carefull, not only spaces, but all whitespaces
def whitespace_func():
    whitespace_count = 0
    for i in norm_func(homework):
        if i.isspace():
            whitespace_count = whitespace_count+1
    return whitespace_count

if __name__ == '__main__':
    print(f"{new_text}\n{new_line()}")

    print("\nTotal number of whitespaces:", whitespace_func())
