from enum import Enum


class AwsWizardCreateTunnelsReqRouting(str, Enum):
    BGP = "BGP"
    STATIC = "static"

    def __str__(self) -> str:
        return str(self.value)
