#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import wikipedia

result = wikipedia.page('Space.Cloud')
print(result.summary)

for link in result.links:
    print(link)