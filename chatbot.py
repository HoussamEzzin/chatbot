from chatterbot import ChatBot

bot = ChatBot(
    'Sakuuragi',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter']
)

from chatterbot.trainers import ChatterBotCorpusTrainer

trainer = ChatterBotCorpusTrainer(bot)

trainer.train('chatterbot.corpus.english')

close = ['bye','Bye','gg','goodbye','see u']

name = input('Enter your name')
print("Hi "+name+", how can I help you?")
while True:
    request = input(name+':')
    if request in close:
        print('Sakuuragi : Bye')
        break
    else:
        response = bot.get_response(request)
        print('Sakuuragi : ',response)