def word_count(file_name):
    # Plik do odczytu
    while True:
        try:
            file = open(file_name, 'r')
            break
        except IOError:
            # Zla nazwa pliku, wczytanie nowej
            print("No such file in this localisation")
            file = input("Write proper file name: ")
            print("\n")

    # Czytanie slow
    while True:
        try:
            text = file.read()
            break
        except UnicodeError:
            # Nie mozna odczytac pliku
            # prawdopodobnie zly typ pliku
            # wczytanie nowej nazwy
            print("Wrong file extension")
            file_name = input("Write proper file name: ")
            print("\n")
            while True:
                try:
                    file = open(file_name, 'r')
                    break
                except FileNotFoundError:
                    # Zla nazwa pliku, wczytanie nowej
                    print("No such file in this localisation")
                    file_name = input("WWrite proper file name: ")
                    print("\n")

    file_write = open('count_answer.txt', 'w')

    if len(text)==0:
        print("This file is empty!")
        file_write.write("File %s is empty!" % file_name)
    else:
        words = text.split()
        print("%s \n This text contain %d words" % (words, len(words)))
        file_write.write("Text from file %s contain %d words" % (file_name, len(words)))

    # Zamkniecie pliku
    file.close()
    file_write.close()
    return len(words)