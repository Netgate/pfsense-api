from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.captive_portal_name import CaptivePortalName


T = TypeVar("T", bound="CaptivePortals")


@_attrs_define
class CaptivePortals:
    """
    Attributes:
        config (Union[Unset, List['CaptivePortalName']]):
    """

    config: Union[Unset, List["CaptivePortalName"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        config: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.config, Unset):
            config = []
            for config_item_data in self.config:
                config_item = config_item_data.to_dict()
                config.append(config_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.captive_portal_name import CaptivePortalName

        d = src_dict.copy()
        config = []
        _config = d.pop("config", UNSET)
        for config_item_data in _config or []:
            config_item = CaptivePortalName.from_dict(config_item_data)

            config.append(config_item)

        captive_portals = cls(
            config=config,
        )

        captive_portals.additional_properties = d
        return captive_portals

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
