from enum import Enum


class SnortInterfaceConfigBlockAddrOpt(str, Enum):
    BOTH = "both"
    DST = "dst"
    SRC = "src"

    def __str__(self) -> str:
        return str(self.value)
