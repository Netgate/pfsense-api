from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FilterLogICMPInfo")


@_attrs_define
class FilterLogICMPInfo:
    """proto_id 1, 58

    Attributes:
        icmp_type (str):
        icmp_id (int):
        icmp_seq (int):
        icmp_dstip (str):
        icmp_proto_id (int):
        icmp_port (int):
        icmp_descr (str):
        icmp_mtu (int):
        icmp_otime (str):
        icmp_rtime (str):
        icmp_ttime (str):
    """

    icmp_type: str
    icmp_id: int
    icmp_seq: int
    icmp_dstip: str
    icmp_proto_id: int
    icmp_port: int
    icmp_descr: str
    icmp_mtu: int
    icmp_otime: str
    icmp_rtime: str
    icmp_ttime: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        icmp_type = self.icmp_type

        icmp_id = self.icmp_id

        icmp_seq = self.icmp_seq

        icmp_dstip = self.icmp_dstip

        icmp_proto_id = self.icmp_proto_id

        icmp_port = self.icmp_port

        icmp_descr = self.icmp_descr

        icmp_mtu = self.icmp_mtu

        icmp_otime = self.icmp_otime

        icmp_rtime = self.icmp_rtime

        icmp_ttime = self.icmp_ttime

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "icmp_type": icmp_type,
                "icmp_id": icmp_id,
                "icmp_seq": icmp_seq,
                "icmp_dstip": icmp_dstip,
                "icmp_proto_id": icmp_proto_id,
                "icmp_port": icmp_port,
                "icmp_descr": icmp_descr,
                "icmp_mtu": icmp_mtu,
                "icmp_otime": icmp_otime,
                "icmp_rtime": icmp_rtime,
                "icmp_ttime": icmp_ttime,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        icmp_type = d.pop("icmp_type")

        icmp_id = d.pop("icmp_id")

        icmp_seq = d.pop("icmp_seq")

        icmp_dstip = d.pop("icmp_dstip")

        icmp_proto_id = d.pop("icmp_proto_id")

        icmp_port = d.pop("icmp_port")

        icmp_descr = d.pop("icmp_descr")

        icmp_mtu = d.pop("icmp_mtu")

        icmp_otime = d.pop("icmp_otime")

        icmp_rtime = d.pop("icmp_rtime")

        icmp_ttime = d.pop("icmp_ttime")

        filter_log_icmp_info = cls(
            icmp_type=icmp_type,
            icmp_id=icmp_id,
            icmp_seq=icmp_seq,
            icmp_dstip=icmp_dstip,
            icmp_proto_id=icmp_proto_id,
            icmp_port=icmp_port,
            icmp_descr=icmp_descr,
            icmp_mtu=icmp_mtu,
            icmp_otime=icmp_otime,
            icmp_rtime=icmp_rtime,
            icmp_ttime=icmp_ttime,
        )

        filter_log_icmp_info.additional_properties = d
        return filter_log_icmp_info

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
