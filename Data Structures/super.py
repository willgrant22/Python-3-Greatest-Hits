#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

class Parent:
  def __init__(self, txt):
    self.message = txt
    print('h')

  def printmessage(self):
    print(self.message)

class Child(Parent):
  def __init__(self, txt):
  	print('j')
  	super().__init__(txt)

x = Child("Hello, and welcome!")

x.printmessage()