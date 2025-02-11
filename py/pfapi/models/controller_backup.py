from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ControllerBackup")


@_attrs_define
class ControllerBackup:
    """
    Attributes:
        time (int):
        id (str):
        label (str):
        description (str):
        acb_id (Union[Unset, str]):
    """

    time: int
    id: str
    label: str
    description: str
    acb_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        time = self.time

        id = self.id

        label = self.label

        description = self.description

        acb_id = self.acb_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "time": time,
                "id": id,
                "label": label,
                "description": description,
            }
        )
        if acb_id is not UNSET:
            field_dict["acb_id"] = acb_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        time = d.pop("time")

        id = d.pop("id")

        label = d.pop("label")

        description = d.pop("description")

        acb_id = d.pop("acb_id", UNSET)

        controller_backup = cls(
            time=time,
            id=id,
            label=label,
            description=description,
            acb_id=acb_id,
        )

        controller_backup.additional_properties = d
        return controller_backup

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
