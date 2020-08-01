
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

users = [ 
    {'name': 'John Doe', 'occupation': 'gardener'},
    {'name': None, 'occupation': 'teacher'}, 
    {'name': 'Robert Brown', 'occupation': 'driver'}, 
    {'name': None, 'occupation': 'driver'}, 
    {'name': 'Marta Newt', 'occupation': 'journalist'} 
] 
  
for user in users:  
    if ((name := user.get('name')) is not None): 
        print(f'{name} is a {user.get("occupation")}') 