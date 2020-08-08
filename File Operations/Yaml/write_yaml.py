#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import yaml

users = [{'name': 'John Doe', 'occupation': 'gardener'},
         {'name': 'Jack Black', 'occupation': 'teacher'}]

with open('users.yaml', 'w') as f:
    
    data = yaml.dump(users, f)