from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ndp_entry import NDPEntry


T = TypeVar("T", bound="NDPTable")


@_attrs_define
class NDPTable:
    """
    Attributes:
        ndptable (Union[Unset, List['NDPEntry']]):
    """

    ndptable: Union[Unset, List["NDPEntry"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ndptable: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ndptable, Unset):
            ndptable = []
            for ndptable_item_data in self.ndptable:
                ndptable_item = ndptable_item_data.to_dict()
                ndptable.append(ndptable_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ndptable is not UNSET:
            field_dict["ndptable"] = ndptable

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ndp_entry import NDPEntry

        d = src_dict.copy()
        ndptable = []
        _ndptable = d.pop("ndptable", UNSET)
        for ndptable_item_data in _ndptable or []:
            ndptable_item = NDPEntry.from_dict(ndptable_item_data)

            ndptable.append(ndptable_item)

        ndp_table = cls(
            ndptable=ndptable,
        )

        ndp_table.additional_properties = d
        return ndp_table

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
