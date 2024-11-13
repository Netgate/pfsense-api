from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LoadAvg")


@_attrs_define
class LoadAvg:
    """
    Attributes:
        loadavg (Union[Unset, List[int]]):
    """

    loadavg: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        loadavg: Union[Unset, List[int]] = UNSET
        if not isinstance(self.loadavg, Unset):
            loadavg = self.loadavg

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if loadavg is not UNSET:
            field_dict["loadavg"] = loadavg

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        loadavg = cast(List[int], d.pop("loadavg", UNSET))

        load_avg = cls(
            loadavg=loadavg,
        )

        load_avg.additional_properties = d
        return load_avg

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
