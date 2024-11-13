from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wg_peer import WGPeer


T = TypeVar("T", bound="WGPeers")


@_attrs_define
class WGPeers:
    """
    Attributes:
        item (Union[Unset, List['WGPeer']]):
    """

    item: Union[Unset, List["WGPeer"]] = UNSET
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
        from ..models.wg_peer import WGPeer

        d = src_dict.copy()
        item = []
        _item = d.pop("item", UNSET)
        for item_item_data in _item or []:
            item_item = WGPeer.from_dict(item_item_data)

            item.append(item_item)

        wg_peers = cls(
            item=item,
        )

        wg_peers.additional_properties = d
        return wg_peers

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
