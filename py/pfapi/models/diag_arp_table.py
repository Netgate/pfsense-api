from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.arp_table_entry import ArpTableEntry


T = TypeVar("T", bound="DiagArpTable")


@_attrs_define
class DiagArpTable:
    """
    Attributes:
        arp (Union[Unset, List['ArpTableEntry']]):
    """

    arp: Union[Unset, List["ArpTableEntry"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        arp: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.arp, Unset):
            arp = []
            for arp_item_data in self.arp:
                arp_item = arp_item_data.to_dict()
                arp.append(arp_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if arp is not UNSET:
            field_dict["arp"] = arp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.arp_table_entry import ArpTableEntry

        d = src_dict.copy()
        arp = []
        _arp = d.pop("arp", UNSET)
        for arp_item_data in _arp or []:
            arp_item = ArpTableEntry.from_dict(arp_item_data)

            arp.append(arp_item)

        diag_arp_table = cls(
            arp=arp,
        )

        diag_arp_table.additional_properties = d
        return diag_arp_table

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
