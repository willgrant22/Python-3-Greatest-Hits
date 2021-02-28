#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import sys
import boto3

ec2 = boto3.resource('ec2')

for instance_id in sys.argv[1:]:
 instance = ec2.Instance(instance_id)
 response = instance.terminate()

 print(response)