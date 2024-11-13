from enum import Enum


class DhcpGlobalSettingsIpv6DuidType(str, Enum):
    EN = "en"
    LL = "ll"
    LLT = "llt"
    RAW = "raw"
    UUID = "uuid"
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"

    def __str__(self) -> str:
        return str(self.value)
