#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Will Grant
# Description : Simple prompt_toolkit button_dialog
# =============================================================================
from prompt_toolkit.shortcuts import button_dialog

def main():
    result = button_dialog(
        title="Button dialog example",
        text="Are you sure?",
        buttons=[("Yes", True), ("No", False), ("Maybe...", None),],
    ).run()

    print(f'Result = {result}')

main()
