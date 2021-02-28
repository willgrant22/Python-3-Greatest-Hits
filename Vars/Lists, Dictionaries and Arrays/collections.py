#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import collections
nums = [1, 2, 3]
# creating deque collection from the list
deque = collections.deque(nums)

print(deque)

# adding an element at the end
deque.append(4)

print(deque)

# adding element at the starting
deque.appendleft(0)

print(deque)

# removing the element at the end
deque.pop()

print(deque)

# removing element at the starting
deque.popleft()

print(deque[1])