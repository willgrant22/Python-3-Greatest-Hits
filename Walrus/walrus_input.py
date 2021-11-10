
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

inputs = list()
while (current := input("Write something: ")) != "quit":
    inputs.append(current)

print(inputs)