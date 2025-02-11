from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="NetIfIpv6RD")


@_attrs_define
class NetIfIpv6RD:
    """
    Attributes:
        prefix_6rd (str):
        gateway_6rd (str):
        track6_prefix_id_hex (str):
        prefix_6rd_v4plen (str):
        track6_interface (str):
    """

    prefix_6rd: str
    gateway_6rd: str
    track6_prefix_id_hex: str
    prefix_6rd_v4plen: str
    track6_interface: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        prefix_6rd = self.prefix_6rd

        gateway_6rd = self.gateway_6rd

        track6_prefix_id_hex = self.track6_prefix_id_hex

        prefix_6rd_v4plen = self.prefix_6rd_v4plen

        track6_interface = self.track6_interface

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "prefix_6rd": prefix_6rd,
                "gateway_6rd": gateway_6rd,
                "track6_prefix_id_hex": track6_prefix_id_hex,
                "prefix_6rd_v4plen": prefix_6rd_v4plen,
                "track6_interface": track6_interface,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        prefix_6rd = d.pop("prefix_6rd")

        gateway_6rd = d.pop("gateway_6rd")

        track6_prefix_id_hex = d.pop("track6_prefix_id_hex")

        prefix_6rd_v4plen = d.pop("prefix_6rd_v4plen")

        track6_interface = d.pop("track6_interface")

        net_if_ipv_6rd = cls(
            prefix_6rd=prefix_6rd,
            gateway_6rd=gateway_6rd,
            track6_prefix_id_hex=track6_prefix_id_hex,
            prefix_6rd_v4plen=prefix_6rd_v4plen,
            track6_interface=track6_interface,
        )

        net_if_ipv_6rd.additional_properties = d
        return net_if_ipv_6rd

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
