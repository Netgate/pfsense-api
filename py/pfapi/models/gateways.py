from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gateway import Gateway
    from ..models.gateway_defaults import GatewayDefaults
    from ..models.text_value import TextValue


T = TypeVar("T", bound="Gateways")


@_attrs_define
class Gateways:
    """
    Attributes:
        defaults (Union[Unset, GatewayDefaults]):
        gateways (Union[Unset, List['Gateway']]):
        default_assignable_gw4 (Union[Unset, List['TextValue']]):
        default_assignable_gw6 (Union[Unset, List['TextValue']]):
    """

    defaults: Union[Unset, "GatewayDefaults"] = UNSET
    gateways: Union[Unset, List["Gateway"]] = UNSET
    default_assignable_gw4: Union[Unset, List["TextValue"]] = UNSET
    default_assignable_gw6: Union[Unset, List["TextValue"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        defaults: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.defaults, Unset):
            defaults = self.defaults.to_dict()

        gateways: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.gateways, Unset):
            gateways = []
            for gateways_item_data in self.gateways:
                gateways_item = gateways_item_data.to_dict()
                gateways.append(gateways_item)

        default_assignable_gw4: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.default_assignable_gw4, Unset):
            default_assignable_gw4 = []
            for default_assignable_gw4_item_data in self.default_assignable_gw4:
                default_assignable_gw4_item = default_assignable_gw4_item_data.to_dict()
                default_assignable_gw4.append(default_assignable_gw4_item)

        default_assignable_gw6: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.default_assignable_gw6, Unset):
            default_assignable_gw6 = []
            for default_assignable_gw6_item_data in self.default_assignable_gw6:
                default_assignable_gw6_item = default_assignable_gw6_item_data.to_dict()
                default_assignable_gw6.append(default_assignable_gw6_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if defaults is not UNSET:
            field_dict["defaults"] = defaults
        if gateways is not UNSET:
            field_dict["gateways"] = gateways
        if default_assignable_gw4 is not UNSET:
            field_dict["default_assignable_gw4"] = default_assignable_gw4
        if default_assignable_gw6 is not UNSET:
            field_dict["default_assignable_gw6"] = default_assignable_gw6

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.gateway import Gateway
        from ..models.gateway_defaults import GatewayDefaults
        from ..models.text_value import TextValue

        d = src_dict.copy()
        _defaults = d.pop("defaults", UNSET)
        defaults: Union[Unset, GatewayDefaults]
        if isinstance(_defaults, Unset):
            defaults = UNSET
        else:
            defaults = GatewayDefaults.from_dict(_defaults)

        gateways = []
        _gateways = d.pop("gateways", UNSET)
        for gateways_item_data in _gateways or []:
            gateways_item = Gateway.from_dict(gateways_item_data)

            gateways.append(gateways_item)

        default_assignable_gw4 = []
        _default_assignable_gw4 = d.pop("default_assignable_gw4", UNSET)
        for default_assignable_gw4_item_data in _default_assignable_gw4 or []:
            default_assignable_gw4_item = TextValue.from_dict(default_assignable_gw4_item_data)

            default_assignable_gw4.append(default_assignable_gw4_item)

        default_assignable_gw6 = []
        _default_assignable_gw6 = d.pop("default_assignable_gw6", UNSET)
        for default_assignable_gw6_item_data in _default_assignable_gw6 or []:
            default_assignable_gw6_item = TextValue.from_dict(default_assignable_gw6_item_data)

            default_assignable_gw6.append(default_assignable_gw6_item)

        gateways = cls(
            defaults=defaults,
            gateways=gateways,
            default_assignable_gw4=default_assignable_gw4,
            default_assignable_gw6=default_assignable_gw6,
        )

        gateways.additional_properties = d
        return gateways

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
