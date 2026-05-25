from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.snort_insp_rna_smb_fingerprints import SnortInspRnaSmbFingerprints
    from ..models.snort_insp_rna_tcp_fingerprints import SnortInspRnaTcpFingerprints
    from ..models.snort_insp_rna_ua_fingerprints import SnortInspRnaUaFingerprints
    from ..models.snort_insp_rna_udp_fingerprints import SnortInspRnaUdpFingerprints


T = TypeVar("T", bound="SnortInspRna")


@_attrs_define
class SnortInspRna:
    """
    Attributes:
        rna_conf_path (str | Unset): path to rna configuration
        enable_logger (bool | Unset): enable or disable writing discovery events into logger; default true
        log_when_idle (bool | Unset): enable host update logging when snort is idle; default false
        dump_file (str | Unset): file name to dump RNA mac cache on shutdown; won’t dump by default
        tcp_fingerprints (list[SnortInspRnaTcpFingerprints] | Unset):
        ua_fingerprints (list[SnortInspRnaUaFingerprints] | Unset):
        udp_fingerprints (list[SnortInspRnaUdpFingerprints] | Unset):
        smb_fingerprints (list[SnortInspRnaSmbFingerprints] | Unset):
    """

    rna_conf_path: str | Unset = UNSET
    enable_logger: bool | Unset = UNSET
    log_when_idle: bool | Unset = UNSET
    dump_file: str | Unset = UNSET
    tcp_fingerprints: list[SnortInspRnaTcpFingerprints] | Unset = UNSET
    ua_fingerprints: list[SnortInspRnaUaFingerprints] | Unset = UNSET
    udp_fingerprints: list[SnortInspRnaUdpFingerprints] | Unset = UNSET
    smb_fingerprints: list[SnortInspRnaSmbFingerprints] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rna_conf_path = self.rna_conf_path

        enable_logger = self.enable_logger

        log_when_idle = self.log_when_idle

        dump_file = self.dump_file

        tcp_fingerprints: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tcp_fingerprints, Unset):
            tcp_fingerprints = []
            for tcp_fingerprints_item_data in self.tcp_fingerprints:
                tcp_fingerprints_item = tcp_fingerprints_item_data.to_dict()
                tcp_fingerprints.append(tcp_fingerprints_item)

        ua_fingerprints: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ua_fingerprints, Unset):
            ua_fingerprints = []
            for ua_fingerprints_item_data in self.ua_fingerprints:
                ua_fingerprints_item = ua_fingerprints_item_data.to_dict()
                ua_fingerprints.append(ua_fingerprints_item)

        udp_fingerprints: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.udp_fingerprints, Unset):
            udp_fingerprints = []
            for udp_fingerprints_item_data in self.udp_fingerprints:
                udp_fingerprints_item = udp_fingerprints_item_data.to_dict()
                udp_fingerprints.append(udp_fingerprints_item)

        smb_fingerprints: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.smb_fingerprints, Unset):
            smb_fingerprints = []
            for smb_fingerprints_item_data in self.smb_fingerprints:
                smb_fingerprints_item = smb_fingerprints_item_data.to_dict()
                smb_fingerprints.append(smb_fingerprints_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rna_conf_path is not UNSET:
            field_dict["rna_conf_path"] = rna_conf_path
        if enable_logger is not UNSET:
            field_dict["enable_logger"] = enable_logger
        if log_when_idle is not UNSET:
            field_dict["log_when_idle"] = log_when_idle
        if dump_file is not UNSET:
            field_dict["dump_file"] = dump_file
        if tcp_fingerprints is not UNSET:
            field_dict["tcp_fingerprints"] = tcp_fingerprints
        if ua_fingerprints is not UNSET:
            field_dict["ua_fingerprints"] = ua_fingerprints
        if udp_fingerprints is not UNSET:
            field_dict["udp_fingerprints"] = udp_fingerprints
        if smb_fingerprints is not UNSET:
            field_dict["smb_fingerprints"] = smb_fingerprints

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.snort_insp_rna_smb_fingerprints import SnortInspRnaSmbFingerprints
        from ..models.snort_insp_rna_tcp_fingerprints import SnortInspRnaTcpFingerprints
        from ..models.snort_insp_rna_ua_fingerprints import SnortInspRnaUaFingerprints
        from ..models.snort_insp_rna_udp_fingerprints import SnortInspRnaUdpFingerprints

        d = dict(src_dict)
        rna_conf_path = d.pop("rna_conf_path", UNSET)

        enable_logger = d.pop("enable_logger", UNSET)

        log_when_idle = d.pop("log_when_idle", UNSET)

        dump_file = d.pop("dump_file", UNSET)

        _tcp_fingerprints = d.pop("tcp_fingerprints", UNSET)
        tcp_fingerprints: list[SnortInspRnaTcpFingerprints] | Unset = UNSET
        if _tcp_fingerprints is not UNSET:
            tcp_fingerprints = []
            for tcp_fingerprints_item_data in _tcp_fingerprints:
                tcp_fingerprints_item = SnortInspRnaTcpFingerprints.from_dict(tcp_fingerprints_item_data)

                tcp_fingerprints.append(tcp_fingerprints_item)

        _ua_fingerprints = d.pop("ua_fingerprints", UNSET)
        ua_fingerprints: list[SnortInspRnaUaFingerprints] | Unset = UNSET
        if _ua_fingerprints is not UNSET:
            ua_fingerprints = []
            for ua_fingerprints_item_data in _ua_fingerprints:
                ua_fingerprints_item = SnortInspRnaUaFingerprints.from_dict(ua_fingerprints_item_data)

                ua_fingerprints.append(ua_fingerprints_item)

        _udp_fingerprints = d.pop("udp_fingerprints", UNSET)
        udp_fingerprints: list[SnortInspRnaUdpFingerprints] | Unset = UNSET
        if _udp_fingerprints is not UNSET:
            udp_fingerprints = []
            for udp_fingerprints_item_data in _udp_fingerprints:
                udp_fingerprints_item = SnortInspRnaUdpFingerprints.from_dict(udp_fingerprints_item_data)

                udp_fingerprints.append(udp_fingerprints_item)

        _smb_fingerprints = d.pop("smb_fingerprints", UNSET)
        smb_fingerprints: list[SnortInspRnaSmbFingerprints] | Unset = UNSET
        if _smb_fingerprints is not UNSET:
            smb_fingerprints = []
            for smb_fingerprints_item_data in _smb_fingerprints:
                smb_fingerprints_item = SnortInspRnaSmbFingerprints.from_dict(smb_fingerprints_item_data)

                smb_fingerprints.append(smb_fingerprints_item)

        snort_insp_rna = cls(
            rna_conf_path=rna_conf_path,
            enable_logger=enable_logger,
            log_when_idle=log_when_idle,
            dump_file=dump_file,
            tcp_fingerprints=tcp_fingerprints,
            ua_fingerprints=ua_fingerprints,
            udp_fingerprints=udp_fingerprints,
            smb_fingerprints=smb_fingerprints,
        )

        snort_insp_rna.additional_properties = d
        return snort_insp_rna

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
