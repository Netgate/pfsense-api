from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="L2TPRadius")


@_attrs_define
class L2TPRadius:
    """
    Attributes:
        server (str):
        secret (str):
        enable (bool):
        accounting (bool):
        radiusissueips (bool):
    """

    server: str
    secret: str
    enable: bool
    accounting: bool
    radiusissueips: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        server = self.server

        secret = self.secret

        enable = self.enable

        accounting = self.accounting

        radiusissueips = self.radiusissueips

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "server": server,
                "secret": secret,
                "enable": enable,
                "accounting": accounting,
                "radiusissueips": radiusissueips,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        server = d.pop("server")

        secret = d.pop("secret")

        enable = d.pop("enable")

        accounting = d.pop("accounting")

        radiusissueips = d.pop("radiusissueips")

        l2tp_radius = cls(
            server=server,
            secret=secret,
            enable=enable,
            accounting=accounting,
            radiusissueips=radiusissueips,
        )

        l2tp_radius.additional_properties = d
        return l2tp_radius

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
