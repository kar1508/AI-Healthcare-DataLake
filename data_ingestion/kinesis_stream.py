import boto3
import json
import random
import time

# AWS Kinesis Stream Name
STREAM_NAME = 'HealthcareDataStream'
kinesis_client = boto3.client('kinesis', region_name='us-east-1')

# Simulating real-time healthcare data
def generate_patient_data():
    return {
        'patient_id': random.randint(1000, 9999),
        'heart_rate': random.randint(60, 120),
        'blood_pressure': f"{random.randint(90, 140)}/{random.randint(60, 90)}",
        'oxygen_level': random.randint(85, 100),
        'temperature': round(random.uniform(97.0, 99.5), 1),
        'timestamp': time.time()
    }

while True:
    data = generate_patient_data()
    kinesis_client.put_record(
        StreamName=STREAM_NAME,
        Data=json.dumps(data),
        PartitionKey=str(data['patient_id'])
    )
    print(f"Sent: {data}")
    time.sleep(2)  # Simulate a 2-second interval between events
