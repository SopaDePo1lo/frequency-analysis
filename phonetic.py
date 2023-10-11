import pymorphy2
from RusPhonetic import phonetic_module
morph = pymorphy2.MorphAnalyzer()

vowels = ['а', 'я', 'у', 'ю', 'о', 'е', 'э', 'и', 'ы', 'ё']
not_accented = ['а́', 'я́', 'у́', 'ю́', 'о́', 'е́', 'э́', 'и́', 'ы́', 'ё́']
accented = ['А', 'Я', 'У', 'Ю', 'О', 'Е', 'Э', 'И', 'Ы', 'Ё']


def normalize_words(list):
    for i in range(len(list)):
        result = morph.parse(list[i])
        list[i] = result[0].normal_form
    return list


def remove_vowels(input):
    output = ''
    for letter in input:
        if letter in accented or letter in vowels:
            output += letter
    return output


def replace_characters(original, new, str):
    for i in range(len(original) - 1):
        str = str.replace(original[i], new[i])
    return str


def get_index(input):
    index = 1
    if len(input) == 0 or len(input) == 1:
        return
    only_phonetic = remove_vowels(input)
    for letter in only_phonetic:
        if letter in accented:
            return index
        index += 1
    return 100


def text_to_phonetic(text, index):
    if index == 100:
        index = 1
    if index is None:
        index = 1
        return phonetic_module.Phonetic(text, index)
    else:
        return phonetic_module.Phonetic(text, index)
