#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import re

email_regex = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

example_text = """
Subject: This is a text email!
From: John Doe <john@doe.com>
Some text here!
===============================
Subject: This is another email!
From: Abdou Rockikz <example@domain.com>
Some other text!
"""

print(re.sub(email_regex, "[email protected]", example_text))