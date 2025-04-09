from enum import Enum


class LimiterQueueMask(str, Enum):
    DSTADDRESS = "dstaddress"
    NONE = "none"
    SRCADDRESS = "srcaddress"

    def __str__(self) -> str:
        return str(self.value)
