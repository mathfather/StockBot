import get_api

def reply(result, name):
    confidence = result['intent']['confidence']
    if confidence < 0.5:
        return intentless()
    else:
        intent = result['intent']['name']
        if result['entities']:
            entity = result['entities'][0]['value']
            entity = entity.upper()
            if get_info(intent, entity):
                info = get_info(intent, entity)[0]
                prompt = get_info(intent, entity)[1]
                answer = 'The ' + prompt + ' of ' + entity + ' is ' + info + '.'
                return answer
            else:
                return type_error()
        else:
            return entityless()

def intentless():
    return 'No specific intent shown.'

def entityless():
    return 'No specific entity shown.'

def get_info(intent, entity):
    if intent == 'FindName':
        return get_name(entity)
    elif intent == 'FindListDate':
        return get_listdate(entity)
    elif intent == 'FindId':
        return get_id(entity)
    elif intent == 'Tradeable':
        return get_tradeable(entity)
    elif intent == 'State':
        return get_state(entity)
    elif intent == 'FindBloomberg':
        return get_bloomberg(entity)

def get_name(entity):
    result = get_api.get_instrument_info('symbol', symbol=entity)
    if result != '':
        name = result.name
    else:
        return []
    return [name, 'full name']

def get_listdate(entity):
    result = get_api.get_instrument_info('symbol', symbol=entity)
    if result != '':
        listdate = result.list_date
    else:
        return []
    return [listdate, 'the date this security was first traded publically on the exchange']

def get_id(entity):
    result = get_api.get_instrument_info('symbol', symbol=entity)
    if result != '':
        id = result.id
    else:
        return []
    return [id, 'ID']

def get_tradeable(entity):
    result = get_api.get_instrument_info('symbol', symbol=entity)
    if result != '':
        tradeable = result.tradeable
    else:
        return []
    return [tradeable, 'tradeable state']

def get_state(entity):
    result = get_api.get_instrument_info('symbol', symbol=entity)
    if result != '':
        state = result.state
    else:
        return []
    return [state, 'active state']

def get_bloomberg(entity):
    result = get_api.get_instrument_info('symbol', symbol=entity)
    if result != '':
        bloomberg = result.bloomberg_unique
    else:
        return []
    return [bloomberg, 'bloomberg unique id']

def type_error():
    return 'There is something wrong with your entity typing.'
       
# test
if __name__ == '__main__':
    name = get_name('MSFT')
    print(name[0])
    print(name[1])