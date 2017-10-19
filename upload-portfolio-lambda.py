import boto3
from botocore.client import Config
import StringIO
import zipfile
import mimetypes


def lambda_handler(event, context):

    sns = boto3.resource('sns')
    topic = sns.Topic('arn:aws:sns:us-east-1:227633078671:DeployPortfolioTopic')

    location = {
        'bucketName': 'portfolio.alchemy-red.com-build',
        'objectKey': 'portfoliobuild.zip'
    }

    try:


        job = event.get('CodePipeline.job')

        if job:
            print str(job)

            for artifact in job['data', 'inputArtifacts']:
                if artifact['name'] == 'MyAppBuild':
                    location = artifact['location']['s3Location']


        print'Building Portfolio: '+ str(location)
        s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))

        portfolio_bucket = s3.Bucket('portfolio.alchemy-red.com')
        build_bucket = s3.Bucket(location['bucketName'])



        portfolio_zip = StringIO.StringIO()
        build_bucket.download_fileobj(location['objectKey'], portfolio_zip)

        with zipfile.ZipFile(portfolio_zip) as myzip:
            for nm in myzip.namelist():
                obj = myzip.open(nm)
                portfolio_bucket.upload_fileobj(obj, nm,
                    ExtraArgs={'ContentType':mimetypes.guess_type(nm)[0]})
                portfolio_bucket.Object(nm).Acl().put(ACL='public-read')


        topic.publish(Subject='Portfolio Deployed', Message='Lambda has successfully deployed your Porfolio Application.')

        if job:
            codepipeline = boto3.client('codepipeline')
            codepipeline.put_job_success_result(jobId=job['id'])


        print 'Portfolio Deployed'

    except:

        topic.publish(Subject='Portfolio Deploy Failed', Message='Lambda has failed to deployed your Porfolio Application.')
        raise

    return 'Portfolio Deploy Complete'
