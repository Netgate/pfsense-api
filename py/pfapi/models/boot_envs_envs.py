from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bootenv import Bootenv


T = TypeVar("T", bound="BootEnvsEnvs")


@_attrs_define
class BootEnvsEnvs:
    """ """

    additional_properties: Dict[str, "Bootenv"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bootenv import Bootenv

        d = src_dict.copy()
        boot_envs_envs = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = Bootenv.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        boot_envs_envs.additional_properties = additional_properties
        return boot_envs_envs

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "Bootenv":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "Bootenv") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
