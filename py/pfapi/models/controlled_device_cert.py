from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ControlledDeviceCert")


@_attrs_define
class ControlledDeviceCert:
    """
    Attributes:
        name (str):
        key (str):
        cert (str):
        ca_cert (str):
    """

    name: str
    key: str
    cert: str
    ca_cert: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        key = self.key

        cert = self.cert

        ca_cert = self.ca_cert

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "key": key,
                "cert": cert,
                "ca_cert": ca_cert,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        key = d.pop("key")

        cert = d.pop("cert")

        ca_cert = d.pop("ca_cert")

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
