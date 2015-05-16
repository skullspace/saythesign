#!/usr/bin/python

import xmpp

def simple_xmpp(server, username, passwd, to, msg):
    client = xmpp.Client(server)
    client.connect()
    client.auth(username, passwd)
    client.send(xmpp.Message(to, msg))

if __name__ == "__main__":
    with file('userpass') as f:
        username = f.readline().strip()
        passwd = f.readline().strip()
    simple_xmpp('skullspace.ca', username, passwd,
                'thesign@skullspace.ca', raw_input() )
