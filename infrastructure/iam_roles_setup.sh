#!/bin/bash

AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
ROLE_NAME="HealthcareDataLakeRole"
POLICY_NAME="HealthcareDataLakePolicy"

# Create IAM Role
aws iam create-role \
    --role-name $ROLE_NAME \
    --assume-role-policy-document '{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {"Service": "glue.amazonaws.com"},
                "Action": "sts:AssumeRole"
            }
        ]
    }'

# Attach Inline Policy to Role
aws iam put-role-policy \
    --role-name $ROLE_NAME \
    --policy-name $POLICY_NAME \
    --policy-document '{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "s3:PutObject", "s3:GetObject", "s3:ListBucket"
                ],
                "Resource": [
                    "arn:aws:s3:::healthcare-data-lake",
                    "arn:aws:s3:::healthcare-data-lake/*"
                ]
            },
            {
                "Effect": "Allow",
                "Action": [
                    "glue:*"
                ],
                "Resource": "*"
            }
        ]
    }'

echo "IAM Role and Policy setup completed successfully."
