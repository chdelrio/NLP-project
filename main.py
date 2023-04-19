import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.corpus import words

words = words.words()

def sentence_correction(sentence):
    tokens = word_tokenize(sentence)
    corrected_tokens = []

    for token in tokens:
        if token in words:
            corrected_tokens.append(token)
        else:
            closest_word = min(words, key=lambda w: nltk.edit_distance(token, w))
            corrected_tokens.append(closest_word)

    corrected_sentence = ' '.join(corrected_tokens)
    return corrected_sentence

user_input = input("Enter a sentence to be corrected: \n")

corrected_input = sentence_correction(user_input.lower())
print("Corrected sentence:", corrected_input)

