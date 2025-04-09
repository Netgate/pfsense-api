from enum import Enum


class LimiterQueueAqm(str, Enum):
    CODEL = "codel"
    DROPTAIL = "droptail"
    GRED = "gred"
    PIE = "pie"
    RED = "red"

    def __str__(self) -> str:
        return str(self.value)
