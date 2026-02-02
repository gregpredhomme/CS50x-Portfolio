from cs50 import get_string

text = get_string("Text: ")

letters = 0
sentences = 0
words = len(text.split())

for char in text:
    if char.isalpha():
        letters += 1
    elif char in ['.', '!', '?']:
        sentences += 1

L = (letters / words) * 100
S = (sentences / words) * 100

index = 0.0588 * L - 0.296 * S - 15.8
grade = round(index)

if grade >= 16:
    print("Grade 16+")
elif grade < 1:
    print("Before Grade 1")
else:
    print(f"Grade {grade}")
