from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.route_record import RouteRecord


T = TypeVar("T", bound="DiagRoutes")


@_attrs_define
class DiagRoutes:
    """
    Attributes:
        ipv4 (List['RouteRecord']):
        ipv6 (List['RouteRecord']):
    """

    ipv4: List["RouteRecord"]
    ipv6: List["RouteRecord"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ipv4 = []
        for ipv4_item_data in self.ipv4:
            ipv4_item = ipv4_item_data.to_dict()
            ipv4.append(ipv4_item)

        ipv6 = []
        for ipv6_item_data in self.ipv6:
            ipv6_item = ipv6_item_data.to_dict()
            ipv6.append(ipv6_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ipv4": ipv4,
                "ipv6": ipv6,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.route_record import RouteRecord

        d = src_dict.copy()
        ipv4 = []
        _ipv4 = d.pop("ipv4")
        for ipv4_item_data in _ipv4:
            ipv4_item = RouteRecord.from_dict(ipv4_item_data)

            ipv4.append(ipv4_item)

        ipv6 = []
        _ipv6 = d.pop("ipv6")
        for ipv6_item_data in _ipv6:
            ipv6_item = RouteRecord.from_dict(ipv6_item_data)

            ipv6.append(ipv6_item)

        diag_routes = cls(
            ipv4=ipv4,
            ipv6=ipv6,
        )

        diag_routes.additional_properties = d
        return diag_routes

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
