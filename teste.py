from bs4 import BeautifulSoup
from urllib.request import urlopen
import json


pages = set()
def getlinks(pagesURL):
    global pages
    html = 'https://pt.wikipedia.org/wiki/{}'.format(pagesURL)
    s = BeautifulSoup(html, 'html.parser')
    print(html)
    try:
        #print(s.find(id= 'firstHeading'))
        #x = str(s.find(class_='mw-parser-output').find_all('p')[0])
        
        x = s.find('div', class_= 'mw-parser-output').find('p')
        print(x.text)

    except AttributeError:
        print('Esta pagina não existe')

    
getlinks('Poema')