import boto3
from botocore.client import Config
import StringIO
import zipfile
import mimetypes


def handler(event, context):

    s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))

    portfolio_bucket = s3.Bucket('portfolio.alchemy-red.com')
    build_bucket = s3.Bucket('portfolio.alchemy-red.com-build')


    portfolio_zip = StringIO.StringIO()
    build_bucket.download_fileobj('portfoliobuild.zip', portfolio_zip)

    with zipfile.ZipFile(portfolio_zip) as myzip:
        for nm in myzip.namelist():
            obj = myzip.open(nm)
            portfolio_bucket.upload_fileobj(obj, nm,
                ExtraArgs={'ContentType':mimetypes.guess_type(nm)[0]})
            portfolio_bucket.Object(nm).Acl().put(ACL='public-read')

    print 'Portfolio Deployed'
    return 'Portfolio Deployed'