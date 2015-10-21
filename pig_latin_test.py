import unittest
from pig_latin import *

class testPigLatin(unittest.TestCase):

    def test_is_vowel(self):
        self.assertEqual(is_vowel('T'), False)
        self.assertEqual(is_vowel('o'), True)
        self.assertEqual(is_vowel('n'), False)
        self.assertEqual(is_vowel('I'), True)

    def test_cut(self):
        self.assertEqual(cut('string'),('str','ing'))
        self.assertEqual(cut('Facebook'),('F','acebook'))
        self.assertEqual(cut('Apple'),('','Apple'))
        self.assertEqual(cut('GOOGLE'),('G','OOGLE'))
        self.assertEqual(cut('AEIOU'),('','AEIOU'))

    def test_piggify_word(self):
        self.assertEqual(piggify_word('b'),'bay')
        self.assertEqual(piggify_word('E'),'Ehay')
        self.assertEqual(piggify_word('Hello'),'elloHay')
        self.assertEqual(piggify_word('AWESOME'),'AWESOMEhay')

    def test_clean_word(self):
        self.assertEqual(clean_word('Hello!'), ('Hello', '!'))
        self.assertEqual(clean_word('Name ?'), ('Name', ' ?'))
        self.assertEqual(clean_word('a'), ('a', ''))

    def test_get_raw_words(self):
        self.assertEqual(get_raw_words('GO BLUE!'), (['GO', 'BLUE!']))
        self.assertEqual(get_raw_words('Michigan! Wolverines!'), (['Michigan!', 'Wolverines!']))
        self.assertEqual(get_raw_words('? ! #'), (['?', '!', '#']))

    def test_piggify_pairs(self):
        self.assertEqual(piggify_pairs([('Go', ''), ("Blue", '!')]), ([('oGay', ''), ('ueBlay', '!')]))
        self.assertEqual(piggify_pairs([('How', ''), ('are', ''), ('you', ''),('doing', '?')]), ([('owHay', ''), ('arehay', ''),('ouyay', ''),('oingday','?')]))

    def test_reassemble(self):
        self.assertEqual(reassemble([('eyHay', '!'), ('ouyay', '!')]),('eyHay! ouyay!'))
        self.assertEqual(reassemble([('Agehay', '3'), ('earyay', '3')]),('Agehay3 earyay3'))

    def test_piggify_sentence(self):
        self.assertEqual(piggify_sentence('We are the champion!'), ('eWay arehay ethay ampionchay!'))
        self.assertEqual(piggify_sentence('A! B! O! U!'), ('Ahay! Bay! Ohay! Uhay!'))

unittest.main()
