import optparse as o
import word_count
import line_count


class Count:
    def __init__(self):
        self.count()

    def count(self):
        parser, opc = self.optionParser()

        # Przekazanie argumentow
        filel = opc.lines
        filew = opc.words

        # Wyjatek od liczby argumentow i przekazanie nazwy pliku
        if (filew == "non" and opc.lines == "non") or (filew != "non" and opc.lines != "non"):
            parser.error("niepoprawna liczba argumentow")
        elif filew != "non" and filel == "non":
            file = filew
            print("wybrales liczenie SLOW\n")
        elif filew == "non" and filel != "non":
            file = filel
            print("wybrales liczenie LINII\n")

        # Nazwa pliku
        print("plik do odczytu: %s\n" % file)

        if filel != "non":
            line_count.line_count(file)

        if filew != "non":
            word_count.word_count(file)

    def optionParser(self):
        # Tworzymy opcje##
        parser = o.OptionParser("OptionParser.py [options] file_name.txt")

        # Wybranie opcji liczenia slow
        parser.add_option("-w", "--words", type="string", help="count words\t -w \"filename.txt\"", dest="words",
                          action="store", default="non")

        # Wybranie opcji liczenia linii
        parser.add_option("-l", "--lines", type="string", help="count lines\t -l \"filename.txt\"", dest="lines",
                          action="store", default="non")
        (opc, args) = parser.parse_args()  # sys.argv[1:])
        return parser, opc


if __name__ == "__main__":
    Count()