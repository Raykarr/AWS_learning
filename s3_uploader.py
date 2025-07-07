import boto3
import json
from datetime import datetime, timezone

def upload_reflection(user_input, llm_output, config):
    s3 = boto3.client('s3', region_name=config['region'])

    # Use timezone-aware timestamp
    now = datetime.now(timezone.utc)

    data = {
        "timestamp": now.isoformat(),
        "user_input": user_input,
        "structured_output": llm_output
    }

    file_name = f"reflection_{now.strftime('%Y%m%dT%H%M%SZ')}.json"

    s3.put_object(
        Bucket=config["bucket_name"],
        Key=file_name,
        Body=json.dumps(data),
        ContentType='application/json'
    )

    print(f"✅ Saved reflection to S3 as '{file_name}'")
