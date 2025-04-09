from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dhcp_6_advanced_options import Dhcp6AdvancedOptions
    from ..models.dhcp_advanced_options import DhcpAdvancedOptions


T = TypeVar("T", bound="NetIfDhcp")


@_attrs_define
class NetIfDhcp:
    """
    Attributes:
        dhcp_hostname (Union[Unset, str]):
        dhcp_reject_from (Union[Unset, List[str]]):
        dhcp_vlan_enable (Union[Unset, bool]):
        dhcp_vlan_priority (Union[Unset, int]):
        dhcp6_usev4_iface (Union[Unset, bool]):
        dhcp6_prefix_only (Union[Unset, bool]):
        dhcp6_ia_pd_send_hint (Union[Unset, bool]):
        dhcp6_debug (Union[Unset, bool]):
        dhcp6_without_ra (Union[Unset, bool]):
        dhcp6_no_release (Union[Unset, bool]):
        dhcp6_vlan_priority (Union[Unset, int]):
        enable_adv_opt (Union[Unset, bool]): enable DHCP v4 advanced options
        enable_adv6_opt (Union[Unset, bool]): enable DHCP v6 advanced options
        dhcp_advanced (Union[Unset, DhcpAdvancedOptions]):
        dhcp6_advanced (Union[Unset, Dhcp6AdvancedOptions]):
    """

    dhcp_hostname: Union[Unset, str] = UNSET
    dhcp_reject_from: Union[Unset, List[str]] = UNSET
    dhcp_vlan_enable: Union[Unset, bool] = UNSET
    dhcp_vlan_priority: Union[Unset, int] = UNSET
    dhcp6_usev4_iface: Union[Unset, bool] = UNSET
    dhcp6_prefix_only: Union[Unset, bool] = UNSET
    dhcp6_ia_pd_send_hint: Union[Unset, bool] = UNSET
    dhcp6_debug: Union[Unset, bool] = UNSET
    dhcp6_without_ra: Union[Unset, bool] = UNSET
    dhcp6_no_release: Union[Unset, bool] = UNSET
    dhcp6_vlan_priority: Union[Unset, int] = UNSET
    enable_adv_opt: Union[Unset, bool] = UNSET
    enable_adv6_opt: Union[Unset, bool] = UNSET
    dhcp_advanced: Union[Unset, "DhcpAdvancedOptions"] = UNSET
    dhcp6_advanced: Union[Unset, "Dhcp6AdvancedOptions"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dhcp_hostname = self.dhcp_hostname

        dhcp_reject_from: Union[Unset, List[str]] = UNSET
        if not isinstance(self.dhcp_reject_from, Unset):
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

        dhcp_advanced: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dhcp_advanced, Unset):
            dhcp_advanced = self.dhcp_advanced.to_dict()

        dhcp6_advanced: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dhcp6_advanced, Unset):
            dhcp6_advanced = self.dhcp6_advanced.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dhcp_hostname is not UNSET:
            field_dict["dhcp_hostname"] = dhcp_hostname
        if dhcp_reject_from is not UNSET:
            field_dict["dhcp_reject_from"] = dhcp_reject_from
        if dhcp_vlan_enable is not UNSET:
            field_dict["dhcp_vlan_enable"] = dhcp_vlan_enable
        if dhcp_vlan_priority is not UNSET:
            field_dict["dhcp_vlan_priority"] = dhcp_vlan_priority
        if dhcp6_usev4_iface is not UNSET:
            field_dict["dhcp6_usev4_iface"] = dhcp6_usev4_iface
        if dhcp6_prefix_only is not UNSET:
            field_dict["dhcp6_prefix_only"] = dhcp6_prefix_only
        if dhcp6_ia_pd_send_hint is not UNSET:
            field_dict["dhcp6_ia_pd_send_hint"] = dhcp6_ia_pd_send_hint
        if dhcp6_debug is not UNSET:
            field_dict["dhcp6_debug"] = dhcp6_debug
        if dhcp6_without_ra is not UNSET:
            field_dict["dhcp6_without_ra"] = dhcp6_without_ra
        if dhcp6_no_release is not UNSET:
            field_dict["dhcp6_no_release"] = dhcp6_no_release
        if dhcp6_vlan_priority is not UNSET:
            field_dict["dhcp6_vlan_priority"] = dhcp6_vlan_priority
        if enable_adv_opt is not UNSET:
            field_dict["enable_adv_opt"] = enable_adv_opt
        if enable_adv6_opt is not UNSET:
            field_dict["enable_adv6_opt"] = enable_adv6_opt
        if dhcp_advanced is not UNSET:
            field_dict["dhcp_advanced"] = dhcp_advanced
        if dhcp6_advanced is not UNSET:
            field_dict["dhcp6_advanced"] = dhcp6_advanced

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dhcp_6_advanced_options import Dhcp6AdvancedOptions
        from ..models.dhcp_advanced_options import DhcpAdvancedOptions

        d = src_dict.copy()
        dhcp_hostname = d.pop("dhcp_hostname", UNSET)

        dhcp_reject_from = cast(List[str], d.pop("dhcp_reject_from", UNSET))

        dhcp_vlan_enable = d.pop("dhcp_vlan_enable", UNSET)

        dhcp_vlan_priority = d.pop("dhcp_vlan_priority", UNSET)

        dhcp6_usev4_iface = d.pop("dhcp6_usev4_iface", UNSET)

        dhcp6_prefix_only = d.pop("dhcp6_prefix_only", UNSET)

        dhcp6_ia_pd_send_hint = d.pop("dhcp6_ia_pd_send_hint", UNSET)

        dhcp6_debug = d.pop("dhcp6_debug", UNSET)

        dhcp6_without_ra = d.pop("dhcp6_without_ra", UNSET)

        dhcp6_no_release = d.pop("dhcp6_no_release", UNSET)

        dhcp6_vlan_priority = d.pop("dhcp6_vlan_priority", UNSET)

        enable_adv_opt = d.pop("enable_adv_opt", UNSET)

        enable_adv6_opt = d.pop("enable_adv6_opt", UNSET)

        _dhcp_advanced = d.pop("dhcp_advanced", UNSET)
        dhcp_advanced: Union[Unset, DhcpAdvancedOptions]
        if isinstance(_dhcp_advanced, Unset):
            dhcp_advanced = UNSET
        else:
            dhcp_advanced = DhcpAdvancedOptions.from_dict(_dhcp_advanced)

        _dhcp6_advanced = d.pop("dhcp6_advanced", UNSET)
        dhcp6_advanced: Union[Unset, Dhcp6AdvancedOptions]
        if isinstance(_dhcp6_advanced, Unset):
            dhcp6_advanced = UNSET
        else:
            dhcp6_advanced = Dhcp6AdvancedOptions.from_dict(_dhcp6_advanced)

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
