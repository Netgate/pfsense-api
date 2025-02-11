from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FilterLogTCPInfo")


@_attrs_define
class FilterLogTCPInfo:
    """proto_id = 6

    Attributes:
        tcp_flags (str):
        seq (str):
        ack (int):
        window (int):
        urg (int):
        options (str):
    """

    tcp_flags: str
    seq: str
    ack: int
    window: int
    urg: int
    options: str
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
        field_dict.update(
            {
                "tcp_flags": tcp_flags,
                "seq": seq,
                "ack": ack,
                "window": window,
                "urg": urg,
                "options": options,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tcp_flags = d.pop("tcp_flags")

        seq = d.pop("seq")

        ack = d.pop("ack")

        window = d.pop("window")

        urg = d.pop("urg")

        options = d.pop("options")

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
