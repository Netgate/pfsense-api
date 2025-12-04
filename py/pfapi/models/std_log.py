from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StdLog")


@_attrs_define
class StdLog:
    """
    Attributes:
        time (str | Unset):
        proc (str | Unset):
        pid (str | Unset):
        msg (str | Unset):
    """

    time: str | Unset = UNSET
    proc: str | Unset = UNSET
    pid: str | Unset = UNSET
    msg: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time

        proc = self.proc

        pid = self.pid

        msg = self.msg

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if proc is not UNSET:
            field_dict["proc"] = proc
        if pid is not UNSET:
            field_dict["pid"] = pid
        if msg is not UNSET:
            field_dict["msg"] = msg

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        time = d.pop("time", UNSET)

        proc = d.pop("proc", UNSET)

        pid = d.pop("pid", UNSET)

        msg = d.pop("msg", UNSET)

        std_log = cls(
            time=time,
            proc=proc,
            pid=pid,
            msg=msg,
        )

        std_log.additional_properties = d
        return std_log

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
