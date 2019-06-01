import json
from settings import testing_data
from model import *

def test(testset=testing_data):
    model = nlu_model()
    with open(testset, 'r') as f:
        test_data = json.load(f)
        intances = test_data['rasa_nlu_data']['common_examples']
        total = float(len(intances))
        accuracy = 0.0
        for instance in intances:
            intent = instance['intent']
            entity = instance['entities'][0]['value']
            text = instance['text']
            model_result = model.interpreter.parse(text)
            model_intent = model_result['intent']['name']
            model_entity = model_result['entities'][0]['value']
            model_entity = model_entity.upper()
            if model_entity == entity and model_intent == intent:
                accuracy += 1.0
                print('Accurate')
            else:
                print('Inaccurate')
        print(accuracy/total)
        return str(accuracy/total)