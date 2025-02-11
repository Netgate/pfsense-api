from enum import Enum


class CRLMethodInternalUpdateRevokeReason(str, Enum):
    AFFILCHANGE = "affilchange"
    CACOMPROMISE = "cacompromise"
    CERTHOLD = "certhold"
    CESSATION = "cessation"
    KEYCOMPROMISE = "keycompromise"
    NOSTATUS = "nostatus"
    PRIVWITHDRAWN = "privwithdrawn"
    SUPERSEDED = "superseded"
    UNSPECIFIED = "unspecified"

    def __str__(self) -> str:
        return str(self.value)
