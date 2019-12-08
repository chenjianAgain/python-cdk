from aws_cdk import (
    aws_s3 as s3,
    core
)


class DevopsStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        bucket = s3.Bucket(self, 
            "Devops5", 
            versioned=True,
            removal_policy=core.RemovalPolicy.DESTROY)
        core.CfnOutput(self, 'bucket', value="bucket_name:{}".format(
            bucket.bucket_name))
        
