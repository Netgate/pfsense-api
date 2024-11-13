from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ControllerBackupResult")


@_attrs_define
class ControllerBackupResult:
    """
    Attributes:
        time (Union[Unset, int]):
        id (Union[Unset, str]):
        label (Union[Unset, str]):
        description (Union[Unset, str]):
        acb_id (Union[Unset, str]):
        messages (Union[Unset, str]):
    """

    time: Union[Unset, int] = UNSET
    id: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    acb_id: Union[Unset, str] = UNSET
    messages: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        time = self.time

        id = self.id

        label = self.label

        description = self.description

        acb_id = self.acb_id

        messages = self.messages

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if id is not UNSET:
            field_dict["id"] = id
        if label is not UNSET:
            field_dict["label"] = label
        if description is not UNSET:
            field_dict["description"] = description
        if acb_id is not UNSET:
            field_dict["acb_id"] = acb_id
        if messages is not UNSET:
            field_dict["messages"] = messages

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        time = d.pop("time", UNSET)

        id = d.pop("id", UNSET)

        label = d.pop("label", UNSET)

        description = d.pop("description", UNSET)

        acb_id = d.pop("acb_id", UNSET)

        messages = d.pop("messages", UNSET)

        controller_backup_result = cls(
            time=time,
            id=id,
            label=label,
            description=description,
            acb_id=acb_id,
            messages=messages,
        )

        controller_backup_result.additional_properties = d
        return controller_backup_result

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
