#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import uuid, boto3

s3_resource = boto3.resource('s3')

def create_bucket_name(bucket_prefix):
    # The generated bucket name must be between 3 and 63 chars long
    return ''.join([bucket_prefix, str(uuid.uuid4())])
#print(create_bucket_name("us-east-2"))
def create_temp_file(size, file_name, file_content):
    random_file_name = ''.join([str(uuid.uuid4().hex[:6]), file_name])
    with open(random_file_name, 'w') as f:
        f.write(str(file_content) * size)
    return random_file_name

def create_bucket(bucket_prefix, s3_connection):
    session = boto3.session.Session()
    current_region = session.region_name
    bucket_name = create_bucket_name(bucket_prefix)
    bucket_response = s3_connection.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={
        'LocationConstraint': current_region})
    print(bucket_name, current_region)
    return bucket_name, bucket_response

first_bucket_name, first_response = create_bucket(
    bucket_prefix='firstpythonbucket',
    s3_connection=s3_resource.meta.client)

second_bucket_name, second_response = create_bucket(
    bucket_prefix='secondpythonbucket', s3_connection=s3_resource)
print('\n')
print(first_response)
print('\n')
print(second_response)
print('\n')

first_file_name = create_temp_file(300, 'firstfile.txt', 'f')

first_bucket = s3_resource.Bucket(name=first_bucket_name)
print(first_bucket)
print('\n')

first_object = s3_resource.Object(
    bucket_name=first_bucket_name, key=first_file_name)

print(first_object)
print('\n')
first_bucket_again = first_object.Bucket()
print(first_bucket_again)
print('\n')
first_object_again = first_bucket.Object(first_file_name)
print(first_object_again)
print('\n')