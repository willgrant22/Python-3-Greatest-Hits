#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import boto3

ec2 = boto3.resource('ec2')

for instance in ec2.instances.all():
 print(instance.id, instance.state)