from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wgip_address import WGIPAddress


T = TypeVar("T", bound="WGIPAddresses")


@_attrs_define
class WGIPAddresses:
    """
    Attributes:
        row (Union[Unset, List['WGIPAddress']]):
    """

    row: Union[Unset, List["WGIPAddress"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        row: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.row, Unset):
            row = []
            for row_item_data in self.row:
                row_item = row_item_data.to_dict()
                row.append(row_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if row is not UNSET:
            field_dict["row"] = row

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.wgip_address import WGIPAddress

        d = src_dict.copy()
        row = []
        _row = d.pop("row", UNSET)
        for row_item_data in _row or []:
            row_item = WGIPAddress.from_dict(row_item_data)

            row.append(row_item)

        wgip_addresses = cls(
            row=row,
        )

        wgip_addresses.additional_properties = d
        return wgip_addresses

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
