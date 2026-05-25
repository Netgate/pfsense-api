from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AwsWizardVpn")


@_attrs_define
class AwsWizardVpn:
    """
    Attributes:
        vpnconnid (str | Unset): vpn connection id
        custgwcfg (str | Unset): base64 endcoded customer gateway configuration
    """

    vpnconnid: str | Unset = UNSET
    custgwcfg: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vpnconnid = self.vpnconnid

        custgwcfg = self.custgwcfg

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vpnconnid is not UNSET:
            field_dict["vpnconnid"] = vpnconnid
        if custgwcfg is not UNSET:
            field_dict["custgwcfg"] = custgwcfg

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        vpnconnid = d.pop("vpnconnid", UNSET)

        custgwcfg = d.pop("custgwcfg", UNSET)

        aws_wizard_vpn = cls(
            vpnconnid=vpnconnid,
            custgwcfg=custgwcfg,
        )

        aws_wizard_vpn.additional_properties = d
        return aws_wizard_vpn

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
