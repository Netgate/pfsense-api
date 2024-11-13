from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gateway import Gateway
    from ..models.gateway_defaults import GatewayDefaults


T = TypeVar("T", bound="Gateways")


@_attrs_define
class Gateways:
    """
    Attributes:
        defaults (Union[Unset, GatewayDefaults]):
        gateways (Union[Unset, List['Gateway']]):
    """

    defaults: Union[Unset, "GatewayDefaults"] = UNSET
    gateways: Union[Unset, List["Gateway"]] = UNSET
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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if defaults is not UNSET:
            field_dict["defaults"] = defaults
        if gateways is not UNSET:
            field_dict["gateways"] = gateways

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.gateway import Gateway
        from ..models.gateway_defaults import GatewayDefaults

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

        gateways = cls(
            defaults=defaults,
            gateways=gateways,
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
