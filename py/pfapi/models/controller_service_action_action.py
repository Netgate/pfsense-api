from enum import Enum


class ControllerServiceActionAction(str, Enum):
    RELOAD = "reload"
    RESTART = "restart"
    STOP = "stop"

    def __str__(self) -> str:
        return str(self.value)
