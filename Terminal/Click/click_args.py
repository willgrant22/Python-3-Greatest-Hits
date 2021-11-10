#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import click

@click.command()
@click.argument('file_name', type=click.File('r'))
@click.argument('lines', default=-1, type=int)
def head(file_name, lines):

    counter = 0

    for line in file_name:

        print(line.strip())
        counter += 1

        if counter == lines: 
            break


if __name__ == '__main__':
    head()

#usage: py test.py forms.log 2