from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GatewayDefaults")


@_attrs_define
class GatewayDefaults:
    """
    Attributes:
        defaultgw4 (Union[Unset, str]):
        defaultgw6 (Union[Unset, str]):
    """

    defaultgw4: Union[Unset, str] = UNSET
    defaultgw6: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        defaultgw4 = self.defaultgw4

        defaultgw6 = self.defaultgw6

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if defaultgw4 is not UNSET:
            field_dict["defaultgw4"] = defaultgw4
        if defaultgw6 is not UNSET:
            field_dict["defaultgw6"] = defaultgw6

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        defaultgw4 = d.pop("defaultgw4", UNSET)

        defaultgw6 = d.pop("defaultgw6", UNSET)

        gateway_defaults = cls(
            defaultgw4=defaultgw4,
            defaultgw6=defaultgw6,
        )

        gateway_defaults.additional_properties = d
        return gateway_defaults

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
