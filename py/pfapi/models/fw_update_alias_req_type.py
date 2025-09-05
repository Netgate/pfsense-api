from enum import Enum


class FWUpdateAliasReqType(str, Enum):
    HOST = "host"
    NETWORK = "network"
    PORT = "port"
    URL = "url"
    URLTABLE = "urltable"
    URLTABLE_PORTS = "urltable_ports"
    URL_PORTS = "url_ports"

    def __str__(self) -> str:
        return str(self.value)
