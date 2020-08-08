#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import sys
import os

sheb = '#!/usr/bin/env python3'
newl = '\n'
spacef = '    '

file = open(f"{'main'}.py", "w")
file.write(f"{sheb}{newl}")
file.write(f'{newl}')
file.write(f'def main():{newl}')
file.write(f'{spacef}#code here{newl}')
file.write(f'{newl}')
file.write(f'main()')

file.close()



