from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.snort_insp_normalizer_ip_4 import SnortInspNormalizerIp4
    from ..models.snort_insp_normalizer_tcp import SnortInspNormalizerTcp


T = TypeVar("T", bound="SnortInspNormalizer")


@_attrs_define
class SnortInspNormalizer:
    """
    Attributes:
        ip4 (SnortInspNormalizerIp4 | Unset):
        tcp (SnortInspNormalizerTcp | Unset):
        ip6 (bool | Unset): clear reserved flag; default false
        icmp4 (bool | Unset): clear reserved flag; default false
        icmp6 (bool | Unset): clear reserved flag; default false
    """

    ip4: SnortInspNormalizerIp4 | Unset = UNSET
    tcp: SnortInspNormalizerTcp | Unset = UNSET
    ip6: bool | Unset = UNSET
    icmp4: bool | Unset = UNSET
    icmp6: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ip4: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ip4, Unset):
            ip4 = self.ip4.to_dict()

        tcp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tcp, Unset):
            tcp = self.tcp.to_dict()

        ip6 = self.ip6

        icmp4 = self.icmp4

        icmp6 = self.icmp6

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ip4 is not UNSET:
            field_dict["ip4"] = ip4
        if tcp is not UNSET:
            field_dict["tcp"] = tcp
        if ip6 is not UNSET:
            field_dict["ip6"] = ip6
        if icmp4 is not UNSET:
            field_dict["icmp4"] = icmp4
        if icmp6 is not UNSET:
            field_dict["icmp6"] = icmp6

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.snort_insp_normalizer_ip_4 import SnortInspNormalizerIp4
        from ..models.snort_insp_normalizer_tcp import SnortInspNormalizerTcp

        d = dict(src_dict)
        _ip4 = d.pop("ip4", UNSET)
        ip4: SnortInspNormalizerIp4 | Unset
        if isinstance(_ip4, Unset):
            ip4 = UNSET
        else:
            ip4 = SnortInspNormalizerIp4.from_dict(_ip4)

        _tcp = d.pop("tcp", UNSET)
        tcp: SnortInspNormalizerTcp | Unset
        if isinstance(_tcp, Unset):
            tcp = UNSET
        else:
            tcp = SnortInspNormalizerTcp.from_dict(_tcp)

        ip6 = d.pop("ip6", UNSET)

        icmp4 = d.pop("icmp4", UNSET)

        icmp6 = d.pop("icmp6", UNSET)

        snort_insp_normalizer = cls(
            ip4=ip4,
            tcp=tcp,
            ip6=ip6,
            icmp4=icmp4,
            icmp6=icmp6,
        )

        snort_insp_normalizer.additional_properties = d
        return snort_insp_normalizer

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
