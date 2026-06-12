import os
import csv
import boto3

# 1. AWS picks up the GitHub secrets automatically from the environment
s3 = boto3.client(
    's3',
    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY')
)

# ⚠️ CHANGE THIS to your exact AWS S3 bucket name from Step 5
BUCKET_NAME = 'sports-analytics-data-lake-ritesh' 
FILE_NAME = 'match_data.csv'

# 2. Generate a fresh batch of sample cricket data
data = [
    [1, 'Shreyas Iyer', '2026-06-01', 'Mumbai Indians', 45, 0],
    [2, 'Rinku Singh', '2026-06-01', 'Mumbai Indians', 28, 0],
    [3, 'Hardik Pandya', '2026-06-01', 'Kolkata Knight Riders', 15, 2]
]

# 3. Write data to a temporary CSV file
with open(FILE_NAME, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Header row matching our Snowflake table columns exactly
    writer.writerow(['performance_id', 'player_name', 'match_date', 'opponent_team', 'runs_scored', 'wickets_taken'])
    writer.writerows(data)

print("Local CSV file created successfully.")

# 4. Push the file into your cloud storage bucket
try:
    s3.upload_file(FILE_NAME, BUCKET_NAME, FILE_NAME)
    print(f"Success! Uploaded {FILE_NAME} to S3 bucket: {BUCKET_NAME}")
except Exception as e:
    print(f"Error uploading to S3: {e}")
