from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ntp_access_restrictions import NtpAccessRestrictions


T = TypeVar("T", bound="NtpNetworkAccessRestriction")


@_attrs_define
class NtpNetworkAccessRestriction:
    """
    Attributes:
        network (str):
        mask (int | Unset):
        restrictions (NtpAccessRestrictions | Unset):
    """

    network: str
    mask: int | Unset = UNSET
    restrictions: NtpAccessRestrictions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        network = self.network

        mask = self.mask

        restrictions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.restrictions, Unset):
            restrictions = self.restrictions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "network": network,
            }
        )
        if mask is not UNSET:
            field_dict["mask"] = mask
        if restrictions is not UNSET:
            field_dict["restrictions"] = restrictions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ntp_access_restrictions import NtpAccessRestrictions

        d = dict(src_dict)
        network = d.pop("network")

        mask = d.pop("mask", UNSET)

        _restrictions = d.pop("restrictions", UNSET)
        restrictions: NtpAccessRestrictions | Unset
        if isinstance(_restrictions, Unset):
            restrictions = UNSET
        else:
            restrictions = NtpAccessRestrictions.from_dict(_restrictions)

        ntp_network_access_restriction = cls(
            network=network,
            mask=mask,
            restrictions=restrictions,
        )

        ntp_network_access_restriction.additional_properties = d
        return ntp_network_access_restriction

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
