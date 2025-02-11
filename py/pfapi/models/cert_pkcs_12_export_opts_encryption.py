from enum import Enum


class CertPkcs12ExportOptsEncryption(str, Enum):
    HIGH = "high"
    LEGACY = "legacy"
    LOW = "low"

    def __str__(self) -> str:
        return str(self.value)
