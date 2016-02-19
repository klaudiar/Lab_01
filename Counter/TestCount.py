import unittest
from line_count import *
from word_count import *

class TestCount(unittest.TestCase):

    def testCurrencyline_count(self):
        lines = line_count("dane.txt")
        assert lines != None and lines >=0, "line_count failed, wrong number of lines"

    def testCurrencyword_count(self):
        words = word_count("dane.txt")
        assert words != None and words >=0, "word_count failed, wrong number of lines"

    def testRightNumberOfLines(self):
        line_count("dane.txt")
        while True:
            try:
                file = open("count_answer.txt", 'r')
                break
            except IOError:
                print("No such file in this localisation")

        text_l = file.read()
        file.close()
        assert text_l == "Text from file dane.txt contain 7 lines", "line_count failed, wrong answer in the file"

    def testRightNumberOfWords(self):
        word_count("dane.txt")
        while True:
            try:
                file = open("count_answer.txt", 'r')
                break
            except IOError:
                print("No such file in this localisation")
        text_w = file.read()
        file.close()
        assert text_w == "Text from file dane.txt contain 23 words",  "word_count failed, wrong answer in the file"

if __name__ == "__main__":
    unittest.main()
