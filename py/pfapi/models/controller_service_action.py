from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.controller_service_action_action import ControllerServiceActionAction
from ..types import UNSET, Unset

T = TypeVar("T", bound="ControllerServiceAction")


@_attrs_define
class ControllerServiceAction:
    """
    Attributes:
        action (Union[Unset, ControllerServiceActionAction]): Action to carry out [restart, reload, stop]
    """

    action: Union[Unset, ControllerServiceActionAction] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        action: Union[Unset, str] = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _action = d.pop("action", UNSET)
        action: Union[Unset, ControllerServiceActionAction]
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = ControllerServiceActionAction(_action)

        controller_service_action = cls(
            action=action,
        )

        controller_service_action.additional_properties = d
        return controller_service_action

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
