import json
import boto3

sns_client = boto3.client('sns')
SNS_TOPIC_ARN = 'arn:aws:sns:us-east-1:123456789012:HealthcareAlerts'

def lambda_handler(event, context):
    for record in event['Records']:
        payload = json.loads(record['body'])
        patient_id = payload.get('patient_id')
        anomaly_detected = payload.get('anomaly_detected', False)
        
        if anomaly_detected:
            message = f"Alert! Anomaly detected for patient {patient_id}: {payload}"
            sns_client.publish(
                TopicArn=SNS_TOPIC_ARN,
                Message=message,
                Subject="Healthcare Anomaly Alert"
            )
            print(f"Alert sent for patient {patient_id}")
        
    return {
        'statusCode': 200,
        'body': json.dumps('Alerts processed successfully!')
    }
