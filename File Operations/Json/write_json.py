#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author: Will Grant
# =============================================================================
import json

dictionary = {
	"name" : "will",
	"rollno" : 56,
	"cgpa" : 8.6,
	"phonenumber" : 5131234567
}

with open("write.json", "w") as outfile:
	json.dump(dictionary, outfile)