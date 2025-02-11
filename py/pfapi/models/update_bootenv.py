from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateBootenv")


@_attrs_define
class UpdateBootenv:
    """
    Attributes:
        old_name (str):
        name (str):
        descr (str):
        protect (bool):
    """

    old_name: str
    name: str
    descr: str
    protect: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        old_name = self.old_name

        name = self.name

        descr = self.descr

        protect = self.protect

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "old_name": old_name,
                "name": name,
                "descr": descr,
                "protect": protect,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        old_name = d.pop("old_name")

        name = d.pop("name")

        descr = d.pop("descr")

        protect = d.pop("protect")

        update_bootenv = cls(
            old_name=old_name,
            name=name,
            descr=descr,
            protect=protect,
        )

        update_bootenv.additional_properties = d
        return update_bootenv

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
