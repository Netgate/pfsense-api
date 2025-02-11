from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IPSecWidgetTunnel")


@_attrs_define
class IPSecWidgetTunnel:
    """
    Attributes:
        source (str):
        destination (str):
        description (str):
        status (str):
    """

    source: str
    destination: str
    description: str
    status: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        source = self.source

        destination = self.destination

        description = self.description

        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source": source,
                "destination": destination,
                "description": description,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        source = d.pop("source")

        destination = d.pop("destination")

        description = d.pop("description")

        status = d.pop("status")

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
