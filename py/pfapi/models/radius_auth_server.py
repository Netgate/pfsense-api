from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RadiusAuthServer")


@_attrs_define
class RadiusAuthServer:
    """
    Attributes:
        type (str):
        name (str):
        host (str):
        protocol (str): pap, chap_md5, mschapv1, mschapv2
        nasip_attribute (str):
        secret (str):
        timeout (int):
        auth_port (int):
        acct_port (int):
        refid (Union[Unset, str]):
    """

    type: str
    name: str
    host: str
    protocol: str
    nasip_attribute: str
    secret: str
    timeout: int
    auth_port: int
    acct_port: int
    refid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        name = self.name

        host = self.host

        protocol = self.protocol

        nasip_attribute = self.nasip_attribute

        secret = self.secret

        timeout = self.timeout

        auth_port = self.auth_port

        acct_port = self.acct_port

        refid = self.refid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "name": name,
                "host": host,
                "protocol": protocol,
                "nasip_attribute": nasip_attribute,
                "secret": secret,
                "timeout": timeout,
                "auth_port": auth_port,
                "acct_port": acct_port,
            }
        )
        if refid is not UNSET:
            field_dict["refid"] = refid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        name = d.pop("name")

        host = d.pop("host")

        protocol = d.pop("protocol")

        nasip_attribute = d.pop("nasip_attribute")

        secret = d.pop("secret")

        timeout = d.pop("timeout")

        auth_port = d.pop("auth_port")

        acct_port = d.pop("acct_port")

        refid = d.pop("refid", UNSET)

        radius_auth_server = cls(
            type=type,
            name=name,
            host=host,
            protocol=protocol,
            nasip_attribute=nasip_attribute,
            secret=secret,
            timeout=timeout,
            auth_port=auth_port,
            acct_port=acct_port,
            refid=refid,
        )

        radius_auth_server.additional_properties = d
        return radius_auth_server

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
