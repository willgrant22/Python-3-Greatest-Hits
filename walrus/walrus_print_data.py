
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

sample_data = [
    {"userId": 1, "id": 1, "title": "first", "completed": False},
    {"userId": 1, "id": 2, "title": "second", "completed": False},
    {"userId": 1, "id": 3, "title": "third", "completed": False},
    {"userId": 1, "id": 4, "title": "fourth", "completed": True},
    {"userId": 1, "id": 4, "title": None, "completed": True},
]

print("With Python 3.8 Walrus Operator:") 
for entry in sample_data: 
    if title := entry.get("title"):
        print(f'Found title: "{title}"')

print("Without Walrus operator:")
for entry in sample_data:
    title = entry.get("title")
    if title:
        print(f'Found title: "{title}"')