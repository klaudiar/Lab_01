def line_count(file_name):
    # Plik do odczytu
    while True:
        try:
            file = open(file_name, 'r')
            break
        except IOError:
            # Zla nazwa pliku, wczytanie nowej
            print("No such file in this localisation")
            file_name = input("Write proper file name: ")
            print("\n")

    # Czytanie linii
    while True:
        try:
            lines = file.readlines()
            break
        except UnicodeError:
            # Nie mozna odczytac pliku
            # prawdopodobnie zly typ pliku, wczytanie nowej nazwy
            print("Wrong file extension")
            file_name = input("Write proper file name: ")
            print("\n")
            while 1:
                try:
                    file = open(file_name, 'r')
                    break
                except FileNotFoundError:
                    # Zla nazwa pliku, wczytanie nowej
                    print("No such file in this localisation")
                    file_name = input("Write proper file name: ")
                    print("\n")

    file_write = open('count_answer.txt', 'w')

    if len(lines)==0:
        print("This file is empty!")
        file_write.write("File %s is empty!" % file_name)
    else:
        print("%s \n This text contain %d lines" % (lines, len(lines)))
        file_write.write("Text from file %s contain %d lines" % (file_name, len(lines)))

    # Zamkniecie pliku
    file.close()
    file_write.close()
    return len(lines)