import boto3

ec2 = boto3.resource('ec2')
ec2.Instance('INSERT_INSTANCE_ID_HERE').stop()
ec2.Instance('INSERT_INSTANCE_ID_HERE').stop()
ec2.Instance('INSERT_INSTANCE_ID_HERE').stop()
