from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LimiterInfo")


@_attrs_define
class LimiterInfo:
    """
    Attributes:
        pipes (Union[Unset, str]):
        sched (Union[Unset, str]):
        queues (Union[Unset, str]):
    """

    pipes: Union[Unset, str] = UNSET
    sched: Union[Unset, str] = UNSET
    queues: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pipes = self.pipes

        sched = self.sched

        queues = self.queues

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pipes is not UNSET:
            field_dict["pipes"] = pipes
        if sched is not UNSET:
            field_dict["sched"] = sched
        if queues is not UNSET:
            field_dict["queues"] = queues

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        pipes = d.pop("pipes", UNSET)

        sched = d.pop("sched", UNSET)

        queues = d.pop("queues", UNSET)

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
