from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dirty_subsystem import DirtySubsystem


T = TypeVar("T", bound="ConfigEvent")


@_attrs_define
class ConfigEvent:
    """This event is sent when configuration changes have occurred, with an indicator
    of whether there are dirty subsystems flagged, or if the system requires a reboot

        Attributes:
            dirty_subsystems (Union[Unset, List['DirtySubsystem']]):
            reboot_required (Union[Unset, bool]): system requires a reboot or not
            change_message (Union[Unset, str]): a message about what changed in the configuration
    """

    dirty_subsystems: Union[Unset, List["DirtySubsystem"]] = UNSET
    reboot_required: Union[Unset, bool] = UNSET
    change_message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dirty_subsystems: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.dirty_subsystems, Unset):
            dirty_subsystems = []
            for dirty_subsystems_item_data in self.dirty_subsystems:
                dirty_subsystems_item = dirty_subsystems_item_data.to_dict()
                dirty_subsystems.append(dirty_subsystems_item)

        reboot_required = self.reboot_required

        change_message = self.change_message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dirty_subsystems is not UNSET:
            field_dict["dirty_subsystems"] = dirty_subsystems
        if reboot_required is not UNSET:
            field_dict["reboot_required"] = reboot_required
        if change_message is not UNSET:
            field_dict["change_message"] = change_message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dirty_subsystem import DirtySubsystem

        d = src_dict.copy()
        dirty_subsystems = []
        _dirty_subsystems = d.pop("dirty_subsystems", UNSET)
        for dirty_subsystems_item_data in _dirty_subsystems or []:
            dirty_subsystems_item = DirtySubsystem.from_dict(dirty_subsystems_item_data)

            dirty_subsystems.append(dirty_subsystems_item)

        reboot_required = d.pop("reboot_required", UNSET)

        change_message = d.pop("change_message", UNSET)

        config_event = cls(
            dirty_subsystems=dirty_subsystems,
            reboot_required=reboot_required,
            change_message=change_message,
        )

        config_event.additional_properties = d
        return config_event

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
