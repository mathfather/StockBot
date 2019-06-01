from wxpy import *
from model import nlu_model
from conversation import *

bot = Bot()
model = nlu_model()
conversation = conversation()

@bot.register(Friend, TEXT)
def auto_reply(msg):
    # name = msg.sender.name
    text = msg.text
    result = model.interpreter.parse(text)
    print(result)
    final_reply = conversation.reply(result)
    print(conversation.intent)
    print(conversation.round)
    # print(final_reply)
    return final_reply

# embed()
bot.join()