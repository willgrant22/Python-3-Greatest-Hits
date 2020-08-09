#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import uuid, boto3
from boto3 import client

s3_resource = boto3.resource('s3')
x = []
for bucket in s3_resource.buckets.all():
#    print(bucket.name)
    for obj in bucket.objects.all():
        x.append(bucket.name)
#        print(obj)
#        print(obj.key)

y = []
for bucket_dict in s3_resource.meta.client.list_buckets().get('Buckets'):
    y.append(bucket_dict)
#    print(bucket_dict['Name'])

first_bucket = x
print(x[0])

conn = client('s3')  # again assumes boto.cfg setup, assume AWS S3
for key in conn.list_objects(Bucket=f'{x[0]}')['Contents']:
    print(key['Key'])
