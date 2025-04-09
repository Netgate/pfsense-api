from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WirelessAddlClone")


@_attrs_define
class WirelessAddlClone:
    """
    Attributes:
        if_ (Union[Unset, str]):
        mode (Union[Unset, str]):
        descr (Union[Unset, str]):
        cloneif (Union[Unset, str]):
    """

    if_: Union[Unset, str] = UNSET
    mode: Union[Unset, str] = UNSET
    descr: Union[Unset, str] = UNSET
    cloneif: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if_ = self.if_

        mode = self.mode

        descr = self.descr

        cloneif = self.cloneif

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if if_ is not UNSET:
            field_dict["if"] = if_
        if mode is not UNSET:
            field_dict["mode"] = mode
        if descr is not UNSET:
            field_dict["descr"] = descr
        if cloneif is not UNSET:
            field_dict["cloneif"] = cloneif

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        if_ = d.pop("if", UNSET)

        mode = d.pop("mode", UNSET)

        descr = d.pop("descr", UNSET)

        cloneif = d.pop("cloneif", UNSET)

        wireless_addl_clone = cls(
            if_=if_,
            mode=mode,
            descr=descr,
            cloneif=cloneif,
        )

        wireless_addl_clone.additional_properties = d
        return wireless_addl_clone

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
