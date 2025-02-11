from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dhcp_6_advanced_options import Dhcp6AdvancedOptions
    from ..models.dhcp_advanced_options import DhcpAdvancedOptions


T = TypeVar("T", bound="NetIfDhcp")


@_attrs_define
class NetIfDhcp:
    """
    Attributes:
        dhcp_hostname (str):
        dhcp_reject_from (List[str]):
        dhcp_vlan_enable (bool):
        dhcp_vlan_priority (int):
        dhcp6_usev4_iface (bool):
        dhcp6_prefix_only (bool):
        dhcp6_ia_pd_send_hint (bool):
        dhcp6_debug (bool):
        dhcp6_without_ra (bool):
        dhcp6_no_release (bool):
        dhcp6_vlan_priority (int):
        enable_adv_opt (bool): enable DHCP v4 advanced options
        enable_adv6_opt (bool): enable DHCP v6 advanced options
        dhcp_advanced (DhcpAdvancedOptions):
        dhcp6_advanced (Dhcp6AdvancedOptions):
    """

    dhcp_hostname: str
    dhcp_reject_from: List[str]
    dhcp_vlan_enable: bool
    dhcp_vlan_priority: int
    dhcp6_usev4_iface: bool
    dhcp6_prefix_only: bool
    dhcp6_ia_pd_send_hint: bool
    dhcp6_debug: bool
    dhcp6_without_ra: bool
    dhcp6_no_release: bool
    dhcp6_vlan_priority: int
    enable_adv_opt: bool
    enable_adv6_opt: bool
    dhcp_advanced: "DhcpAdvancedOptions"
    dhcp6_advanced: "Dhcp6AdvancedOptions"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dhcp_hostname = self.dhcp_hostname

        dhcp_reject_from = self.dhcp_reject_from

        dhcp_vlan_enable = self.dhcp_vlan_enable

        dhcp_vlan_priority = self.dhcp_vlan_priority

        dhcp6_usev4_iface = self.dhcp6_usev4_iface

        dhcp6_prefix_only = self.dhcp6_prefix_only

        dhcp6_ia_pd_send_hint = self.dhcp6_ia_pd_send_hint

        dhcp6_debug = self.dhcp6_debug

        dhcp6_without_ra = self.dhcp6_without_ra

        dhcp6_no_release = self.dhcp6_no_release

        dhcp6_vlan_priority = self.dhcp6_vlan_priority

        enable_adv_opt = self.enable_adv_opt

        enable_adv6_opt = self.enable_adv6_opt

        dhcp_advanced = self.dhcp_advanced.to_dict()

        dhcp6_advanced = self.dhcp6_advanced.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dhcp_hostname": dhcp_hostname,
                "dhcp_reject_from": dhcp_reject_from,
                "dhcp_vlan_enable": dhcp_vlan_enable,
                "dhcp_vlan_priority": dhcp_vlan_priority,
                "dhcp6_usev4_iface": dhcp6_usev4_iface,
                "dhcp6_prefix_only": dhcp6_prefix_only,
                "dhcp6_ia_pd_send_hint": dhcp6_ia_pd_send_hint,
                "dhcp6_debug": dhcp6_debug,
                "dhcp6_without_ra": dhcp6_without_ra,
                "dhcp6_no_release": dhcp6_no_release,
                "dhcp6_vlan_priority": dhcp6_vlan_priority,
                "enable_adv_opt": enable_adv_opt,
                "enable_adv6_opt": enable_adv6_opt,
                "dhcp_advanced": dhcp_advanced,
                "dhcp6_advanced": dhcp6_advanced,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dhcp_6_advanced_options import Dhcp6AdvancedOptions
        from ..models.dhcp_advanced_options import DhcpAdvancedOptions

        d = src_dict.copy()
        dhcp_hostname = d.pop("dhcp_hostname")

        dhcp_reject_from = cast(List[str], d.pop("dhcp_reject_from"))

        dhcp_vlan_enable = d.pop("dhcp_vlan_enable")

        dhcp_vlan_priority = d.pop("dhcp_vlan_priority")

        dhcp6_usev4_iface = d.pop("dhcp6_usev4_iface")

        dhcp6_prefix_only = d.pop("dhcp6_prefix_only")

        dhcp6_ia_pd_send_hint = d.pop("dhcp6_ia_pd_send_hint")

        dhcp6_debug = d.pop("dhcp6_debug")

        dhcp6_without_ra = d.pop("dhcp6_without_ra")

        dhcp6_no_release = d.pop("dhcp6_no_release")

        dhcp6_vlan_priority = d.pop("dhcp6_vlan_priority")

        enable_adv_opt = d.pop("enable_adv_opt")

        enable_adv6_opt = d.pop("enable_adv6_opt")

        dhcp_advanced = DhcpAdvancedOptions.from_dict(d.pop("dhcp_advanced"))

        dhcp6_advanced = Dhcp6AdvancedOptions.from_dict(d.pop("dhcp6_advanced"))

        net_if_dhcp = cls(
            dhcp_hostname=dhcp_hostname,
            dhcp_reject_from=dhcp_reject_from,
            dhcp_vlan_enable=dhcp_vlan_enable,
            dhcp_vlan_priority=dhcp_vlan_priority,
            dhcp6_usev4_iface=dhcp6_usev4_iface,
            dhcp6_prefix_only=dhcp6_prefix_only,
            dhcp6_ia_pd_send_hint=dhcp6_ia_pd_send_hint,
            dhcp6_debug=dhcp6_debug,
            dhcp6_without_ra=dhcp6_without_ra,
            dhcp6_no_release=dhcp6_no_release,
            dhcp6_vlan_priority=dhcp6_vlan_priority,
            enable_adv_opt=enable_adv_opt,
            enable_adv6_opt=enable_adv6_opt,
            dhcp_advanced=dhcp_advanced,
            dhcp6_advanced=dhcp6_advanced,
        )

        net_if_dhcp.additional_properties = d
        return net_if_dhcp

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
