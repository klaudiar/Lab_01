from parser_fun import *


class ParsXML:
    def __init__(self):
        self.book_datas()

    def book_datas(self):
        struct = parser_fun()

        print("_"*50)
        print('\tSpis tresci\n\n')

        for i in range(0, len(struct)):
            print(i+1, '.\t',struct[i]['title'])

        x = menuParser()

        print("\nTytul:\t\t\t%s\nAutor:\t\t\t%s\nGatunek:\t\t%s\nData publikacji:\t%s\nOpis:\t\t\t%s\nCena:\t\t\t%s\n\n"
              % (struct[x]['title'], struct[x]['author'], struct[x]['genre'], struct[x]['publish_date'],
                struct[x]['description'], struct[x]['price']))


if __name__ == "__main__":
    ParsXML()