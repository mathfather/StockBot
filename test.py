from conversation import *
from model import *

if __name__ == '__main__':
    a = nlu_model()
    b = conversation()
    result = a.interpreter.parse(u"qqst")
    print(result)
    c = b.reply(result)
    d = b.round
    e = b.intent
    print(c)
    print(d)
    print(e)