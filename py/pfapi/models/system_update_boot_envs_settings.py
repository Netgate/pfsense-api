from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SystemUpdateBootEnvsSettings")


@_attrs_define
class SystemUpdateBootEnvsSettings:
    """
    Attributes:
        deferred_boot (Union[Unset, bool]):
        verify (Union[Unset, bool]):
        verify_timeout (Union[Unset, int]):
    """

    deferred_boot: Union[Unset, bool] = UNSET
    verify: Union[Unset, bool] = UNSET
    verify_timeout: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        deferred_boot = self.deferred_boot

        verify = self.verify

        verify_timeout = self.verify_timeout

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deferred_boot is not UNSET:
            field_dict["deferred_boot"] = deferred_boot
        if verify is not UNSET:
            field_dict["verify"] = verify
        if verify_timeout is not UNSET:
            field_dict["verify_timeout"] = verify_timeout

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        deferred_boot = d.pop("deferred_boot", UNSET)

        verify = d.pop("verify", UNSET)

        verify_timeout = d.pop("verify_timeout", UNSET)

        system_update_boot_envs_settings = cls(
            deferred_boot=deferred_boot,
            verify=verify,
            verify_timeout=verify_timeout,
        )

        system_update_boot_envs_settings.additional_properties = d
        return system_update_boot_envs_settings

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
