from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FilterLogTCPInfo")


@_attrs_define
class FilterLogTCPInfo:
    """proto_id = 6

    Attributes:
        tcp_flags (Union[Unset, str]):
        seq (Union[Unset, str]):
        ack (Union[Unset, int]):
        window (Union[Unset, int]):
        urg (Union[Unset, int]):
        options (Union[Unset, str]):
    """

    tcp_flags: Union[Unset, str] = UNSET
    seq: Union[Unset, str] = UNSET
    ack: Union[Unset, int] = UNSET
    window: Union[Unset, int] = UNSET
    urg: Union[Unset, int] = UNSET
    options: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tcp_flags = self.tcp_flags

        seq = self.seq

        ack = self.ack

        window = self.window

        urg = self.urg

        options = self.options

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tcp_flags is not UNSET:
            field_dict["tcp_flags"] = tcp_flags
        if seq is not UNSET:
            field_dict["seq"] = seq
        if ack is not UNSET:
            field_dict["ack"] = ack
        if window is not UNSET:
            field_dict["window"] = window
        if urg is not UNSET:
            field_dict["urg"] = urg
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tcp_flags = d.pop("tcp_flags", UNSET)

        seq = d.pop("seq", UNSET)

        ack = d.pop("ack", UNSET)

        window = d.pop("window", UNSET)

        urg = d.pop("urg", UNSET)

        options = d.pop("options", UNSET)

        filter_log_tcp_info = cls(
            tcp_flags=tcp_flags,
            seq=seq,
            ack=ack,
            window=window,
            urg=urg,
            options=options,
        )

        filter_log_tcp_info.additional_properties = d
        return filter_log_tcp_info

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
