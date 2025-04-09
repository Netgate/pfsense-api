from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PfInfo")


@_attrs_define
class PfInfo:
    """
    Attributes:
        info (Union[Unset, str]):
        memory (Union[Unset, str]):
        timeouts (Union[Unset, str]):
        interfaces (Union[Unset, str]):
    """

    info: Union[Unset, str] = UNSET
    memory: Union[Unset, str] = UNSET
    timeouts: Union[Unset, str] = UNSET
    interfaces: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        info = self.info

        memory = self.memory

        timeouts = self.timeouts

        interfaces = self.interfaces

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if info is not UNSET:
            field_dict["info"] = info
        if memory is not UNSET:
            field_dict["memory"] = memory
        if timeouts is not UNSET:
            field_dict["timeouts"] = timeouts
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        info = d.pop("info", UNSET)

        memory = d.pop("memory", UNSET)

        timeouts = d.pop("timeouts", UNSET)

        interfaces = d.pop("interfaces", UNSET)

        pf_info = cls(
            info=info,
            memory=memory,
            timeouts=timeouts,
            interfaces=interfaces,
        )

        pf_info.additional_properties = d
        return pf_info

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
