import get_api

class conversation(object):
    def __init__(self):
        self.intent = ''
        self.round = 0

    def clear(self):
        self.intent = ''
        self.round = 0

    def slot_filling(self, entity):
        if self.intent == '':
            return self.intentless() # clear
            # lack of context intent and only input an entity this round
        else:
            intent = self.intent
            if self.get_info(intent, entity):
                # correctly search
                info = self.get_info(intent, entity)[0]
                prompt = self.get_info(intent, entity)[1]
                answer = 'The ' + prompt + ' of ' + entity + ' is ' + info + '.'
                self.clear() # end
                return answer
            else:
                return self.type_error()
                # check round number

    def reply(self, result):
        confidence = result['intent']['confidence']
        if confidence < 0.5:
            return self.intentless() # classifer cannot make a decision
        elif result['intent']['name'] == 'None':
            if result['entities']:
                entity = result['entities'][0]['value']
                entity = entity.upper()
                self.round += 1
                return self.slot_filling(entity)
            else:
                return self.allless()
        else: # have intent and it is not 'None'
            intent = result['intent']['name']
            if result['entities']:
                entity = result['entities'][0]['value']
                entity = entity.upper()
                self.intent = intent
                if self.get_info(intent, entity):
                    # correct symbol
                    info = self.get_info(intent, entity)[0]
                    prompt = self.get_info(intent, entity)[1]
                    answer = 'The ' + prompt + ' of ' + entity + ' is ' + info + '.'
                    self.clear()
                    return answer
                else:
                    return self.type_error()
            else:
                return self.entityless(intent)
                # wait for the second round conversation to get an entity

    def intentless(self):
        self.clear()
        return 'No specific intent shown. Please be more specific about what you want to do.'

    def entityless(self, intent):
        self.intent = intent
        if self.round < 3:
            self.round += 1
        else:
            self.clear()
        return 'No specific entity shown. Whose ' + self.intent + ' you want to find?'

    def allless(self):
        self.clear()
        return 'Please start over from the begining.'

    def get_info(self, intent, entity):
        if intent == 'FindName':
            return self.get_name(entity)
        elif intent == 'FindListDate':
            return self.get_listdate(entity)
        elif intent == 'FindId':
            return self.get_id(entity)
        elif intent == 'Tradeable':
            return self.get_tradeable(entity)
        elif intent == 'State':
            return self.get_state(entity)
        elif intent == 'FindBloomberg':
            return self.get_bloomberg(entity)

    def get_name(self, entity):
        result = get_api.get_instrument_info('symbol', symbol=entity)
        if result != '':
            name = result.name
        else:
            return []
        return [name, 'full name']

    def get_listdate(self, entity):
        result = get_api.get_instrument_info('symbol', symbol=entity)
        if result != '':
            listdate = result.list_date
        else:
            return []
        return [listdate, 'date this security was first traded publically on the exchange']

    def get_id(self, entity):
        result = get_api.get_instrument_info('symbol', symbol=entity)
        if result != '':
            id = result.id
        else:
            return []
        return [id, 'ID']

    def get_tradeable(self, entity):
        result = get_api.get_instrument_info('symbol', symbol=entity)
        if result != '':
            tradeable = result.tradeable
        else:
            return []
        return [tradeable, 'tradeable state']

    def get_state(self, entity):
        result = get_api.get_instrument_info('symbol', symbol=entity)
        if result != '':
            state = result.state
        else:
            return []
        return [state, 'active state']

    def get_bloomberg(self, entity):
        result = get_api.get_instrument_info('symbol', symbol=entity)
        if result != '':
            bloomberg = result.bloomberg_unique
        else:
            return []
        return [bloomberg, 'bloomberg unique id']

    def type_error(self):
        if self.round < 3:
            self.round += 1
            return 'There is something wrong with your entity typing. Please type again.'
        else:
            self.clear()
            return 'There is something wrong with your entity typing. History clear. Please start over from the begining.'
       
# test
if __name__ == '__main__':
    name = get_name('MSFT')
    print(name[0])
    print(name[1])