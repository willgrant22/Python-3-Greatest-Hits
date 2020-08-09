#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import uuid, boto3
from boto3 import client

s3_resource = boto3.resource('s3')

def delete_all_objects(bucket_name):
    res = []
    bucket=s3_resource.Bucket(bucket_name)
    for obj_version in bucket.object_versions.all():
        res.append({'Key': obj_version.object_key,
                    'VersionId': obj_version.id})
    print(res)
    bucket.delete_objects(Delete={'Objects': res})

x = []
for bucket in s3_resource.buckets.all():
    print(bucket.name)
    x.append(bucket.name)
    for obj in bucket.objects.all():
        print(obj)
        print(obj.key)
print(x)

y = []
for bucket_dict in s3_resource.meta.client.list_buckets().get('Buckets'):
    y.append(bucket_dict)
    #print(bucket_dict['Name'])

first_bucket_name = x[0]
second_bucket_name = x[1]

conn = client('s3')
for key in conn.list_objects(Bucket=f'{first_bucket_name}')['Contents']:
    print(key['Key'])

#delete objects from bucket
delete_all_objects(first_bucket_name)

#del bucket
s3_resource.Bucket(first_bucket_name).delete()

#del bucket with client
s3_resource.meta.client.delete_bucket(Bucket=second_bucket_name)
