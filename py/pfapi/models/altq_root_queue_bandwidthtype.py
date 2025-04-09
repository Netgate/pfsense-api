from enum import Enum


class ALTQRootQueueBandwidthtype(str, Enum):
    B = "b"
    GB = "Gb"
    KB = "Kb"
    MB = "Mb"
    VALUE_4 = "%"

    def __str__(self) -> str:
        return str(self.value)
