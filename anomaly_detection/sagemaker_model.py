import boto3
import sagemaker
from sagemaker import get_execution_role
from sagemaker.xgboost.estimator import XGBoost

# Set up AWS SageMaker session
role = get_execution_role()
sagemaker_session = sagemaker.Session()
bucket = 'healthcare-data-lake'

# Data paths
train_path = f's3://{bucket}/training-data/train.csv'
test_path = f's3://{bucket}/training-data/test.csv'

# XGBoost Model Configuration
xgb_model = XGBoost(
    entry_point='train.py',
    framework_version='1.2-1',
    hyperparameters={
        'num_round': 100,
        'max_depth': 5,
        'eta': 0.2,
        'objective': 'binary:logistic'
    },
    role=role,
    instance_count=1,
    instance_type='ml.m5.large',
    output_path=f's3://{bucket}/model-output/',
    sagemaker_session=sagemaker_session
)

# Train the model
xgb_model.fit({'train': train_path, 'validation': test_path})

print("SageMaker model training completed.")
