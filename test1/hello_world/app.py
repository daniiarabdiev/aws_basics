import json
import s3fs
from decouple import config


def lambda_handler(event, context):

    fs = s3fs.S3FileSystem(key=config('aws_key'), secret=config('aws_secret'))

    with fs.open('devinstantanalytics/email_templates/daily_refresh_success.json') as rfile:
        srfile = json.load(rfile)
        print(srfile)

    srfile['new_thing'] = 'something'

    with fs.open('devinstantanalytics/email_templates/daily_refresh_success.json', 'w') as wfile:
        json.dump(srfile, wfile)

    return {
        "statusCode": 200,
        "body": json.dumps(srfile),
    }


lambda_handler(event={}, context={})