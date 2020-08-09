#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import uuid, boto3

s3_resource = boto3.resource('s3')

for bucket in s3_resource.buckets.all():
    print(bucket.name)