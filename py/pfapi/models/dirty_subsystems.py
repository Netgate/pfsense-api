from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dirty_subsystems_all_subsystems import DirtySubsystemsAllSubsystems
    from ..models.dirty_subsystems_dirty_subsystems import DirtySubsystemsDirtySubsystems


T = TypeVar("T", bound="DirtySubsystems")


@_attrs_define
class DirtySubsystems:
    """
    Attributes:
        dirty_subsystems (DirtySubsystemsDirtySubsystems):
        all_subsystems (DirtySubsystemsAllSubsystems):
    """

    dirty_subsystems: "DirtySubsystemsDirtySubsystems"
    all_subsystems: "DirtySubsystemsAllSubsystems"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dirty_subsystems = self.dirty_subsystems.to_dict()

        all_subsystems = self.all_subsystems.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dirty_subsystems": dirty_subsystems,
                "all_subsystems": all_subsystems,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dirty_subsystems_all_subsystems import DirtySubsystemsAllSubsystems
        from ..models.dirty_subsystems_dirty_subsystems import DirtySubsystemsDirtySubsystems

        d = src_dict.copy()
        dirty_subsystems = DirtySubsystemsDirtySubsystems.from_dict(d.pop("dirty_subsystems"))

        all_subsystems = DirtySubsystemsAllSubsystems.from_dict(d.pop("all_subsystems"))

        dirty_subsystems = cls(
            dirty_subsystems=dirty_subsystems,
            all_subsystems=all_subsystems,
        )

        dirty_subsystems.additional_properties = d
        return dirty_subsystems

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
