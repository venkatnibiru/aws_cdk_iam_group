from aws_cdk import (
core as cdk,
aws_iam as iam
)
from aws_cdk_iam_group.myvars import *

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core


class AwsCdkIamGroupStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        devgroup= iam.Group(self, id="iam_devgroup", group_name=IAM_GROUPNAME)
        iampolicy= iam.ManagedPolicy.from_aws_managed_policy_name(managed_policy_name=IAM_POLICYNAME)
        #iampolicy.attach_to_group(devgroup)

