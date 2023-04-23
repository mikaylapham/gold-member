import boto3

ec2 = boto3.resource('ec2')
ec2.Instance('i-098159fa133fd14cb').stop()
ec2.Instance('i-0ea8ed5dbf4228953').stop()
ec2.Instance('i-0b027f8ddfa10a45f').stop()