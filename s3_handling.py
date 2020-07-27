import s3fs
from decouple import config
import pandas as pd


fs = s3fs.S3FileSystem(key=config('aws_key'), secret=config('aws_secret'))

the_bucket = 'devinstantanalytics'

path = 'devinstantanalytics/users/davyjonescompany/linkedin/data/linkedin_dashboard_one'

folders = fs.ls(path)
print(folders)

with fs.open(f'{the_bucket}/email_templates/daily_refresh_success.html') as rfile:
    srfile = rfile.read()
    print(srfile)


with fs.open(f'{the_bucket}/email_templates/changed_daily_refresh_success.html', 'w') as wfile:
    wfile.write('<p>something</p>')


with fs.open(f'{path}/all_linkedin_dashboard_one.csv') as rfile:
    df = pd.read_csv(rfile)
    print(df)


with fs.open(f'{path}/new_all_linkedin_dashboard_one.csv', 'w') as wfile:
    df.to_csv(wfile, index=False)







