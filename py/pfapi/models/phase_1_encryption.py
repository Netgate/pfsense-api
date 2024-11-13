from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.phase_1_alg import Phase1Alg


T = TypeVar("T", bound="Phase1Encryption")


@_attrs_define
class Phase1Encryption:
    """
    Attributes:
        item (Union[Unset, List['Phase1Alg']]):
    """

    item: Union[Unset, List["Phase1Alg"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        item: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.item, Unset):
            item = []
            for item_item_data in self.item:
                item_item = item_item_data.to_dict()
                item.append(item_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if item is not UNSET:
            field_dict["item"] = item

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.phase_1_alg import Phase1Alg

        d = src_dict.copy()
        item = []
        _item = d.pop("item", UNSET)
        for item_item_data in _item or []:
            item_item = Phase1Alg.from_dict(item_item_data)

            item.append(item_item)

        phase_1_encryption = cls(
            item=item,
        )

        phase_1_encryption.additional_properties = d
        return phase_1_encryption

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
