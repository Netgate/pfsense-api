from enum import Enum


class AwsWizardCredPartition(str, Enum):
    AWS = "aws"
    AWS_US_GOV = "aws-us-gov"

    def __str__(self) -> str:
        return str(self.value)
