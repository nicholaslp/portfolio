import boto3
from botocore.client import Config
import StringIO
import zipfile
import mimetypes


def handler(event, context):


    location = {
        'bucketName': 'portfolio.alchemy-red.com-build',
        'objectKey': 'portfoliobuild.zip'
    }

    try:

        job = event.get('CodePipeline.job')

        if job:
            for artifact in job['data', 'inputArtifacts']
                if artifact['name'] == 'MyAppBuild'
                    location = artifact['location']['s3Location']


        print 'Building Portfolio: '+ str(location)
        s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))

        portfolio_bucket = s3.Bucket('portfolio.alchemy-red.com')
        build_bucket = s3.Bucket(location['bucketName'])

        sns = boto3.resource('sns')
        topic = sns.Topic('arn:aws:sns:us-east-1:227633078671:DeployPortfolioTopic')


        portfolio_zip = StringIO.StringIO()
        build_bucket.download_fileobj(location['objectKey'], portfolio_zip)

        with zipfile.ZipFile(portfolio_zip) as myzip:
            for nm in myzip.namelist():
                obj = myzip.open(nm)
                portfolio_bucket.upload_fileobj(obj, nm,
                    ExtraArgs={'ContentType':mimetypes.guess_type(nm)[0]})
                portfolio_bucket.Object(nm).Acl().put(ACL='public-read')


        topic.publish(Subject='Portfolio Deployed', Message='Lambda has successfully deployed your Porfolio Application.')

        print 'Portfolio Deployed'


        if job:
            codepipline = boto3.client('codepipeline')
            codepipeline = put_job_success_result(jobId=job['id'])


        return 'Portfolio Deployed'
    except:

        if job:
            codepipline = boto3.client('codepipeline')
            codepipeline = put_job_failure_result(jobId=job['id'])

        topic.publish(Subject='Portfolio Deploy Failed', Message='Lambda has failed to deployed your Porfolio Application.')
        print 'Portfolio Deploy Failed'
        return 'Portfolio Deploy Failed'

    return 'Portfolio Deploy Failed'
