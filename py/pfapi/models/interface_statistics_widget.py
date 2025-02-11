from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="InterfaceStatisticsWidget")


@_attrs_define
class InterfaceStatisticsWidget:
    """
    Attributes:
        packets_in (int):
        packets_out (int):
        bytes_in (int):
        bytes_out (int):
        errors_in (int):
        errors_out (int):
        collisions (int):
    """

    packets_in: int
    packets_out: int
    bytes_in: int
    bytes_out: int
    errors_in: int
    errors_out: int
    collisions: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        packets_in = self.packets_in

        packets_out = self.packets_out

        bytes_in = self.bytes_in

        bytes_out = self.bytes_out

        errors_in = self.errors_in

        errors_out = self.errors_out

        collisions = self.collisions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "packets_in": packets_in,
                "packets_out": packets_out,
                "bytes_in": bytes_in,
                "bytes_out": bytes_out,
                "errors_in": errors_in,
                "errors_out": errors_out,
                "collisions": collisions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        packets_in = d.pop("packets_in")

        packets_out = d.pop("packets_out")

        bytes_in = d.pop("bytes_in")

        bytes_out = d.pop("bytes_out")

        errors_in = d.pop("errors_in")

        errors_out = d.pop("errors_out")

        collisions = d.pop("collisions")

        interface_statistics_widget = cls(
            packets_in=packets_in,
            packets_out=packets_out,
            bytes_in=bytes_in,
            bytes_out=bytes_out,
            errors_in=errors_in,
            errors_out=errors_out,
            collisions=collisions,
        )

        interface_statistics_widget.additional_properties = d
        return interface_statistics_widget

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
