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

def letters_stats(txt):
    text = txt
    letter_counts = {}
    upper_counts = {}
    total_letters = 0

    # Loop through each character in the text
    for char in text:
        if char.isalpha():
            # If the character is a letter, add it to the letter count
            total_letters += 1
            if char.isupper():
                # If the character is uppercase, increment the uppercase count for that letter
                if char in upper_counts:
                    upper_counts[char] += 1
                else:
                    upper_counts[char] = 1
            # Add the letter to the letter count dictionary
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1

    # Write results to CSV file
    with open('letter_stats.csv', mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(['Letter', 'Count', 'Uppercase Count', 'Uppercase Percentage'])
        for letter, count in letter_counts.items():
            if letter != ' ':
                upper_count = upper_counts.get(letter, 0)
                upper_percentage = upper_count / count * 100 if count > 0 else 0
                writer.writerow([letter, count, upper_count, "{:.2f}%".format(upper_percentage)])

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

letters_stats(content)
