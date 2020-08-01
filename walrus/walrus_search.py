
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import re

data = 'There is a book on the table.'

pattern = re.compile(r'book')

if match := pattern.search(data):
    print(f'The word {pattern.pattern} is at {match.start(), match.end()}') 
else:
    print(f'No {pattern.pattern} found')