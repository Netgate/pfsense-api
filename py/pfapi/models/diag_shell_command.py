from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DiagShellCommand")


@_attrs_define
class DiagShellCommand:
    """
    Attributes:
        cmd (Union[Unset, str]):
        timeout (Union[Unset, int]): number of seconds to wait for command before timing out, default 90, max 300
    """

    cmd: Union[Unset, str] = UNSET
    timeout: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cmd = self.cmd

        timeout = self.timeout

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cmd is not UNSET:
            field_dict["cmd"] = cmd
        if timeout is not UNSET:
            field_dict["timeout"] = timeout

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cmd = d.pop("cmd", UNSET)

        timeout = d.pop("timeout", UNSET)

        diag_shell_command = cls(
            cmd=cmd,
            timeout=timeout,
        )

        diag_shell_command.additional_properties = d
        return diag_shell_command

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
