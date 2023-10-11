import string, phonetic, accentuation.stress
from nltk import word_tokenize
from nltk.probability import FreqDist


def split_by_sound(word, dict):
    newline = ''
    for letter in word:
        if letter == "'":
            if newline + letter not in dict:
                dict[newline + letter] = 0
            dict[newline + letter] += 1
            dict[newline] -= 1
        else:
            if newline + letter not in dict:
                dict[letter] = 0
            dict[letter] += 1
        newline = letter
    return dict


def show_frequency_of_sounds(text, amount=20, label=''):
    text = accentuation.stress.to_sound(text)
    words = text.split(' ')
    dict = {}
    for word in words:
        try:
            index = phonetic.get_index(word)
            result = phonetic.text_to_phonetic(word.lower(), index)

            dict = split_by_sound(result.get_phonetic(), dict)

        except Exception:
            pass

    fdist = FreqDist(dict)
    print(fdist.most_common(amount))
    fdist.plot(amount, cumulative=False, title=label)


def show_frequency_of_words(text, amount=70, label=''):
    text_tokens = phonetic.normalize_words(word_tokenize(text))

    from nltk.corpus import stopwords
    russian_stopwords = stopwords.words("russian")

    text_tokens = [token.strip() for token in text_tokens if token not in russian_stopwords]
    fdist = FreqDist(text_tokens)
    print(fdist.most_common(amount))

    fdist.plot(amount, cumulative=False, title=label)


def show_frequency_of_letters(text, amount=32):
    word_tokens = text.replace(' ', '')
    fdist = FreqDist(word_tokens)

    print(fdist.most_common(amount))
    fdist.plot(30, cumulative=False)


def remove_chars_from_text(input, chars):
    return "".join([ch for ch in input if ch not in chars])


def parse_file(filename):
    input_file = open(filename, 'r', encoding='utf-8')
    text, index = input_file.read(), input_file.read().find('.')

    label = text[:text.find('.')]

    text = text[text.find('.'):].lower()
    text = text.replace('\n', ' ')
    spec_chars = string.punctuation + '\xa0«»\t—…№–' + string.digits
    text = remove_chars_from_text(text, spec_chars)

    return text, label


# text, label = parse_file('south.txt')
# show_frequence_of_letters(text, 15, label)
# show_frequence_of_words(text, label = label)

text, label = parse_file('texts/text.txt')
# show_frequency_of_letters(text)
show_frequency_of_sounds(text, label = label)
