from wxpy import *
from model import nlu_model
from conversation import *

bot = Bot()
model = nlu_model()

@bot.register(Friend, TEXT)
def auto_reply(msg):
    name = msg.sender.name
    text = msg.text
    result = model.interpreter.parse(text)
    final_reply = reply(result, name)
    return final_reply
#embed()
bot.join()