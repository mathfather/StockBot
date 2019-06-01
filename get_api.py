import requests
import json


class Stock:  # 结构体，存放一只股票的所有信息
    pass


class Market:  # 结构体，存放一个股市的所有信息
    pass

# 在知道symbols的情况下获取一只股票的基本信息
# 返回一个Stock的list，每个Stock中包含一只股票的基本信息


def get_fundamentals_info(symbols):
    headers = {'Accept': 'application/json'}
    url = "https://api.robinhood.com/fundamentals/?symbols="
    for i in symbols:
        url = url + i + ","
    url = url[:-1]
    # print(url)
    r = requests.get(url=url, headers=headers, timeout=3)
    # print("status code :",r.status_code)
    response_dict = r.json()
    results = response_dict["results"]
    stocks = []
    for dic in results:
        stock = Stock()
        stock.open = dic['open']
        stock.high = dic['high']
        stock.low = dic['low']
        stock.volume = dic['volume']
        stock.average_volume_2_weeks = dic['average_volume_2_weeks']
        stock.average_volume = dic['average_volume']
        stock.high_52_weeks = dic['high_52_weeks']
        stock.dividend_yield = dic['dividend_yield']
        stock.low_52_weeks = dic['low_52_weeks']
        stock.pe_ratio = dic['pe_ratio']
        stock.shares_outstanding = dic['shares_outstanding']
        stock.description = dic['description']
        stock.instrument = dic['instrument']
        stock.ceo = dic['ceo']
        stock.headquarters_city = dic['headquarters_city']
        stock.headquarters_state = dic['headquarters_state']
        stock.sector = dic['sector']
        stock.num_employees = dic['num_employees']
        stock.year_founded = dic['year_founded']
        stocks.append(stock)

    # print(response_dict)
    return stocks

# 获取一只股票的高级信息，有两种查询方式，在typ参数中指出
# typ==‘symbol’是在已知symbol的情况下查询，typ==‘url’是在已知url的情况下查询
# 返回值是一个Stock结构体，包含这只股票的全部高级信息


def get_instrument_info(typ, symbol='', url=''):
    headers = {'Accept': 'application/json'}
    url1 = ""

    if typ == "symbol":
        url1 = "https://api.robinhood.com/instruments/?symbol=" + symbol
    elif typ == "url":
        url1 = url

    r = requests.get(url=url1, headers=headers, timeout=30)

    # print("status code :",r.status_code)

    response_dict = r.json()

    result_dict = {}

    if typ == "symbol":
        if response_dict['results'] != []:
            result_dict = response_dict["results"][0]
        else:
            return ''
    elif typ == "url":
        result_dict = response_dict

    # print(result_dict)

    stock = Stock()

    stock.margin_initial_ratio = result_dict['margin_initial_ratio']
    stock.rhs_tradability = result_dict['rhs_tradability']
    stock.id = result_dict['id']
    stock.market = result_dict['market']
    stock.simple_name = result_dict['simple_name']
    stock.min_tick_size = result_dict['min_tick_size']
    stock.maintenance_ratio = result_dict['maintenance_ratio']
    stock.tradability = result_dict['tradability']
    stock.state = result_dict['state']
    stock.type = result_dict['type']
    stock.tradeable = result_dict['tradeable']
    stock.fundamentals = result_dict['fundamentals']
    stock.quote = result_dict['quote']
    stock.symbol = result_dict['symbol']
    stock.day_trade_ratio = result_dict['day_trade_ratio']
    stock.name = result_dict['name']
    stock.tradable_chain_id = result_dict['tradable_chain_id']
    stock.splits = result_dict['splits']
    stock.url = result_dict['url']
    stock.country = result_dict['country']
    stock.bloomberg_unique = result_dict['bloomberg_unique']
    stock.list_date = result_dict['list_date']

    return stock


# 在知道symbols的情况下获取一只股票的报价信息
# 返回一个Stock的list，每个Stock中包含一只股票的报价信息
def get_quote_info(symbols):
    headers = {'Accept': 'application/json'}
    url = "https://api.robinhood.com/quotes/?symbols="

    for i in symbols:
        url = url + i + ","
    url = url[:-1]

    # print(url)

    r = requests.get(url=url, headers=headers, timeout=30)

    # print("status code :",r.status_code)

    response_dict = r.json()

    results = response_dict["results"]

    stocks = []

    for dic in results:
        stock = Stock()
        stock.ask_price = dic['ask_price']
        stock.ask_size = dic['ask_size']
        stock.bid_price = dic['bid_price']
        stock.bid_size = dic['bid_size']
        stock.last_trade_price = dic['last_trade_price']
        stock.last_extended_hours_trade_price = dic['last_extended_hours_trade_price']
        stock.previous_close = dic['previous_close']
        stock.adjusted_previous_close = dic['adjusted_previous_close']
        stock.previous_close_date = dic['previous_close_date']
        stock.symbol = dic['symbol']
        stock.trading_halted = dic['trading_halted']
        stock.has_traded = dic['has_traded']
        stock.last_trade_price_source = dic['last_trade_price_source']
        stock.updated_at = dic['updated_at']
        stock.instrument = dic['instrument']
        stocks.append(stock)

    return stocks


# 获取一个股市的信息，可以查询基本信息和开市时间表，在typ参数中指出
# typ==‘mic’是在已知mic的情况下查询股市基本信息，typ==‘hours’是在已知mic的情况下查询一个股市的时间表，需要在date参数中给出具体日期
# 返回值是一个Market结构体，包含这个股市的相关查询信息
def get_market_info(typ, mic='', date=''):
    headers = {'Accept': 'application/json'}
    url = "https://api.robinhood.com/markets/"

    if typ == "mic":
        url = url + mic + "/"
    elif typ == "hours":
        url = url + mic + "/hours/" + date

    r = requests.get(url=url, headers=headers, timeout=30)

    # print(url)

    response_dict = r.json()

    result_dict = {}

    # print(response_dict)

    market = Market()
    if typ == "mic":
        result_dict = response_dict
        market.website = result_dict['website']
        market.city = result_dict['city']
        market.name = result_dict['name']
        market.url = result_dict['url']
        market.country = result_dict['country']
        market.todays_hours = result_dict['todays_hours']
        market.operating_mic = result_dict['operating_mic']
        market.acronym = result_dict['acronym']
        market.timezone = result_dict['timezone']
        market.mic = result_dict['mic']
    elif typ == "hours":
        result_dict = response_dict
        market.closes_at = result_dict['closes_at']
        market.extended_opens_at = result_dict['extended_opens_at']
        market.next_open_hours = result_dict['next_open_hours']
        market.previous_open_hours = result_dict['previous_open_hours']
        market.is_open = result_dict['is_open']
        market.extended_closes_at = result_dict['extended_closes_at']
        market.date = result_dict['date']
        market.opens_at = result_dict['opens_at']

    return market