from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InterfaceAssignedName")


@_attrs_define
class InterfaceAssignedName:
    """
    Attributes:
        device (Union[Unset, str]): interface device, e.g. igbe0
        ident (Union[Unset, str]): identity, e.g. wan, lan, opt1
        assigned (Union[Unset, str]): user assigned name, e.g. WAN, LAN, MYLAN
    """

    device: Union[Unset, str] = UNSET
    ident: Union[Unset, str] = UNSET
    assigned: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        device = self.device

        ident = self.ident

        assigned = self.assigned

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device is not UNSET:
            field_dict["device"] = device
        if ident is not UNSET:
            field_dict["ident"] = ident
        if assigned is not UNSET:
            field_dict["assigned"] = assigned

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        device = d.pop("device", UNSET)

        ident = d.pop("ident", UNSET)

        assigned = d.pop("assigned", UNSET)

        interface_assigned_name = cls(
            device=device,
            ident=ident,
            assigned=assigned,
        )

        interface_assigned_name.additional_properties = d
        return interface_assigned_name

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
