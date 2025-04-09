from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ControlledDeviceCert")


@_attrs_define
class ControlledDeviceCert:
    """
    Attributes:
        name (Union[Unset, str]):
        key (Union[Unset, str]):
        cert (Union[Unset, str]):
        ca_cert (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    cert: Union[Unset, str] = UNSET
    ca_cert: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        key = self.key

        cert = self.cert

        ca_cert = self.ca_cert

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if key is not UNSET:
            field_dict["key"] = key
        if cert is not UNSET:
            field_dict["cert"] = cert
        if ca_cert is not UNSET:
            field_dict["ca_cert"] = ca_cert

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        key = d.pop("key", UNSET)

        cert = d.pop("cert", UNSET)

        ca_cert = d.pop("ca_cert", UNSET)

        controlled_device_cert = cls(
            name=name,
            key=key,
            cert=cert,
            ca_cert=ca_cert,
        )

        controlled_device_cert.additional_properties = d
        return controlled_device_cert

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
