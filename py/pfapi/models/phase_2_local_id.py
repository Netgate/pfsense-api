from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Phase2LocalId")


@_attrs_define
class Phase2LocalId:
    """
    Attributes:
        type (Union[Unset, str]):
        address (Union[Unset, str]):
        netbits (Union[Unset, str]):
    """

    type: Union[Unset, str] = UNSET
    address: Union[Unset, str] = UNSET
    netbits: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        address = self.address

        netbits = self.netbits

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if address is not UNSET:
            field_dict["address"] = address
        if netbits is not UNSET:
            field_dict["netbits"] = netbits

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        address = d.pop("address", UNSET)

        netbits = d.pop("netbits", UNSET)

        phase_2_local_id = cls(
            type=type,
            address=address,
            netbits=netbits,
        )

        phase_2_local_id.additional_properties = d
        return phase_2_local_id

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
