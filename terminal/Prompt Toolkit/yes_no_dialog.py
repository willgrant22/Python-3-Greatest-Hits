#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author: Will Grant
# =============================================================================
from prompt_toolkit.shortcuts import yes_no_dialog


def main():
    result = yes_no_dialog(
        title="Yes/No dialog example", text="Do you want to confirm?"
    ).run()

    print("Result = {}".format(result))


if __name__ == "__main__":
    main()
