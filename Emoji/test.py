import unittest
from hate_speech import *


hate=['you are stupid','you are a fucking idiot']

normal=['hi how are you','you are a kind person']


class TestStringMethods(unittest.TestCase):
    def test_hate(self):
        for sentence in hate:
            sentence=emoticon(sentence)
            stemmed = stemSentence(sentence)
            sentence=[stemmed]

            sentence = vectorizer.transform(sentence)
            self.assertEqual(model.predict(sentence),0)
            
    def test_normal(self):
        for sentence in normal:
            sentence=emoticon(sentence)
            stemmed = stemSentence(sentence)
            sentence=[stemmed]

            sentence = vectorizer.transform(sentence)
            self.assertEqual(model.predict(sentence),1)
  
if __name__ == '__main__':
    unittest.main()
