import csv

def words_count(text):
    # Looping through the text to find the occurrence of each word in the text
    counts = dict()
    words = text.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

def letters_count( letter_counts):
    count_of_letters = []
    total_count = len(letter_counts)
    for char in letter_counts:
        if char != ' ' and char.isalpha():
            total = letter_counts.count(char.lower())
            upper_count = letter_counts.count(char.upper())
            percentage = ((total + upper_count) / total_count) * 100
            count_of_letters.append((char.lower(), total + upper_count, upper_count, percentage))
    count_of_letters = list(dict.fromkeys(count_of_letters))

    with open('letter_count.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['letter', 'total_count', 'upper_count', 'percentage'])
        for letter, total, upper, percentage in count_of_letters:
            writer.writerow([letter, total, upper, percentage])

#Taking the News output file as the input text
with open('News_output.txt', 'r') as f:
    content = f.read()
    global count_words
    count_words = words_count(content.lower())

# Creating output csv for words count
with open('word_count.csv', 'w', newline='') as f:
    test_writer = csv.writer(f)
    test_writer.writerow(['word', 'count'])
    for key, value in count_words.items():
        if key.isalpha():
            test_writer.writerow([key, value])

letters_count(content)
