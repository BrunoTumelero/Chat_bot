from bs4 import BeautifulSoup
from urllib.request import urlopen


pages = set()
def getlinks(pagesURL):
    global pages
    html = urlopen('https://pt.wikipedia.org/wiki/{}'.format(pagesURL))
    s = BeautifulSoup(html, 'html.parser')

    try:
        print(s.find(id= 'firstHeading'))
        print(s.find(class_='mw-parser-output').find_all('p'))
        print(s.find(class_='mw-parser-output').find_all('ul'))

    except AttributeError:
        print('Esta pagina não existe')

    

getlinks('Amigos')