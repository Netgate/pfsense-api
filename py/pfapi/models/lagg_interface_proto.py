from enum import Enum


class LAGGInterfaceProto(str, Enum):
    FAILOVER = "failover"
    LACP = "lacp"
    LOADBALANCE = "loadbalance"
    NONE = "none"
    ROUNDROBIN = "roundrobin"

    def __str__(self) -> str:
        return str(self.value)
