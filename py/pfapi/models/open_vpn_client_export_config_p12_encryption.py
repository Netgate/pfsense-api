from enum import Enum


class OpenVPNClientExportConfigP12Encryption(str, Enum):
    HIGH = "high"
    LEGACY = "legacy"
    LOW = "low"

    def __str__(self) -> str:
        return str(self.value)
