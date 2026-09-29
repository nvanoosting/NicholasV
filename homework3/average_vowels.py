# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()

# Hint: You can use .isalpha() to check if a character is a letter.

# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()

# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 

def naming_vowels_and_consonants(text):
    vowels = "aeiouy"
    vowels_count = 0
    consonants_count = 0
    for char in text:
        if char.isalpha():
            if char in vowels:
               vowels_count += 1
            else:
               consonants_count += 1
    return (vowels_count, consonants_count)

def average_vowels_and_consonants(text):
    punctuation = "!?."
    total_sentances = 0
    total_vowels = 0
    total_consonants = 0
    sentance = ""
    function_output = None
    for char in text:
        if char in punctuation:
            total_sentances += 1
            function_output = naming_vowels_and_consonants(sentance)
            total_vowels += function_output[0]
            total_consonants += function_output[1]
            sentance = ""

        else:
            sentance += char
    return (total_sentances, total_vowels // total_sentances, total_consonants // total_sentances)

final_result_paragraph = average_vowels_and_consonants(paragraph)
print(f"Total Sentances:{final_result_paragraph[0]} , Average Number of Vowels:{final_result_paragraph[1]} , Average Number of Consonants:{final_result_paragraph[2]}")