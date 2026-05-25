from enum import Enum


class OpenVPNClientExportConfigVerifyservercn(str, Enum):
    AUTO = "auto"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
