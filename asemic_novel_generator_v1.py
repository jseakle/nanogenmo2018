from string import lowercase, uppercase
import random

word_end_punc = [',', ',', ',', ',', ',', ' -', ' -', ':', ' &', ';']
sentence_end_punc = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '!', '?', '...']
word_punc = ['^', '-', '\'', '/', '\'', '~']

vowels = ['aeiou']

lexicon = []

chapter_lengths = [1, 5, 7, 11, 15, 18, 20, 25, 26, 27, 28, 29, 29, 30, 30, 31, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
para_lengths = [1, 1, 1, 1, 1, 2, 3, 4, 4, 4, 5, 5, 6, 7]
sentence_lengths = [3, 4, 5, 5, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 10, 11, 12, 13, 14, 15]
word_lengths = [1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 24]


novel_length = 0

def word():
    global novel_length
    novel_length += 1
    
    if len(lexicon) > 0 and random.random() < float(len(lexicon)) / 10000:
        if random.random() < .1:
            return random.choice(lexicon[:25])
        if random.random() < .2:
            return random.choice(lexicon[:100])
        if random.random() < .5:
            return random.choice(lexicon[:500])
        return random.choice(lexicon)
    
    length = random.choice(word_lengths)
    if random.random() < .002:
        out = random.choice(uppercase)
    else:
        out = random.choice(lowercase)
    for i in xrange(length):
        if random.random() < .001:
            out += random.choice(word_punc)
        elif random.random() < .2:
            out += random.choice(vowels)
        else:
            out += random.choice(lowercase)

    lexicon.append(out)

    return out

def sentence():
    length = random.choice(sentence_lengths) - 1
    first = word()
    out = [first[0].upper() + first[1:]]

    for i in xrange(length):
        next_word = word()
        if random.random() < .03:
            next_word += random.choice(word_end_punc)

    return ' '.join(out) + random.choice(sentence_end_punc) + ' '


def paragraph():
    length = random.choice(para_lengths)

    out = "\t"
    for i in xrange(length):
        out += sentence()
    return out + "\n"


def chapter(n):
    length = random.choice(chapter_lengths)

    out = "\t\t\t\t\t{}\n\n".format(n)
    for i in xrange(length):
        out += paragraph()
    return out + "\n\n\t\t\t\t       ~*~\n\n"

chap = 1
while novel_length < 50000:
    print chapter(chap),
    chap += 1
    

