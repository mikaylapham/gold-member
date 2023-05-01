# Import Boto3 library
import boto3

# Create an SQS client
sqs = boto3.client('sqs')

# Create a new SQS queue
response = sqs.create_queue(QueueName='Wk15PrjOrderNoti')

# Retrieve the SQS queue URL
queue_url = response['QueueUrl']
print(f"Queue URL: {queue_url}")