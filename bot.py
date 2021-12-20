import json, sys, os
import subprocess as sp
from urllib.request import urlopen
from bs4 import BeautifulSoup
from pandas import DataFrame

class Uma():
    def __init__(self, name):
        try:
            memory = open(name+'.json', 'r')
        except FileNotFoundError:
            memory = open(name+'.json', 'w')
            memory.write('[["Uma"], {"Oi": "Olá! Qual seu nome?", "tchau": "Tchau! Tchau!"}]')
            memory.close()
            memory = open(name+'.json', 'r')
        self.name = name
        self.known, self.phrases = json.load(memory)
        memory.close()
        self.historic = [None]
    def listen(self, phrase=None):
        if phrase == None:
            phrase = input('>: ')
        phrase = str(phrase)
#        phrase = phrase.lower()
        return phrase
    
    def think(self, phrase):
        url_base = 'https://pt.wikipedia.org/wiki/Dinheiro'
        def request_data(url, tag, attr):
            html = urlopen(url)
            bs = BeautifulSoup(html, 'html.parser')
            data = bs.find_all(tag, {"class": attr})
            return data
        if phrase in self.phrases:
            return self.phrases[phrase]
        if phrase == 'Aprende':
            return 'O que você quer que eu aprenda?'
        if phrase == 'valor':
            data = request_data(url_base, 'div', 'mw-parser-output"')
            print(data, '>>> SITE')
        
        # historic
        lastPhrase = self.historic[-1]
        if lastPhrase == 'Olá! Qual seu nome?':
            name = self.getName(phrase)
            response = self.answerName(name)
            return response
        if lastPhrase == 'O que você quer que eu aprenda?':
            self.key = phrase
            return 'Digite o que eu devo responder:'
        if lastPhrase == 'Digite o que eu devo responder:':
            response = phrase
            self.phrases[self.key] = response
            self.saveMemory()
            return 'Aprendido!'
        try:
            response = str(eval(phrase))
            return response
        except:
            pass
        return 'Não entendi...'
    def getName(self, name):
        if 'Meu nome é ' in name:
            name = name[12:]
        name = name.title()
        return name
    def answerName(self, name):
        if name in self.known:
            if name != 'Uma':
                phrase = 'Eaew, '
            else:
                phrase = 'Eu sou um elfo sabio que foi amaldiçoado me tornando o homem mais feio do mundo'
        else:
            phrase = 'Muito prazer '
            self.known.append(name)
            self.saveMemory()
        return phrase + name + '!'
    def saveMemory(self):
        memory = open(self.name+'.json', 'w')
        json.dump([self.known, self.phrases], memory)
        memory.close()
    def speak(self, phrase):
        if 'Executa ' in phrase:
            platform = sys.platform
            command = phrase.replace('Executa ', '')
            if 'win' in platform:
                os.startfile(command)
            if 'linux' in platform:
                try:
                    sp.Popen(command)
                except FileNotFoundError:
                    sp.Popen(['xdg-open', command])
        else:
            print(phrase)
        self.historic.append(phrase)