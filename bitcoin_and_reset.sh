#!/bin/sh

cd ~/saythesign/
./bitcoin_price_bot.py | ./xmpp_thesign.py
sleep 15s
./xmpp_thesign.py < jayswelcome.txt