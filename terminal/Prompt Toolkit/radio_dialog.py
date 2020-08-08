#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.shortcuts import radiolist_dialog


def main():
    result = radiolist_dialog(
        values=[
            ("red", "Red"),
            ("green", "Green"),
            ("blue", "Blue"),
            ("orange", "Orange"),
            ("test", "Test"),
        ],
        title="Radiolist dialog example",
        text="Please select a color:",
    ).run()

    print(f"Result = {result}")

    # With HTML.
    result = radiolist_dialog(
        values=[
            ("red", HTML('<style bg="red" fg="white">Red</style>')),
            ("green", HTML('<style bg="green" fg="white">Green</style>')),
            ("blue", HTML('<style bg="blue" fg="white">Blue</style>')),
            ("orange", HTML('<style bg="orange" fg="white">Orange</style>')),
        ],
        title=HTML("Radiolist dialog example <reverse>with colors</reverse>"),
        text="Please select a color:",
    ).run()

    print(f"Result = {result}")


main()
