from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StdLog")


@_attrs_define
class StdLog:
    """
    Attributes:
        time (Union[Unset, str]):
        proc (Union[Unset, str]):
        pid (Union[Unset, str]):
        msg (Union[Unset, str]):
    """

    time: Union[Unset, str] = UNSET
    proc: Union[Unset, str] = UNSET
    pid: Union[Unset, str] = UNSET
    msg: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        time = self.time

        proc = self.proc

        pid = self.pid

        msg = self.msg

        field_dict: Dict[str, Any] = {}
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
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
