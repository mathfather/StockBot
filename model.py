import os
import re
from rasa_nlu import config
from rasa_nlu.training_data import load_data
from rasa_nlu.model import Interpreter, Trainer
from settings import models_path, reg_rule, config_file, data, saving_path

class nlu_model(object):
    def __init__(self, models_path=models_path, reg_rule=reg_rule):
        if os.path.exists(models_path):
            models_name = os.listdir(models_path)
            if models_name:
                model_name = models_name[0]
                if re.match(reg_rule, model_name):
                    model_path = models_path + '/' + model_name
                    self.interpreter = Interpreter.load(model_path)
                else:
                    self.train()
            else:
                self.train()
        else:
            self.train()

    def train(self, config_file=config_file, data=data, saving_path=saving_path):
        trainer = Trainer(config.load(config_file))
        training_data = load_data(data)
        self.interpreter = trainer.train(training_data)
        trainer.persist(saving_path)

# test
if __name__ == '__main__':
    a = nlu_model()
    result = a.interpreter.parse(u"bloomberg")
    print(result)