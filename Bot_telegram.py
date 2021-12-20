from urllib.request import urlopen
from bs4 import BeautifulSoup
import telepot
from telepot.loop import MessageLoop
import time
from random import randint
from Telegram_bot import TOKEN

API = TOKEN

def inicio(msg):
    chat_id = telepot.glance(msg)
    bot.sendMessage(chat_id, 'O que gostaria de saber mestre?')

def monitora(msg):
    lista = open('lista.txt', 'r')
    lista = lista.read()
    lista = lista.split()
    n = len(lista) - 1
    print(n, ' Lista')
    i = randint(0,n)
    print(i)
    tipo1, tipo2, chat_id = telepot.glance(msg)
    bot.sendMessage(chat_id, lista[i])
    add = open('lista.txt', 'a')
    add.write(msg['text']+'\n')

pages = set()
def getlinks(msg):
    global pages
    html = urlopen('https://www.google.com/search?q=cotação+{}'.format(msg))
    s = BeautifulSoup(html, 'html.parser')

    try:
        x = s.find('div', attrs={'class': 'mw-parser-output'})
        return 'sucesso'

    except AttributeError:
        print('Esta pagina não existe')

    



bot = telepot.Bot(API)

MessageLoop(bot, monitora).run_as_thread()

while 1:
    time.sleep(10)

