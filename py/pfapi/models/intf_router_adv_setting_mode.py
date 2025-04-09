from enum import Enum


class IntfRouterAdvSettingMode(str, Enum):
    ASSIST = "assist"
    DISABLED = "disabled"
    MANAGED = "managed"
    ROUTER = "router"
    STATELESS_DHCP = "stateless_dhcp"
    UNMANAGED = "unmanaged"

    def __str__(self) -> str:
        return str(self.value)
