#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import click


@click.command()
@click.option('--n', type=int, default=1)
def dots(n):
    click.echo('.' * n)


if __name__ == '__main__':
    dots()


# usage: py test.py --n 4 