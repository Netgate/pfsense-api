from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CaCertMethodExisting")


@_attrs_define
class CaCertMethodExisting:
    """Existing PEM certificate and key, either in PEM format or base64-encoded

    Attributes:
        cert (str):
        private_key (str):
        next_serial (int):
    """

    cert: str
    private_key: str
    next_serial: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cert = self.cert

        private_key = self.private_key

        next_serial = self.next_serial

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cert": cert,
                "private_key": private_key,
                "next_serial": next_serial,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cert = d.pop("cert")

        private_key = d.pop("private_key")

        next_serial = d.pop("next_serial")

        ca_cert_method_existing = cls(
            cert=cert,
            private_key=private_key,
            next_serial=next_serial,
        )

        ca_cert_method_existing.additional_properties = d
        return ca_cert_method_existing

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
