from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mdns_publishing import MDNSPublishing
    from ..models.text_value import TextValue


T = TypeVar("T", bound="MDNSConfig")


@_attrs_define
class MDNSConfig:
    """
    Attributes:
        enable (bool | Unset): enable mDNS service
        carp_vip_intf (str | Unset): name of CARP VIP interface for detecting current HA status. Service will be stopped
            when the chosen VIP is in Backup.
        include_interfaces (list[str] | Unset):
        exclude_interfaces (list[str] | Unset):
        disable_ipv4 (bool | Unset): disable IPv4 servicing
        disable_ipv6 (bool | Unset): disable IPv6 servicing
        reflection (bool | Unset): reflect packets across different subnets
        publish (MDNSPublishing | Unset):
        avail_interfaces (list[TextValue] | Unset):
        carp_vips (list[TextValue] | Unset):
    """

    enable: bool | Unset = UNSET
    carp_vip_intf: str | Unset = UNSET
    include_interfaces: list[str] | Unset = UNSET
    exclude_interfaces: list[str] | Unset = UNSET
    disable_ipv4: bool | Unset = UNSET
    disable_ipv6: bool | Unset = UNSET
    reflection: bool | Unset = UNSET
    publish: MDNSPublishing | Unset = UNSET
    avail_interfaces: list[TextValue] | Unset = UNSET
    carp_vips: list[TextValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        carp_vip_intf = self.carp_vip_intf

        include_interfaces: list[str] | Unset = UNSET
        if not isinstance(self.include_interfaces, Unset):
            include_interfaces = self.include_interfaces

        exclude_interfaces: list[str] | Unset = UNSET
        if not isinstance(self.exclude_interfaces, Unset):
            exclude_interfaces = self.exclude_interfaces

        disable_ipv4 = self.disable_ipv4

        disable_ipv6 = self.disable_ipv6

        reflection = self.reflection

        publish: dict[str, Any] | Unset = UNSET
        if not isinstance(self.publish, Unset):
            publish = self.publish.to_dict()

        avail_interfaces: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.avail_interfaces, Unset):
            avail_interfaces = []
            for avail_interfaces_item_data in self.avail_interfaces:
                avail_interfaces_item = avail_interfaces_item_data.to_dict()
                avail_interfaces.append(avail_interfaces_item)

        carp_vips: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.carp_vips, Unset):
            carp_vips = []
            for carp_vips_item_data in self.carp_vips:
                carp_vips_item = carp_vips_item_data.to_dict()
                carp_vips.append(carp_vips_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if carp_vip_intf is not UNSET:
            field_dict["carp_vip_intf"] = carp_vip_intf
        if include_interfaces is not UNSET:
            field_dict["include_interfaces"] = include_interfaces
        if exclude_interfaces is not UNSET:
            field_dict["exclude_interfaces"] = exclude_interfaces
        if disable_ipv4 is not UNSET:
            field_dict["disable_ipv4"] = disable_ipv4
        if disable_ipv6 is not UNSET:
            field_dict["disable_ipv6"] = disable_ipv6
        if reflection is not UNSET:
            field_dict["reflection"] = reflection
        if publish is not UNSET:
            field_dict["publish"] = publish
        if avail_interfaces is not UNSET:
            field_dict["avail_interfaces"] = avail_interfaces
        if carp_vips is not UNSET:
            field_dict["carp_vips"] = carp_vips

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mdns_publishing import MDNSPublishing
        from ..models.text_value import TextValue

        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        carp_vip_intf = d.pop("carp_vip_intf", UNSET)

        include_interfaces = cast(list[str], d.pop("include_interfaces", UNSET))

        exclude_interfaces = cast(list[str], d.pop("exclude_interfaces", UNSET))

        disable_ipv4 = d.pop("disable_ipv4", UNSET)

        disable_ipv6 = d.pop("disable_ipv6", UNSET)

        reflection = d.pop("reflection", UNSET)

        _publish = d.pop("publish", UNSET)
        publish: MDNSPublishing | Unset
        if isinstance(_publish, Unset):
            publish = UNSET
        else:
            publish = MDNSPublishing.from_dict(_publish)

        _avail_interfaces = d.pop("avail_interfaces", UNSET)
        avail_interfaces: list[TextValue] | Unset = UNSET
        if _avail_interfaces is not UNSET:
            avail_interfaces = []
            for avail_interfaces_item_data in _avail_interfaces:
                avail_interfaces_item = TextValue.from_dict(avail_interfaces_item_data)

                avail_interfaces.append(avail_interfaces_item)

        _carp_vips = d.pop("carp_vips", UNSET)
        carp_vips: list[TextValue] | Unset = UNSET
        if _carp_vips is not UNSET:
            carp_vips = []
            for carp_vips_item_data in _carp_vips:
                carp_vips_item = TextValue.from_dict(carp_vips_item_data)

                carp_vips.append(carp_vips_item)

        mdns_config = cls(
            enable=enable,
            carp_vip_intf=carp_vip_intf,
            include_interfaces=include_interfaces,
            exclude_interfaces=exclude_interfaces,
            disable_ipv4=disable_ipv4,
            disable_ipv6=disable_ipv6,
            reflection=reflection,
            publish=publish,
            avail_interfaces=avail_interfaces,
            carp_vips=carp_vips,
        )

        mdns_config.additional_properties = d
        return mdns_config

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
