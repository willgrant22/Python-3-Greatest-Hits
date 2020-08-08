#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author: Will Grant
# =============================================================================
from prompt_toolkit.shortcuts import message_dialog


def main():
    message_dialog(
        title="Example dialog window",
        text="Do you want to continue?\nPress ENTER to quit.",
    ).run()


if __name__ == "__main__":
    main()
