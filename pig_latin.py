def is_vowel(ch):
    if ch in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        return True
    else:
        return False

def cut(word):
    if len(word) == 1:
        return (word, '')
    else:
        for n in range(0, len(word)):
            if is_vowel(word[n]):
                return (word[:n], word[n:])
        
def piggify_word(word):
    if len(word) == 1:
        if is_vowel(word[0]):
            return word + 'hay'
        else:
            return word + 'ay'
    else:
        if is_vowel(word[0]):
            return word + 'hay'
        else:
            return cut(word)[1] + cut(word)[0] + 'ay'

def clean_word(raw_word):
    if len(raw_word) == 0:
        return ('')
    else:
        for n in range (0, len(raw_word)):
            if not raw_word[n].isalpha():
                return (raw_word[:n], raw_word[n:])
            
    return (raw_word, '')

def get_raw_words (sentence):
    return sentence.split()

def piggify_pairs(pair_list):
    new_list = []
    for n in range (0, len(pair_list)):
        pig_word = piggify_word(pair_list[n][0])
        add_punctuation = (pig_word, pair_list[n][1])
        new_list.append(add_punctuation)
        
    return new_list

def reassemble(pair_list):
    sentence = ''
    for n in range(0, len(pair_list)):
        if n == (len(pair_list) - 1):
            sentence += pair_list[n][0] + pair_list[n][1]
        else:
            sentence += pair_list[n][0] + pair_list[n][1] + ' '

    return sentence

def piggify_sentence(sentence):
    clean_list = []
    for n in get_raw_words(sentence):
        clean_list.append(clean_word(n))
        
    return reassemble(piggify_pairs(clean_list))

def main():
    sentence = input('Please enter your sentence to be translated into Pig Latin: ')
    print (piggify_sentence(sentence))

if __name__ == "__main__":
    main()
