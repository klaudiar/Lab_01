from xml.dom import minidom
import copy as c

def parser_fun():
    # opens XML filein parser
    DOMTree = minidom.parse("Books.xml")
    # download DOMTree structure elements
    cNodes = DOMTree.childNodes
    id = []
    for n in range(0, len(cNodes[0].getElementsByTagName("book"))):
        id.append(cNodes[0].getElementsByTagName("book")[n].getAttribute("id"))

    parent = {}
    child = {}
    struct = ()
    n = 0
    descript = ('author', 'title', 'genre', 'price', 'publish_date', 'description')

    for j in cNodes[0].getElementsByTagName("book"):
        for i in descript:
            child[j.getElementsByTagName(i)[0].nodeName] = \
                j.getElementsByTagName(i)[0].childNodes[0].toxml()
        parent[id[n]] = c.copy(child)
        struct += (c.copy(parent[id[n]]),)
        parent.clear()
        child.clear()
        n = n+1

    return struct

def menuParser():
    while True:
        while True:
            try:
                x = int(input("\nWpisz numer ksiazki, ktorej dane chcesz uzyskac... "))
                break
            except ValueError:
                print('Podana liczba musi byc calkowita')
        if x >= 1 and x <= 12:
            break
        else:
            print("Musisz wybrac liczbe z zakresu od 1 do 12")
    return x-1