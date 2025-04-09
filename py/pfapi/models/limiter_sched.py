from enum import Enum


class LimiterSched(str, Enum):
    FIFO = "fifo"
    FQ_CODEL = "fq_codel"
    FQ_PIE = "fq_pie"
    PRIO = "prio"
    QFQ = "qfq"
    RR = "rr"
    WF2Q = "wf2q+"

    def __str__(self) -> str:
        return str(self.value)
