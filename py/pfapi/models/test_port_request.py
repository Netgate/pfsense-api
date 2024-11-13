from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TestPortRequest")


@_attrs_define
class TestPortRequest:
    """
    Attributes:
        host (Union[Unset, str]):
        src_port (Union[Unset, str]):
        src_ip (Union[Unset, str]):
        port (Union[Unset, int]):
        show_text (Union[Unset, bool]):
        ip_proto (Union[Unset, str]):
    """

    host: Union[Unset, str] = UNSET
    src_port: Union[Unset, str] = UNSET
    src_ip: Union[Unset, str] = UNSET
    port: Union[Unset, int] = UNSET
    show_text: Union[Unset, bool] = UNSET
    ip_proto: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        host = self.host

        src_port = self.src_port

        src_ip = self.src_ip

        port = self.port

        show_text = self.show_text

        ip_proto = self.ip_proto

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if host is not UNSET:
            field_dict["host"] = host
        if src_port is not UNSET:
            field_dict["src_port"] = src_port
        if src_ip is not UNSET:
            field_dict["src_ip"] = src_ip
        if port is not UNSET:
            field_dict["port"] = port
        if show_text is not UNSET:
            field_dict["show_text"] = show_text
        if ip_proto is not UNSET:
            field_dict["ip_proto"] = ip_proto

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        host = d.pop("host", UNSET)

        src_port = d.pop("src_port", UNSET)

        src_ip = d.pop("src_ip", UNSET)

        port = d.pop("port", UNSET)

        show_text = d.pop("show_text", UNSET)

        ip_proto = d.pop("ip_proto", UNSET)

        test_port_request = cls(
            host=host,
            src_port=src_port,
            src_ip=src_ip,
            port=port,
            show_text=show_text,
            ip_proto=ip_proto,
        )

        test_port_request.additional_properties = d
        return test_port_request

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
