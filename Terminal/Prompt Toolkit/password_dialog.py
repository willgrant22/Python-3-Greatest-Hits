#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================
from prompt_toolkit.shortcuts import input_dialog


def main():
    result = input_dialog(
        title="Password dialog example",
        text="Please type your password:",
        password=True,
    ).run()

    print("Result = {}".format(result))


if __name__ == "__main__":
    main()
