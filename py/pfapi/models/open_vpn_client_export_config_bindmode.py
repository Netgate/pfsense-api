from enum import Enum


class OpenVPNClientExportConfigBindmode(str, Enum):
    BIND = "bind"
    LPORT0 = "lport0"
    NOBIND = "nobind"

    def __str__(self) -> str:
        return str(self.value)
