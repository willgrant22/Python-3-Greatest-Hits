#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

from twilio.rest import Client 

account_sid = ''
auth_token = ''

client = Client(account_sid, auth_token) 

''' Change the value of 'from' with the number 
received from Twilio and the value of 'to' 
with the number in which you want to send message.'''
message = client.messages.create( 
							from_='', 
							body ='', 
							to =''
						) 

print(message.sid) 

