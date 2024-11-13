from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.boot_envs_envs import BootEnvsEnvs


T = TypeVar("T", bound="BootEnvs")


@_attrs_define
class BootEnvs:
    """
    Attributes:
        envs (Union[Unset, BootEnvsEnvs]):
    """

    envs: Union[Unset, "BootEnvsEnvs"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        envs: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.envs, Unset):
            envs = self.envs.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if envs is not UNSET:
            field_dict["envs"] = envs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.boot_envs_envs import BootEnvsEnvs

        d = src_dict.copy()
        _envs = d.pop("envs", UNSET)
        envs: Union[Unset, BootEnvsEnvs]
        if isinstance(_envs, Unset):
            envs = UNSET
        else:
            envs = BootEnvsEnvs.from_dict(_envs)

        boot_envs = cls(
            envs=envs,
        )

        boot_envs.additional_properties = d
        return boot_envs

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
