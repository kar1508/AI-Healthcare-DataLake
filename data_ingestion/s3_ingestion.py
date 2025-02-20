import boto3
import json
import time

# AWS S3 Bucket Name
BUCKET_NAME = 'healthcare-data-lake'
FOLDER_NAME = 'raw-data/'
s3_client = boto3.client('s3', region_name='us-east-1')

def upload_to_s3(data):
    timestamp = int(time.time())
    file_name = f"{FOLDER_NAME}patient_data_{timestamp}.json"
    s3_client.put_object(
        Bucket=BUCKET_NAME,
        Key=file_name,
        Body=json.dumps(data)
    )
    print(f"Uploaded to S3: {file_name}")

# Example data ingestion
if __name__ == "__main__":
    sample_data = {
        'patient_id': 1234,
        'heart_rate': 85,
        'blood_pressure': '120/80',
        'oxygen_level': 98,
        'temperature': 98.6,
        'timestamp': time.time()
    }
    upload_to_s3(sample_data)
