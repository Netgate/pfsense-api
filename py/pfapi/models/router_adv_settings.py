from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.intf_router_adv_setting import IntfRouterAdvSetting


T = TypeVar("T", bound="RouterAdvSettings")


@_attrs_define
class RouterAdvSettings:
    """
    Attributes:
        intf_radvs (Union[Unset, List['IntfRouterAdvSetting']]):
    """

    intf_radvs: Union[Unset, List["IntfRouterAdvSetting"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        intf_radvs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.intf_radvs, Unset):
            intf_radvs = []
            for intf_radvs_item_data in self.intf_radvs:
                intf_radvs_item = intf_radvs_item_data.to_dict()
                intf_radvs.append(intf_radvs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if intf_radvs is not UNSET:
            field_dict["intf_radvs"] = intf_radvs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.intf_router_adv_setting import IntfRouterAdvSetting

        d = src_dict.copy()
        intf_radvs = []
        _intf_radvs = d.pop("intf_radvs", UNSET)
        for intf_radvs_item_data in _intf_radvs or []:
            intf_radvs_item = IntfRouterAdvSetting.from_dict(intf_radvs_item_data)

            intf_radvs.append(intf_radvs_item)

        router_adv_settings = cls(
            intf_radvs=intf_radvs,
        )

        router_adv_settings.additional_properties = d
        return router_adv_settings

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
