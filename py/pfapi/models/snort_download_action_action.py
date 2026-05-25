from enum import Enum


class SnortDownloadActionAction(str, Enum):
    RESUME = "resume"
    START = "start"
    STOP = "stop"
    SUSPEND = "suspend"

    def __str__(self) -> str:
        return str(self.value)
