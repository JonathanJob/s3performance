import boto3

from dotenv import load_dotenv
load_dotenv()

s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)
