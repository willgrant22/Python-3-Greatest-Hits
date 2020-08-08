#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author: Will Grant
# =============================================================================

import json

person = {
     'first_name': "John",
     "isAlive": True,
     "age": 27,
     "address": {
         "streetAddress": "21 2nd Street",
         "city": "New York",
         "state": "NY",
         "postalCode": "10021-3100"
     },
     "hasMortgage": None
 }

 
with open('person.json', 'w') as f:  # writing JSON object
 json.dump(person, f)



print(open('person.json', 'r').read())   # reading JSON object as string


print(type(open('person.json', 'r').read())) 