from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RadiusServer")


@_attrs_define
class RadiusServer:
    """
    Attributes:
        ip (str):
        secret (str):
        port (str):
        acctport (str):
        enable (bool):
    """

    ip: str
    secret: str
    port: str
    acctport: str
    enable: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ip = self.ip

        secret = self.secret

        port = self.port

        acctport = self.acctport

        enable = self.enable

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ip": ip,
                "secret": secret,
                "port": port,
                "acctport": acctport,
                "enable": enable,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ip = d.pop("ip")

        secret = d.pop("secret")

        port = d.pop("port")

        acctport = d.pop("acctport")

        enable = d.pop("enable")

        radius_server = cls(
            ip=ip,
            secret=secret,
            port=port,
            acctport=acctport,
            enable=enable,
        )

        radius_server.additional_properties = d
        return radius_server

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
