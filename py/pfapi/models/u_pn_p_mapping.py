from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UPnPMapping")


@_attrs_define
class UPnPMapping:
    """
    Attributes:
        ext_interface (str):
        ext_port (str):
        int_ip (str):
        int_port (str):
        proto (str):
        source_ip (str):
        source_port (str):
        desc (str):
    """

    ext_interface: str
    ext_port: str
    int_ip: str
    int_port: str
    proto: str
    source_ip: str
    source_port: str
    desc: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ext_interface = self.ext_interface

        ext_port = self.ext_port

        int_ip = self.int_ip

        int_port = self.int_port

        proto = self.proto

        source_ip = self.source_ip

        source_port = self.source_port

        desc = self.desc

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ext_interface": ext_interface,
                "ext_port": ext_port,
                "int_ip": int_ip,
                "int_port": int_port,
                "proto": proto,
                "source_ip": source_ip,
                "source_port": source_port,
                "desc": desc,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ext_interface = d.pop("ext_interface")

        ext_port = d.pop("ext_port")

        int_ip = d.pop("int_ip")

        int_port = d.pop("int_port")

        proto = d.pop("proto")

        source_ip = d.pop("source_ip")

        source_port = d.pop("source_port")

        desc = d.pop("desc")

        u_pn_p_mapping = cls(
            ext_interface=ext_interface,
            ext_port=ext_port,
            int_ip=int_ip,
            int_port=int_port,
            proto=proto,
            source_ip=source_ip,
            source_port=source_port,
            desc=desc,
        )

        u_pn_p_mapping.additional_properties = d
        return u_pn_p_mapping

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
