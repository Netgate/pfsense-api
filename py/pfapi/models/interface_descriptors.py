from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

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
        descriptors (Union[Unset, InterfaceDescriptorsInfo]): Mapping of interface names to their descriptions.
    """

    descriptors: Union[Unset, "InterfaceDescriptorsInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        descriptors: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.descriptors, Unset):
            descriptors = self.descriptors.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if descriptors is not UNSET:
            field_dict["descriptors"] = descriptors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.interface_descriptors_info import InterfaceDescriptorsInfo

        d = src_dict.copy()
        _descriptors = d.pop("descriptors", UNSET)
        descriptors: Union[Unset, InterfaceDescriptorsInfo]
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
