from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RadiusAuthServer")


@_attrs_define
class RadiusAuthServer:
    """
    Attributes:
        type (Union[Unset, str]):
        name (Union[Unset, str]):
        host (Union[Unset, str]):
        protocol (Union[Unset, str]):
        nasip_attribute (Union[Unset, str]):
        secret (Union[Unset, str]):
        timeout (Union[Unset, int]):
        auth_port (Union[Unset, int]):
        acct_port (Union[Unset, int]):
        refid (Union[Unset, str]):
    """

    type: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    host: Union[Unset, str] = UNSET
    protocol: Union[Unset, str] = UNSET
    nasip_attribute: Union[Unset, str] = UNSET
    secret: Union[Unset, str] = UNSET
    timeout: Union[Unset, int] = UNSET
    auth_port: Union[Unset, int] = UNSET
    acct_port: Union[Unset, int] = UNSET
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
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if name is not UNSET:
            field_dict["name"] = name
        if host is not UNSET:
            field_dict["host"] = host
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if nasip_attribute is not UNSET:
            field_dict["nasip_attribute"] = nasip_attribute
        if secret is not UNSET:
            field_dict["secret"] = secret
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if auth_port is not UNSET:
            field_dict["auth_port"] = auth_port
        if acct_port is not UNSET:
            field_dict["acct_port"] = acct_port
        if refid is not UNSET:
            field_dict["refid"] = refid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        name = d.pop("name", UNSET)

        host = d.pop("host", UNSET)

        protocol = d.pop("protocol", UNSET)

        nasip_attribute = d.pop("nasip_attribute", UNSET)

        secret = d.pop("secret", UNSET)

        timeout = d.pop("timeout", UNSET)

        auth_port = d.pop("auth_port", UNSET)

        acct_port = d.pop("acct_port", UNSET)

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