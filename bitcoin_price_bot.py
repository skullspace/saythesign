#!/usr/bin/env python3

import urllib.request
import json
from datetime import date

def json_from_url(request):
    response = urllib.request.urlopen(request)

    str_response = response.readall().decode('utf-8')
    return json.loads(str_response)


historical_closes = sorted( json_from_url(
    'http://api.coindesk.com/v1/bpi/historical/close.json')[
    "bpi"].items() )
yesterdays_close_usd = historical_closes[-1][1]
    

BPI = json_from_url('http://api.coindesk.com/v1/bpi/currentprice/CAD')['bpi']

current_usd, current_cad = BPI['USD']['rate_float'], BPI['CAD']['rate_float']

up_down = "{green}^" if current_usd > yesterdays_close_usd else "{red}v"
abs_percent = abs(
    (current_usd-yesterdays_close_usd)*100 / yesterdays_close_usd )

print( "coindesk.com/price "  
       "%.2f USD/BTC, %.2f CAD, %s %.2f%% {yellow} "
       "from yesterday (%.2f)" %
        (current_usd, current_cad, up_down, abs_percent, yesterdays_close_usd)
       )

current_balance_of_endowment = 0.55847658

# replace constant with lookup
bonehead_endowment_value = current_balance_of_endowment * current_cad

#https://blockchain.info/tx/0e8cf9152a8b44bcb526bfe65493c70ccc521afeb78d8569d159f384fa9ab1d4
# trust fund seeded by Ian, principal in bitcoin terms also grew by mining,
# additional donations, and sales of miners, but only Ian's seed is documented
# here
bonehead_endowment_seed_btc = 0.15561679
bonehead_endowment_seed_value = 50
bonehead_endowment_seed_day = date(2013, 11, 17)
days_since_seed = (date.today() - bonehead_endowment_seed_day).days
years_since_seed = days_since_seed / 365.25
annual_growth = ( (bonehead_endowment_value/bonehead_endowment_seed_value) ** ( 1/(years_since_seed) ) -1 ) *100

growth_or_loss = "{green}growth" if annual_growth >= 0 else "{red}loss"

additional_btc_in_endowment_from_seed = \
    current_balance_of_endowment - bonehead_endowment_seed_btc

print( "{red}Bonehead {yellow}Bitcoin Endowment Trust is worth "
       "{green}$%.0f, %.1f%% annual %s {yellow}from {green}$%s seed (%.2f) "
       "{yellow}on %s and %.2f BTC added since" %
       (bonehead_endowment_value, annual_growth, growth_or_loss,
        bonehead_endowment_seed_value, bonehead_endowment_seed_btc,
        bonehead_endowment_seed_day,
        additional_btc_in_endowment_from_seed)
       )
    



