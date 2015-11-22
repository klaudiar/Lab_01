from xml.dom import minidom
import copy as c

__author__ = "KRogon"

class ParserXML:
    def __init__(self):

        str = ParserXML.__parser__()

        #print(str)
        print("_"*50)
        print('\tSpis tresci\n\n')

        for i in range(0,len(str)):
            print(i+1,'.\t',str[i]['title'])

        while 1:
            while 2:
                try:
                    x = int(input("\nWpisz numer ksiazki, ktorej dane chcesz uzyskac... "))-1
                    break
                except ValueError:
                    print('Podana liczba musi byc calkowita')
            if x>=1 and x<=12: break
            else: print('Musisz wybrać liczbe z zakresu od 1 do 12')

        print("\nTytul:\t\t\t%s\nAutor:\t\t\t%s\nGatunek:\t\t%s\nData publikacji:\t%s\nOpis:\t\t\t%s\nCena:\t\t\t%s\n\n"
              %(str[x]['title'],str[x]['author'],str[x]['genre'],str[x]['publish_date'],str[x]['description'],str[x]['price']))

    def __parser__():
        # otwiera plik XML w parserze
        DOMTree = minidom.parse("Books.xml")

        # odczyt danych
        #print("%s\n\n" % DOMTree.toxml())

        # pobieramy elementy struktury DOMTree
        cNodes = DOMTree.childNodes

        # Wez struktore
        le = len(cNodes[0].getElementsByTagName("book"))
        id=[]

        for n in range(0,le):
            id.append(cNodes[0].getElementsByTagName("book")[n].getAttribute("id"))

        # utworzenie pustych struktur dziecka i rodzica
        parent = {}
        dziecko = {}
        strukt = ()
        n = 0
        d = ('author', 'title', 'genre', 'price', 'publish_date', 'description')
        print("#"*50)
        for j in cNodes[0].getElementsByTagName("book"):
            dziecko[j.getElementsByTagName("author")[0].nodeName] = j.getElementsByTagName("author")[0].childNodes[0].toxml()
            dziecko[j.getElementsByTagName("title")[0].nodeName] = j.getElementsByTagName("title")[0].childNodes[0].toxml()
            dziecko[j.getElementsByTagName("genre")[0].nodeName] = j.getElementsByTagName("genre")[0].childNodes[0].toxml()
            dziecko[j.getElementsByTagName("price")[0].nodeName] = j.getElementsByTagName("price")[0].childNodes[0].toxml()
            dziecko[j.getElementsByTagName("publish_date")[0].nodeName] = j.getElementsByTagName("publish_date")[0].childNodes[0].toxml()
            dziecko[j.getElementsByTagName("description")[0].nodeName] = j.getElementsByTagName("description")[0].childNodes[0].toxml()

            # skopiowanie struktury pojedynczego dziecka
            parent[id[n]] = c.copy(dziecko)
            strukt += (c.copy(parent[id[n]]),)
            parent.clear()
            dziecko.clear()
            n=n+1

        return strukt

ParserXML()
