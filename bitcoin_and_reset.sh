#!/bin/sh

cd ~/saythesign/
./bitcoin_price_bot.py | ./xmpp_thesign.py
./xmpp_thesign.py < jayswelcome.txt