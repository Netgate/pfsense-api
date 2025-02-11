from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StorageStats")


@_attrs_define
class StorageStats:
    """
    Attributes:
        volume (str): volume name or directory
        device (str): device partition
        capacity (int):
        used (int):
    """

    volume: str
    device: str
    capacity: int
    used: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        volume = self.volume

        device = self.device

        capacity = self.capacity

        used = self.used

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "volume": volume,
                "device": device,
                "capacity": capacity,
                "used": used,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        volume = d.pop("volume")

        device = d.pop("device")

        capacity = d.pop("capacity")

        used = d.pop("used")

        storage_stats = cls(
            volume=volume,
            device=device,
            capacity=capacity,
            used=used,
        )

        storage_stats.additional_properties = d
        return storage_stats

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
