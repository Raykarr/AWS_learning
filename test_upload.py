import boto3
from botocore.exceptions import ClientError

# Set your bucket name and file details
bucket_name = 'clarity-mirror-kaustubh' 
file_name = 'test_upload.txt'
file_content = 'This is a test upload from my GenAI project'

# Initialize the S3 client
try:
    print("Initializing S3 client...")
    s3 = boto3.client('s3')
    print("S3 client initialized.")

    print(f"Uploading file '{file_name}' to bucket '{bucket_name}'...")
    response = s3.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=file_content
    )

    # Confirm response
    print("Upload successful.")
    print("Response metadata:")
    print(response)

except ClientError as e:
    print("Upload failed:")
    print(e)
except Exception as ex:
    print("Unexpected error occurred:")
    print(ex)
