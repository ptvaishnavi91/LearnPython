#Python for DQE String Home task

# 1. This is your homework, copy these text to variable.

homework = """
homEwork:

  tHis iz your homeWork, copy these Text to variable.

 

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

 

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

 

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# 2. You need to normalize it from letter cases point of view.
normalized_text = []
Sentence = homework.splitlines()
for i in range(0, len(Sentence)):
    Line = Sentence[i].strip(' ').capitalize()
    normalized_text.append(Line)
Task = '\n'.join(normalized_text)

# 3. Create one more sentence with last words of each existing sentence and add it to the end of this paragraph.
Tasklist = (Task.split('.'))
Lastwords = []
for i in range(0, len(Tasklist)):
    a = (Tasklist[i].split(' ')[-1])
    Lastwords.append(a)
New_sentence = ' '.join(Lastwords).capitalize()
Task = f"{Task}\n\n{New_sentence}"

# 4. It is misspelling here. fix“iz” with correct “is”, but only when it is a mistake.

result1 = Task.replace(' iz ', ' is ')
print(result1.replace(' Iz ', ' Is '))

# 5. Last is to calculate number of whitespace characters in this tex. carefull, not only spaces, but all whitespaces

whitespace_count = 0
for i in Task:
    if i.isspace():
        whitespace_count = whitespace_count+1
        
        
print("\nTotal number of whitespaces:", whitespace_count)

