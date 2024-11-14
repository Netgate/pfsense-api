from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.controller_alarms_alarms import ControllerAlarmsAlarms


T = TypeVar("T", bound="ControllerAlarms")


@_attrs_define
class ControllerAlarms:
    """
    Attributes:
        alarms (Union[Unset, ControllerAlarmsAlarms]):
    """

    alarms: Union[Unset, "ControllerAlarmsAlarms"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        alarms: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.alarms, Unset):
            alarms = self.alarms.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alarms is not UNSET:
            field_dict["alarms"] = alarms

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.controller_alarms_alarms import ControllerAlarmsAlarms

        d = src_dict.copy()
        _alarms = d.pop("alarms", UNSET)
        alarms: Union[Unset, ControllerAlarmsAlarms]
        if isinstance(_alarms, Unset):
            alarms = UNSET
        else:
            alarms = ControllerAlarmsAlarms.from_dict(_alarms)

        controller_alarms = cls(
            alarms=alarms,
        )

        controller_alarms.additional_properties = d
        return controller_alarms

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
