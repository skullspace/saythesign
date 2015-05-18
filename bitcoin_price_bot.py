#!/usr/bin/env python3

import urllib.request
import json

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

# replace constant with lookup
bonehead_endowment_value = 0.55847658 * current_cad

print( "coindesk.com/price "  
       "%.2f USD/BTC, %.2f CAD, %s %.2f%% {yellow} "
       "from yesterday (%.2f)" %
        (current_usd, current_cad, up_down, abs_percent, yesterdays_close_usd)
       )

print( "{red}Bonehead {yellow}Bitcoin Endowment Trust is worth "
       "{green}$%.0f" %
        bonehead_endowment_value )
    



