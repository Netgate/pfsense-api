from enum import Enum


class SnortInterfaceConfigDetectionMethod(str, Enum):
    AC_BNFA = "ac_bnfa"
    AC_FULL = "ac_full"
    HYPERSCAN = "hyperscan"

    def __str__(self) -> str:
        return str(self.value)
