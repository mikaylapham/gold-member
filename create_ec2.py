#!/usr/bin/env python3.7

import boto3

ec2 = boto3.resource('ec2')

instance = (ec2.create_instances(
    ImageId='ami-069aabeee6f53e7bf',
    InstanceType='t2.micro',
    MaxCount=3,
    MinCount=3,
)

print(instance)