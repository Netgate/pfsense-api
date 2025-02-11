from enum import Enum


class NetIfAssignOwnerReqOwnerType(str, Enum):
    CONTAINER = "container"
    HOST = "host"
    VM = "vm"
    VPP = "vpp"

    def __str__(self) -> str:
        return str(self.value)
