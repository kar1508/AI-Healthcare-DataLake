# **AI Healthcare Data Lake**

## **Project Overview**
This project implements a scalable **data lake** architecture on AWS for real-time **streaming analytics** in healthcare. It enables the ingestion, transformation, and analysis of structured and semi-structured data for fraud detection and anomaly detection in patient health records.

## **Architecture & Services Used**
- **AWS Kinesis** – Streaming data ingestion
- **AWS S3** – Data lake storage
- **AWS Glue** – ETL processing
- **Apache Airflow** – Workflow orchestration
- **AWS Redshift** – Data warehouse for analytics
- **AWS SageMaker** – Machine learning for anomaly detection
- **AWS Lambda** – Real-time alerts
- **AWS QuickSight** – Data visualization
- **AWS Lake Formation** – Data governance and security

## **Project Structure**
```
AI-Healthcare-DataLake/
│── data_ingestion/
│   ├── kinesis_stream.py
│   ├── s3_ingestion.py
│── etl_processing/
│   ├── glue_job.py
│   ├── airflow_dag.py
│── anomaly_detection/
│   ├── sagemaker_model.py
│   ├── redshift_fraud_detection.sql
│── alerts/
│   ├── lambda_alert.py
│── visualization/
│   ├── quicksight_dashboard.json
│── infrastructure/
│   ├── iam_roles_setup.sh
│   ├── lake_formation_policies.json
│── README.md
```

## **Setup & Deployment**
### **1. Clone Repository**
```bash
git clone https://github.com/kar1508/AI-Healthcare-DataLake.git
cd AI-Healthcare-DataLake
```

### **2. Configure AWS Credentials**
Ensure your AWS CLI is configured properly:
```bash
aws configure
```

### **3. Deploy Infrastructure**
Set up IAM roles and policies:
```bash
bash infrastructure/iam_roles_setup.sh
```

### **4. Run Data Ingestion**
Start streaming data into Kinesis and store it in S3:
```bash
python data_ingestion/kinesis_stream.py
python data_ingestion/s3_ingestion.py
```

### **5. Execute ETL Processing**
Run AWS Glue job for transformation:
```bash
python etl_processing/glue_job.py
```

Execute the Apache Airflow DAG:
```bash
python etl_processing/airflow_dag.py
```

### **6. Train Anomaly Detection Model**
Deploy an ML model in SageMaker:
```bash
python anomaly_detection/sagemaker_model.py
```

### **7. Set Up Alerts & Monitoring**
Deploy Lambda function for fraud alerts:
```bash
aws lambda update-function-code --function-name HealthcareAlerts --zip-file fileb://alerts/lambda_alert.py.zip
```

### **8. Visualize Insights**
Configure QuickSight dashboard using:
```bash
aws quicksight create-dashboard --cli-input-json file://visualization/quicksight_dashboard.json
```

## **Contributors**
- karthikeya R – Developer & Architect



