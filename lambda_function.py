import boto3
import pandas as pd
import io

def lambda_handler(event, context):
    # Retrieve the file from S3
    s3_bucket = 'jpmdata-bucket'
    input_file_key = 'input/JPMorgan Chase.csv'
    output_file_key = 'processed/processed_file.csv'
    
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=s3_bucket, Key=input_file_key)
    content = response['Body'].read().decode('utf-8')
    
    # Process the file using pandas
    df = pd.read_csv(io.StringIO(content))
    
    # Calculate the new columns
    df['Daily Range'] = df['Close'] - df['Open']
    df['Daily Span'] = df['High'] - df['Low']
    
    # Save the updated file to another folder within S3
    processed_content = df.to_csv(index=False)
    s3.put_object(Body=processed_content, Bucket=s3_bucket, Key=output_file_key)
    
    return {
        'statusCode': 200,
        'body': 'File processed and saved successfully.'
    }
