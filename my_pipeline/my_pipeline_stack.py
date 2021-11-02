from aws_cdk import core as cdk
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep

class MyPipelineStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        pipeline =  CodePipeline(self, "Pipeline123", 
                        pipeline_name="MyPipeline123",
                        synth=ShellStep("Synth", 
                            input=CodePipelineSource.connection("MoeinGh/send-email-cdk", "main" , 
                                connection_arn="arn:aws:codepipeline:eu-central-1:597729917624:bitbucket-cdk-p-Pipeline"
                            ),
                            commands=["npm install -g aws-cdk", 
                                "python -m pip install -r requirements.txt", 
                                "cdk synth"]
                        )
                    )
