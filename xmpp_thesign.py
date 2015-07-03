#!/usr/bin/python

import xmpp
import sys
import time

SERVER = 'skullspace.ca'
SIGN_POST_USER = 'thesign@skullspace.ca'

def create_connected_authed_client():
    with file('userpass') as f:
        username = f.readline().strip()
        passwd = f.readline().strip()

    client = xmpp.Client(SERVER)
    client.connect()
    client.auth(username, passwd)
    return client

def send_line_iterable_w_send_delay(client, line_iterable, delay=1):
    for line in line_iterable:
        client.send(xmpp.Message(
                SIGN_POST_USER,
                line.strip() + "\n" ))
        time.sleep(delay)

if __name__ == "__main__":
    client = create_connected_authed_client()

    send_line_iterable_w_send_delay(client, sys.stdin, 1)

    for file_name in sys.argv[1:]:
        with open(file_name) as f:
            send_line_iterable_w_send_delay(client, f, 1)


