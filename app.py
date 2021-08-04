from textblob import TextBlob
from spellchecker import SpellChecker


a = input('Enter an Incorrect String : ')
print('Original Text : ' + str(a))
b = TextBlob(a)
print('Corrected Text : ' + str(b.correct()))


spell = SpellChecker()
# Find those words that may be misspelled
misspelled = spell.unknown(['Good', 'Evening'])

for word in misspelled:
    # getting the one `most likely` answer
    print(spell.correction(word))
    # getting a list of `likely` options
    print(spell.candidates(word))
