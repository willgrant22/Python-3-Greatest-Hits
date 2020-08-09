#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import boto3

ec2 = boto3.resource('ec2')
instance = ec2.create_instances(

 ImageId='ami-02b0c55eeae6d5096',
 MinCount=1,
 MaxCount=1,
 InstanceType='t2.micro'

 )

print(instance[0].id)