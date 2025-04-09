from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dyn_dns_config import DynDNSConfig


T = TypeVar("T", bound="DynDnsList")


@_attrs_define
class DynDnsList:
    """
    Attributes:
        dyndnses (Union[Unset, List['DynDNSConfig']]):
    """

    dyndnses: Union[Unset, List["DynDNSConfig"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dyndnses: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.dyndnses, Unset):
            dyndnses = []
            for dyndnses_item_data in self.dyndnses:
                dyndnses_item = dyndnses_item_data.to_dict()
                dyndnses.append(dyndnses_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dyndnses is not UNSET:
            field_dict["dyndnses"] = dyndnses

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dyn_dns_config import DynDNSConfig

        d = src_dict.copy()
        dyndnses = []
        _dyndnses = d.pop("dyndnses", UNSET)
        for dyndnses_item_data in _dyndnses or []:
            dyndnses_item = DynDNSConfig.from_dict(dyndnses_item_data)

            dyndnses.append(dyndnses_item)

        dyn_dns_list = cls(
            dyndnses=dyndnses,
        )

        dyn_dns_list.additional_properties = d
        return dyn_dns_list

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
