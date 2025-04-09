from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IPSecWidgetTunnel")


@_attrs_define
class IPSecWidgetTunnel:
    """
    Attributes:
        source (Union[Unset, str]):
        destination (Union[Unset, str]):
        description (Union[Unset, str]):
        status (Union[Unset, str]):
    """

    source: Union[Unset, str] = UNSET
    destination: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        source = self.source

        destination = self.destination

        description = self.description

        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source is not UNSET:
            field_dict["source"] = source
        if destination is not UNSET:
            field_dict["destination"] = destination
        if description is not UNSET:
            field_dict["description"] = description
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        source = d.pop("source", UNSET)

        destination = d.pop("destination", UNSET)

        description = d.pop("description", UNSET)

        status = d.pop("status", UNSET)

        ip_sec_widget_tunnel = cls(
            source=source,
            destination=destination,
            description=description,
            status=status,
        )

        ip_sec_widget_tunnel.additional_properties = d
        return ip_sec_widget_tunnel

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
