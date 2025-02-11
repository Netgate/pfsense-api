from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TestPortRequest")


@_attrs_define
class TestPortRequest:
    """
    Attributes:
        host (str):
        src_port (str):
        src_ip (str):
        port (int):
        show_text (bool):
        ip_proto (str):
    """

    host: str
    src_port: str
    src_ip: str
    port: int
    show_text: bool
    ip_proto: str
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
        field_dict.update(
            {
                "host": host,
                "src_port": src_port,
                "src_ip": src_ip,
                "port": port,
                "show_text": show_text,
                "ip_proto": ip_proto,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        host = d.pop("host")

        src_port = d.pop("src_port")

        src_ip = d.pop("src_ip")

        port = d.pop("port")

        show_text = d.pop("show_text")

        ip_proto = d.pop("ip_proto")

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
