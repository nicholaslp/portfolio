import boto3
s3 - boto.resource("s3")
s3 = boto.resource("s3")
s3 = boto3.resource("s3")
portfolio_bucket = s3.Bucket('portfolio.alchemy-red.com')
for obj in portfolio_bucket.objects.all():
    print obj.key
build_bucket - s3.Bucket('portfolio.alchemy-red.com-build')
build_bucket = s3.Bucket('portfolio.alchemy-red.com-build')
build_bucket.download('portfoliobuild.zip','/Downloads/portfoliobuild.zip')
build_bucket.download_file('portfoliobuild.zip','/Downloads/portfoliobuild.zip')
build_bucket.download_file('portfoliobuild.zip','/tmp/portfoliobuild.zip')
from botocore.client import Config
s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))
build_bucket = s3.Bucket('portfolio.alchemy-red.com-build')
build_bucket.download_file('portfoliobuild.zip','/tmp/portfoliobuild.zip')
for obj in build_bucket.objects.all():
    print obj.key
build_bucket.download_file('portfoliobuild.zip','/tmp/portfoliobuild.zip')
import StringIO
portfolio_zip = StringIO.StringIO()
build_bucket.download_fileobj('portfoliobuild.zip', portfolio_zip)
import zipfile
with zipfile.ZipFile(portfolio_zip) as myzip:
    for nm in myzip.namelist():
        print nm
with zipfile.ZipFile(portfolio_zip) as myzip:
    for nm in myzip.namelist():
        obj.myzip.open(nm)
        portfolio_bucket.upload_fileobj(obj, nm)
with zipfile.ZipFile(portfolio_zip) as myzip:
    for nm in myzip.namelist():
        obj = myzip.open(nm)
        portfolio_bucket.upload_fileobj(obj, nm)
with zipfile.ZipFile(portfolio_zip) as myzip:
    for nm in myzip.namelist():
        obj = myzip.open(nm)
        portfolio_bucket.upload_fileobj(obj, nm)
        portfolio_bucket.Object(nm).Acl().put(ACL='public-read')
