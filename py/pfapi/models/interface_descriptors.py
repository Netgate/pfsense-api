from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.interface_descriptors_info import InterfaceDescriptorsInfo


T = TypeVar("T", bound="InterfaceDescriptors")


@_attrs_define
class InterfaceDescriptors:
    """
    Attributes:
        descriptors (InterfaceDescriptorsInfo | Unset): Mapping of interface names to their descriptions.
    """

    descriptors: InterfaceDescriptorsInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        descriptors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.descriptors, Unset):
            descriptors = self.descriptors.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if descriptors is not UNSET:
            field_dict["descriptors"] = descriptors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.interface_descriptors_info import InterfaceDescriptorsInfo

        d = dict(src_dict)
        _descriptors = d.pop("descriptors", UNSET)
        descriptors: InterfaceDescriptorsInfo | Unset
        if isinstance(_descriptors, Unset):
            descriptors = UNSET
        else:
            descriptors = InterfaceDescriptorsInfo.from_dict(_descriptors)

        interface_descriptors = cls(
            descriptors=descriptors,
        )

        interface_descriptors.additional_properties = d
        return interface_descriptors

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
