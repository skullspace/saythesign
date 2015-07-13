#!/usr/bin/env python

from sys import stdin
from os import getenv
from StringIO import StringIO

from xmpp_thesign import \
    create_connected_authed_client, send_line_iterable_w_send_delay

def main():
    
    if getenv('CONTENT_TYPE') == 'application/x-www-form-urlencoded':
        from cgi import FieldStorage

        form = FieldStorage()
        
        msg = form.getvalue('msg')
	if msg == None:
	    raise Exception("No message")
    else:
        msg =  ''.join(stdin)
    
    client = create_connected_authed_client()
    send_line_iterable_w_send_delay(client, StringIO(msg), 1)

    if getenv('CONTENT_TYPE') == 'application/x-www-form-urlencoded':
        print "Status: 303"
        print "Location: /"
    else:
        print "Status: 204" 
    print ''
    

if __name__ == "__main__":
    main()
    
