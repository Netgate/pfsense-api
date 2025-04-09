from enum import Enum


class ALTQRootQueueScheduler(str, Enum):
    CBQ = "CBQ"
    CODELQ = "CODELQ"
    FAIRQ = "FAIRQ"
    HFSC = "HFSC"
    PRIQ = "PRIQ"

    def __str__(self) -> str:
        return str(self.value)
