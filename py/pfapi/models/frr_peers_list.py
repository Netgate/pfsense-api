from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.frr_bfd_peer import FrrBfdPeer
    from ..models.text_value import TextValue


T = TypeVar("T", bound="FrrPeersList")


@_attrs_define
class FrrPeersList:
    """
    Attributes:
        items (list[FrrBfdPeer] | Unset):
        profile_options (list[TextValue] | Unset):
        interface_options (list[TextValue] | Unset):
        local_address_options (list[TextValue] | Unset):
    """

    items: list[FrrBfdPeer] | Unset = UNSET
    profile_options: list[TextValue] | Unset = UNSET
    interface_options: list[TextValue] | Unset = UNSET
    local_address_options: list[TextValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        profile_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.profile_options, Unset):
            profile_options = []
            for profile_options_item_data in self.profile_options:
                profile_options_item = profile_options_item_data.to_dict()
                profile_options.append(profile_options_item)

        interface_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.interface_options, Unset):
            interface_options = []
            for interface_options_item_data in self.interface_options:
                interface_options_item = interface_options_item_data.to_dict()
                interface_options.append(interface_options_item)

        local_address_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.local_address_options, Unset):
            local_address_options = []
            for local_address_options_item_data in self.local_address_options:
                local_address_options_item = local_address_options_item_data.to_dict()
                local_address_options.append(local_address_options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if items is not UNSET:
            field_dict["items"] = items
        if profile_options is not UNSET:
            field_dict["profile_options"] = profile_options
        if interface_options is not UNSET:
            field_dict["interface_options"] = interface_options
        if local_address_options is not UNSET:
            field_dict["local_address_options"] = local_address_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.frr_bfd_peer import FrrBfdPeer
        from ..models.text_value import TextValue

        d = dict(src_dict)
        _items = d.pop("items", UNSET)
        items: list[FrrBfdPeer] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = FrrBfdPeer.from_dict(items_item_data)

                items.append(items_item)

        _profile_options = d.pop("profile_options", UNSET)
        profile_options: list[TextValue] | Unset = UNSET
        if _profile_options is not UNSET:
            profile_options = []
            for profile_options_item_data in _profile_options:
                profile_options_item = TextValue.from_dict(profile_options_item_data)

                profile_options.append(profile_options_item)

        _interface_options = d.pop("interface_options", UNSET)
        interface_options: list[TextValue] | Unset = UNSET
        if _interface_options is not UNSET:
            interface_options = []
            for interface_options_item_data in _interface_options:
                interface_options_item = TextValue.from_dict(interface_options_item_data)

                interface_options.append(interface_options_item)

        _local_address_options = d.pop("local_address_options", UNSET)
        local_address_options: list[TextValue] | Unset = UNSET
        if _local_address_options is not UNSET:
            local_address_options = []
            for local_address_options_item_data in _local_address_options:
                local_address_options_item = TextValue.from_dict(local_address_options_item_data)

                local_address_options.append(local_address_options_item)

        frr_peers_list = cls(
            items=items,
            profile_options=profile_options,
            interface_options=interface_options,
            local_address_options=local_address_options,
        )

        frr_peers_list.additional_properties = d
        return frr_peers_list

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
