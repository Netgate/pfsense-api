from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RadiusServer")


@_attrs_define
class RadiusServer:
    """
    Attributes:
        ip (str):
        secret (Union[Unset, str]):
        port (Union[Unset, str]):
        acctport (Union[Unset, str]):
        enable (Union[Unset, bool]):
    """

    ip: str
    secret: Union[Unset, str] = UNSET
    port: Union[Unset, str] = UNSET
    acctport: Union[Unset, str] = UNSET
    enable: Union[Unset, bool] = UNSET
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
            }
        )
        if secret is not UNSET:
            field_dict["secret"] = secret
        if port is not UNSET:
            field_dict["port"] = port
        if acctport is not UNSET:
            field_dict["acctport"] = acctport
        if enable is not UNSET:
            field_dict["enable"] = enable

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ip = d.pop("ip")

        secret = d.pop("secret", UNSET)

        port = d.pop("port", UNSET)

        acctport = d.pop("acctport", UNSET)

        enable = d.pop("enable", UNSET)

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
