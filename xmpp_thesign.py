#!/usr/bin/python

import xmpp
import sys
import time

SERVER = 'skullspace.ca'
SIGN_POST_USER = 'thesign@skullspace.ca'

if __name__ == "__main__":
    with file('userpass') as f:
        username = f.readline().strip()
        passwd = f.readline().strip()

    client = xmpp.Client(SERVER)
    client.connect()
    client.auth(username, passwd)

    for line in sys.stdin:
        client.send(xmpp.Message(
                SIGN_POST_USER,
                line.strip() + "\n" ))
        time.sleep(1)

    for file_name in sys.argv[1:]:
        with open(file_name) as f:
            for i, line in enumerate(f):
                client.send(xmpp.Message(
                        SIGN_POST_USER,
                        line.strip() + "\n" ) )
                time.sleep(1)

