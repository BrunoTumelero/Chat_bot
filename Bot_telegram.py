from urllib.request import urlopen
from bs4 import BeautifulSoup
import telepot
from telepot.loop import MessageLoop
import time



API = '2123518901:AAF19RESIsJpiq1d4B5dy0AJWC_EzhKT2sQ'

def inicio(msg):
    chat_id = telepot.glance(msg)
    bot.sendMessage(chat_id, 'O que gostaria de saber mestre?')

def monitora(msg):
    tipo1, tipo2, chat_id = telepot.glance(msg)
    bot.sendMessage(chat_id, msg['text'])

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

    



bot = telepot.Bot(API)

MessageLoop(bot, monitora).run_as_thread()

while 1:
    time.sleep(10)

