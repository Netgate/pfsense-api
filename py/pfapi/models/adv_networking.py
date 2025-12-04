from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.adv_network_setting import AdvNetworkSetting


T = TypeVar("T", bound="AdvNetworking")


@_attrs_define
class AdvNetworking:
    """
    Attributes:
        networking (AdvNetworkSetting | Unset):
    """

    networking: AdvNetworkSetting | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        networking: dict[str, Any] | Unset = UNSET
        if not isinstance(self.networking, Unset):
            networking = self.networking.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if networking is not UNSET:
            field_dict["networking"] = networking

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.adv_network_setting import AdvNetworkSetting

        d = dict(src_dict)
        _networking = d.pop("networking", UNSET)
        networking: AdvNetworkSetting | Unset
        if isinstance(_networking, Unset):
            networking = UNSET
        else:
            networking = AdvNetworkSetting.from_dict(_networking)

        adv_networking = cls(
            networking=networking,
        )

        adv_networking.additional_properties = d
        return adv_networking

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
