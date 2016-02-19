import unittest
from parser_fun import *

class TestCurrencyParsXML(unittest.TestCase):

    def testCurrencyExitparser_fun(self):
        struct = parser_fun()
        assert struct != None, "parser_fun failed, None argument returned"

    def testparser_fun(self):
        struct = parser_fun()
        number = 7
        assert struct[number]['title'] == "Creepy Crawlies" and struct[number]['author'] == "Knorr, Stefan"\
            and struct[number]['genre'] == "Horror" and struct[number]['publish_date'] == "2000-12-06"\
            and struct[number]['price'] == "4.95", "parser_fun failed, wrong titles to number of book"

if __name__ == "__main__":
    unittest.main()