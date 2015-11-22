import optparse as o

##Tworzymy opcje##
parser = o.OptionParser("OptionParser.py [options] file_name.txt")

# Wybranie opcji liczenia slow
parser.add_option("-w", "--words", type="string", help="count words\t -w \"filename.txt\"", dest="words", action="store",
                  default="non")

# Wybranie opcji liczenia linii
parser.add_option("-l", "--lines", type="string", help="count lines\t -l \"filename.txt\"", dest="lines", action="store",
                  default="non")
(opc, args) = parser.parse_args()  # sys.argv[1:])

# Przekazanie argumentow
filel = opc.lines
filew = opc.words

#print("Opcje: %s, argumenty: %s, plik slowa: %s, plik linie: %s\n" % (opc, args, filew, filel))

# Wyjatek od liczby argumentow i przekazanie nazwy pliku
if (filew == "non" and opc.lines == "non") or (filew != "non" and opc.lines != "non"):
    parser.erros("niepoprawna liczba argumentow")
elif filew != "non" and filel == "non":
    file = filew
    print("wybrales liczenie SLOW\n")
elif filew == "non" and filel != "non":
    file = filel
    print("wybrales liczenie LINII\n")

#Nazwa pliku
print("plik do odczytu: %s\n" % (file))

# Plik do odczytu
while 1:
    try:
        f = open(file, 'r')
        break
    except FileNotFoundError:
        ###Zla nazwa pliku, wczytanie nowej
        print("Nie ma takiego pliku w tej lokalizacji")
        file = input("Wprowadz poprawna nazwe pliku: ")
        print("\n")


if filel != "non":
    #Czytanie linii
    while 1:
        try:
            lines = f.readlines()
            break
        except UnicodeError:
            ###Nie mozna odczytac pliku
            ###prawdopodobnie zly typ pliku
            ###wczytanie nowej nazwy
            print("Ten program nie obsluguje takiego typu rozszerzenia")
            file = input("Wprowadz inny plik: ")
            print("\n")
            while 1:
                try:
                    f = open(file, 'r')
                    break
                except FileNotFoundError:
                    ###Zla nazwa pliku, wczytanie nowej
                    print("Nie ma takiego pliku w tej lokalizacji")
                    file = input("Wprowadz poprawna nazwe pliku: ")
                    print("\n")
    if len(lines)==0:
        print("Ten plik jest pusty!")
    else: print("%s \n Ten tekst zawiera %d linii" % (lines, len(lines)))

elif filew != "non":
    #Czytanie slow
    while 1:
        try:
            text = f.read()
            break
        except UnicodeError:
            ###Nie mozna odczytac pliku
            ###prawdopodobnie zly typ pliku
            ###wczytanie nowej nazwy
            print("Ten program nie obsluguje takiego typu rozszerzenia")
            file = input("Wprowadz inny plik: ")
            print("\n")
            while 1:
                try:
                    f = open(file, 'r')
                    break
                except FileNotFoundError:
                    ###Zla nazwa pliku, wczytanie nowej
                    print("Nie ma takiego pliku w tej lokalizacji")
                    file = input("Wprowadz poprawna nazwe pliku: ")
                    print("\n")
    if len(text)==0:
        print("Ten plik jest pusty!")
    else:
        words = text.split()
        print("%s \n Ten tekst zawiera %d slow" % (words, len(words)))

#Zamkniecie pliku
f.close()
