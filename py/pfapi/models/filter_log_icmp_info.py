from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FilterLogICMPInfo")


@_attrs_define
class FilterLogICMPInfo:
    """proto_id 1, 58

    Attributes:
        icmp_type (Union[Unset, str]):
        icmp_id (Union[Unset, int]):
        icmp_seq (Union[Unset, int]):
        icmp_dstip (Union[Unset, str]):
        icmp_proto_id (Union[Unset, int]):
        icmp_port (Union[Unset, int]):
        icmp_descr (Union[Unset, str]):
        icmp_mtu (Union[Unset, int]):
        icmp_otime (Union[Unset, str]):
        icmp_rtime (Union[Unset, str]):
        icmp_ttime (Union[Unset, str]):
    """

    icmp_type: Union[Unset, str] = UNSET
    icmp_id: Union[Unset, int] = UNSET
    icmp_seq: Union[Unset, int] = UNSET
    icmp_dstip: Union[Unset, str] = UNSET
    icmp_proto_id: Union[Unset, int] = UNSET
    icmp_port: Union[Unset, int] = UNSET
    icmp_descr: Union[Unset, str] = UNSET
    icmp_mtu: Union[Unset, int] = UNSET
    icmp_otime: Union[Unset, str] = UNSET
    icmp_rtime: Union[Unset, str] = UNSET
    icmp_ttime: Union[Unset, str] = UNSET
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
        field_dict.update({})
        if icmp_type is not UNSET:
            field_dict["icmp_type"] = icmp_type
        if icmp_id is not UNSET:
            field_dict["icmp_id"] = icmp_id
        if icmp_seq is not UNSET:
            field_dict["icmp_seq"] = icmp_seq
        if icmp_dstip is not UNSET:
            field_dict["icmp_dstip"] = icmp_dstip
        if icmp_proto_id is not UNSET:
            field_dict["icmp_proto_id"] = icmp_proto_id
        if icmp_port is not UNSET:
            field_dict["icmp_port"] = icmp_port
        if icmp_descr is not UNSET:
            field_dict["icmp_descr"] = icmp_descr
        if icmp_mtu is not UNSET:
            field_dict["icmp_mtu"] = icmp_mtu
        if icmp_otime is not UNSET:
            field_dict["icmp_otime"] = icmp_otime
        if icmp_rtime is not UNSET:
            field_dict["icmp_rtime"] = icmp_rtime
        if icmp_ttime is not UNSET:
            field_dict["icmp_ttime"] = icmp_ttime

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        icmp_type = d.pop("icmp_type", UNSET)

        icmp_id = d.pop("icmp_id", UNSET)

        icmp_seq = d.pop("icmp_seq", UNSET)

        icmp_dstip = d.pop("icmp_dstip", UNSET)

        icmp_proto_id = d.pop("icmp_proto_id", UNSET)

        icmp_port = d.pop("icmp_port", UNSET)

        icmp_descr = d.pop("icmp_descr", UNSET)

        icmp_mtu = d.pop("icmp_mtu", UNSET)

        icmp_otime = d.pop("icmp_otime", UNSET)

        icmp_rtime = d.pop("icmp_rtime", UNSET)

        icmp_ttime = d.pop("icmp_ttime", UNSET)

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
