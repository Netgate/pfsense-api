from enum import Enum


class PPPInterfaceType(str, Enum):
    L2TP = "l2tp"
    PPP = "ppp"
    PPPOE = "pppoe"
    PPTP = "pptp"

    def __str__(self) -> str:
        return str(self.value)
