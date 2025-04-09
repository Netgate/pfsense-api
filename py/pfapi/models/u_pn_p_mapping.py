from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UPnPMapping")


@_attrs_define
class UPnPMapping:
    """
    Attributes:
        ext_interface (Union[Unset, str]):
        ext_port (Union[Unset, str]):
        int_ip (Union[Unset, str]):
        int_port (Union[Unset, str]):
        proto (Union[Unset, str]):
        source_ip (Union[Unset, str]):
        source_port (Union[Unset, str]):
        desc (Union[Unset, str]):
    """

    ext_interface: Union[Unset, str] = UNSET
    ext_port: Union[Unset, str] = UNSET
    int_ip: Union[Unset, str] = UNSET
    int_port: Union[Unset, str] = UNSET
    proto: Union[Unset, str] = UNSET
    source_ip: Union[Unset, str] = UNSET
    source_port: Union[Unset, str] = UNSET
    desc: Union[Unset, str] = UNSET
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
        field_dict.update({})
        if ext_interface is not UNSET:
            field_dict["ext_interface"] = ext_interface
        if ext_port is not UNSET:
            field_dict["ext_port"] = ext_port
        if int_ip is not UNSET:
            field_dict["int_ip"] = int_ip
        if int_port is not UNSET:
            field_dict["int_port"] = int_port
        if proto is not UNSET:
            field_dict["proto"] = proto
        if source_ip is not UNSET:
            field_dict["source_ip"] = source_ip
        if source_port is not UNSET:
            field_dict["source_port"] = source_port
        if desc is not UNSET:
            field_dict["desc"] = desc

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ext_interface = d.pop("ext_interface", UNSET)

        ext_port = d.pop("ext_port", UNSET)

        int_ip = d.pop("int_ip", UNSET)

        int_port = d.pop("int_port", UNSET)

        proto = d.pop("proto", UNSET)

        source_ip = d.pop("source_ip", UNSET)

        source_port = d.pop("source_port", UNSET)

        desc = d.pop("desc", UNSET)

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
