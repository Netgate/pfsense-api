from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IfStats")


@_attrs_define
class IfStats:
    """
    Attributes:
        time (Union[Unset, int]):
        bytesin (Union[Unset, int]):
        bytesout (Union[Unset, int]):
    """

    time: Union[Unset, int] = UNSET
    bytesin: Union[Unset, int] = UNSET
    bytesout: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        time = self.time

        bytesin = self.bytesin

        bytesout = self.bytesout

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if bytesin is not UNSET:
            field_dict["bytesin"] = bytesin
        if bytesout is not UNSET:
            field_dict["bytesout"] = bytesout

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        time = d.pop("time", UNSET)

        bytesin = d.pop("bytesin", UNSET)

        bytesout = d.pop("bytesout", UNSET)

        if_stats = cls(
            time=time,
            bytesin=bytesin,
            bytesout=bytesout,
        )

        if_stats.additional_properties = d
        return if_stats

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
