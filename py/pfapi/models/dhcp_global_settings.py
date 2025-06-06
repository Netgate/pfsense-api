from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dhcp_global_settings_ipv_6_duid_type import DhcpGlobalSettingsIpv6DuidType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DhcpGlobalSettings")


@_attrs_define
class DhcpGlobalSettings:
    """
    Attributes:
        backend (Union[Unset, str]):
        radvd_debug (Union[Unset, bool]):
        dhcp6_debug (Union[Unset, bool]):
        address_release (Union[Unset, bool]):
        ipv6_duid_type (Union[Unset, DhcpGlobalSettingsIpv6DuidType]): A DHCPv6 Unique Identifier (DUID) is used by the
            firewall when requesting an IPv6 address.

            By default, the firewall automatically creates a dynamic DUID-LLT which is not saved
            in the firewall configuration. To ensure that the same DUID is retained by the firewall
            at all times, enter a DUID in this section. The new DUID will take effect after a
            reboot or when the WAN interface(s) are reconfigured by the firewall.

            If the firewall is configured to use a RAM disk for state (such as /var), the best
            practice is to store a DUID here; otherwise, the DUID will change on each reboot.

            When setting the config, if duid type is 0/raw and no value for ipv6_duid_raw is provided,
            then the DUID will be removed from the firewall configuration.
        ipv6_duid_raw (Union[Unset, str]):
        ipv6_duid_llt_time (Union[Unset, str]):
        ipv6_duid_llt_ll (Union[Unset, str]):
        ipv6_duid_en_en (Union[Unset, str]):
        ipv6_duid_en_id (Union[Unset, str]):
        ipv6_duid_ll (Union[Unset, str]):
        ipv6_duid_uuid (Union[Unset, str]):
    """

    backend: Union[Unset, str] = UNSET
    radvd_debug: Union[Unset, bool] = UNSET
    dhcp6_debug: Union[Unset, bool] = UNSET
    address_release: Union[Unset, bool] = UNSET
    ipv6_duid_type: Union[Unset, DhcpGlobalSettingsIpv6DuidType] = UNSET
    ipv6_duid_raw: Union[Unset, str] = UNSET
    ipv6_duid_llt_time: Union[Unset, str] = UNSET
    ipv6_duid_llt_ll: Union[Unset, str] = UNSET
    ipv6_duid_en_en: Union[Unset, str] = UNSET
    ipv6_duid_en_id: Union[Unset, str] = UNSET
    ipv6_duid_ll: Union[Unset, str] = UNSET
    ipv6_duid_uuid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        backend = self.backend

        radvd_debug = self.radvd_debug

        dhcp6_debug = self.dhcp6_debug

        address_release = self.address_release

        ipv6_duid_type: Union[Unset, str] = UNSET
        if not isinstance(self.ipv6_duid_type, Unset):
            ipv6_duid_type = self.ipv6_duid_type.value

        ipv6_duid_raw = self.ipv6_duid_raw

        ipv6_duid_llt_time = self.ipv6_duid_llt_time

        ipv6_duid_llt_ll = self.ipv6_duid_llt_ll

        ipv6_duid_en_en = self.ipv6_duid_en_en

        ipv6_duid_en_id = self.ipv6_duid_en_id

        ipv6_duid_ll = self.ipv6_duid_ll

        ipv6_duid_uuid = self.ipv6_duid_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backend is not UNSET:
            field_dict["backend"] = backend
        if radvd_debug is not UNSET:
            field_dict["radvd_debug"] = radvd_debug
        if dhcp6_debug is not UNSET:
            field_dict["dhcp6_debug"] = dhcp6_debug
        if address_release is not UNSET:
            field_dict["address_release"] = address_release
        if ipv6_duid_type is not UNSET:
            field_dict["ipv6_duid_type"] = ipv6_duid_type
        if ipv6_duid_raw is not UNSET:
            field_dict["ipv6_duid_raw"] = ipv6_duid_raw
        if ipv6_duid_llt_time is not UNSET:
            field_dict["ipv6_duid_llt_time"] = ipv6_duid_llt_time
        if ipv6_duid_llt_ll is not UNSET:
            field_dict["ipv6_duid_llt_ll"] = ipv6_duid_llt_ll
        if ipv6_duid_en_en is not UNSET:
            field_dict["ipv6_duid_en_en"] = ipv6_duid_en_en
        if ipv6_duid_en_id is not UNSET:
            field_dict["ipv6_duid_en_id"] = ipv6_duid_en_id
        if ipv6_duid_ll is not UNSET:
            field_dict["ipv6_duid_ll"] = ipv6_duid_ll
        if ipv6_duid_uuid is not UNSET:
            field_dict["ipv6_duid_uuid"] = ipv6_duid_uuid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        backend = d.pop("backend", UNSET)

        radvd_debug = d.pop("radvd_debug", UNSET)

        dhcp6_debug = d.pop("dhcp6_debug", UNSET)

        address_release = d.pop("address_release", UNSET)

        _ipv6_duid_type = d.pop("ipv6_duid_type", UNSET)
        ipv6_duid_type: Union[Unset, DhcpGlobalSettingsIpv6DuidType]
        if isinstance(_ipv6_duid_type, Unset):
            ipv6_duid_type = UNSET
        else:
            ipv6_duid_type = DhcpGlobalSettingsIpv6DuidType(_ipv6_duid_type)

        ipv6_duid_raw = d.pop("ipv6_duid_raw", UNSET)

        ipv6_duid_llt_time = d.pop("ipv6_duid_llt_time", UNSET)

        ipv6_duid_llt_ll = d.pop("ipv6_duid_llt_ll", UNSET)

        ipv6_duid_en_en = d.pop("ipv6_duid_en_en", UNSET)

        ipv6_duid_en_id = d.pop("ipv6_duid_en_id", UNSET)

        ipv6_duid_ll = d.pop("ipv6_duid_ll", UNSET)

        ipv6_duid_uuid = d.pop("ipv6_duid_uuid", UNSET)

        dhcp_global_settings = cls(
            backend=backend,
            radvd_debug=radvd_debug,
            dhcp6_debug=dhcp6_debug,
            address_release=address_release,
            ipv6_duid_type=ipv6_duid_type,
            ipv6_duid_raw=ipv6_duid_raw,
            ipv6_duid_llt_time=ipv6_duid_llt_time,
            ipv6_duid_llt_ll=ipv6_duid_llt_ll,
            ipv6_duid_en_en=ipv6_duid_en_en,
            ipv6_duid_en_id=ipv6_duid_en_id,
            ipv6_duid_ll=ipv6_duid_ll,
            ipv6_duid_uuid=ipv6_duid_uuid,
        )

        dhcp_global_settings.additional_properties = d
        return dhcp_global_settings

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
