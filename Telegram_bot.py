import json, time, telepot
from telepot.loop import MessageLoop
from bot import Uma

with open('token.json') as json_file:
    TOKEN =  json.load(json_file)

telegram = telepot.Bot(TOKEN)
bot = Uma("Memoria")
    
def handle(msg):
    phrase = bot.listen(phrase=msg['text'])
    response = bot.think(phrase)
    bot.speak(response)
    msgType, chatType, chatID = telepot.glance(msg)
    telegram.sendMessage(chatID, response)

MessageLoop(telegram, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)