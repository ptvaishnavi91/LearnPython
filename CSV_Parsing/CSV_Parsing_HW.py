import csv


def words_count(text):
    counts = dict()
    words = text.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


def letters_count(txt):
    letters_dict = {"letter":[],"occurence":[], "upper_count":[], "percentage":[]}
    total_count = 0
    upper_count = 0
    upper_letters = []
    for i in txt:
        print('i=', i)
        print(letters_dict["letter"])
        if i.isupper() and i.lower() in letters_dict["letter"] and i in upper_letters:
            total_count +=1
            upper_count +=1
        elif i.isupper() and  i.lower() not in letters_dict["letter"]:
            total_count = 1
            upper_count = 1
            letters_dict["letter"].append(i.lower())
        elif not i.isupper() and  i.lower() in letters_dict["letter"]:
            total_count +=1
            upper_count = 0
        elif not i.isupper() and  i.lower() not in letters_dict["letter"]:
            total_count = 1
            upper_count = 0
            letters_dict["letter"].append(i.lower())
        letters_dict["occurence"].append(total_count)
        letters_dict["upper_count"].append(upper_count)
        percentage = (upper_count/total_count)*100
        letters_dict["percentage"].append(percentage)

    return letters_dict

with open('News_output.txt', 'r') as f:
    content = f.read()
   # print(content)
    global count_words
    count_words = words_count(content.lower())

# with open('word_count.csv', 'w', newline='') as f:
#     test_writer = csv.writer(f)
#     test_writer.writerow(['word', 'count'])
#     for key, value in count_words.items():
#         test_writer.writerow([key, value])


with open('letter_count.csv', 'w', newline='') as f:
    test_writer = csv.writer(f)
    test_writer.writerow(['letter', 'count', 'count_uppercase', 'percentage'])
    test_writer.writerow([ 'a', '4',  '2', '50'])

    # # print(count_words)
    letters_freq = letters_count('An apple A day')
    print('letters_freq\n', letters_freq)