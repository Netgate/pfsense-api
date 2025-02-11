from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LimiterInfo")


@_attrs_define
class LimiterInfo:
    """
    Attributes:
        pipes (str):
        sched (str):
        queues (str):
    """

    pipes: str
    sched: str
    queues: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pipes = self.pipes

        sched = self.sched

        queues = self.queues

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pipes": pipes,
                "sched": sched,
                "queues": queues,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        pipes = d.pop("pipes")

        sched = d.pop("sched")

        queues = d.pop("queues")

        limiter_info = cls(
            pipes=pipes,
            sched=sched,
            queues=queues,
        )

        limiter_info.additional_properties = d
        return limiter_info

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
