#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author: Will Grant
# =============================================================================
from prompt_toolkit.shortcuts import button_dialog


def main():
    result = button_dialog(
        title="Button dialog example",
        text="Are you sure?",
        buttons=[("Yes", True), ("No", False), ("Maybe...", None),],
    ).run()

    print("Result = {}".format(result))


if __name__ == "__main__":
    main()
