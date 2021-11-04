from aws_cdk import core as cdk
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
from aws_cdk import (
    core,
    aws_lambda as _lambda,
    aws_apigateway as _apigw,
    aws_s3_notifications,
     aws_s3 as _s3,
)

class MyPipelineStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        pipeline =  CodePipeline(self, "Pipeline", 
                        pipeline_name="MyPipeline",
                        synth=ShellStep("Synth", 
                            input=CodePipelineSource.connection("MoeinGh/send-email-cdk", "main" , 
                                connection_arn="arn:aws:codestar-connections:eu-central-1:597729917624:connection/bbc30f95-9181-43a3-a4b5-60098faed96c"
                            ),
                            commands=[
                                # "/root/.pyenv/versions/3.9.5/bin/python -m pip install --upgrade pip", 
                                "npm install -g aws-cdk", 
                                "python -m pip install -r requirements.txt", 
                                "cdk synth"]
                        )
                    )

         # create lambda function
        function = _lambda.Function(self, "lambda_function",
                                    runtime=_lambda.Runtime.PYTHON_3_7,
                                    handler="lambda-handler.main",
                                    code=_lambda.Code.asset("./lambda"))

        # create s3 bucket
        s3 = _s3.Bucket(self, "s3bucket")

        # create s3 notification for lambda function
        notification = aws_s3_notifications.LambdaDestination(function)

        # assign notification for the s3 event type (ex: OBJECT_CREATED)
        s3.add_event_notification(_s3.EventType.OBJECT_CREATED, notification)