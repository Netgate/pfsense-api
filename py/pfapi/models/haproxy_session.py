from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HaproxySession")


@_attrs_define
class HaproxySession:
    """
    Attributes:
        sessid (str | Unset): Session ID
        src (str | Unset): Raw source ip:port
        srcip (str | Unset): Source IP
        srcport (str | Unset): Source port
        be (str | Unset): Backend name
        srv (str | Unset): Server name
        age (str | Unset): Session age
        calls (str | Unset): Number of calls
        exp (str | Unset): Expiration
    """

    sessid: str | Unset = UNSET
    src: str | Unset = UNSET
    srcip: str | Unset = UNSET
    srcport: str | Unset = UNSET
    be: str | Unset = UNSET
    srv: str | Unset = UNSET
    age: str | Unset = UNSET
    calls: str | Unset = UNSET
    exp: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sessid = self.sessid

        src = self.src

        srcip = self.srcip

        srcport = self.srcport

        be = self.be

        srv = self.srv

        age = self.age

        calls = self.calls

        exp = self.exp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sessid is not UNSET:
            field_dict["sessid"] = sessid
        if src is not UNSET:
            field_dict["src"] = src
        if srcip is not UNSET:
            field_dict["srcip"] = srcip
        if srcport is not UNSET:
            field_dict["srcport"] = srcport
        if be is not UNSET:
            field_dict["be"] = be
        if srv is not UNSET:
            field_dict["srv"] = srv
        if age is not UNSET:
            field_dict["age"] = age
        if calls is not UNSET:
            field_dict["calls"] = calls
        if exp is not UNSET:
            field_dict["exp"] = exp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sessid = d.pop("sessid", UNSET)

        src = d.pop("src", UNSET)

        srcip = d.pop("srcip", UNSET)

        srcport = d.pop("srcport", UNSET)

        be = d.pop("be", UNSET)

        srv = d.pop("srv", UNSET)

        age = d.pop("age", UNSET)

        calls = d.pop("calls", UNSET)

        exp = d.pop("exp", UNSET)

        haproxy_session = cls(
            sessid=sessid,
            src=src,
            srcip=srcip,
            srcport=srcport,
            be=be,
            srv=srv,
            age=age,
            calls=calls,
            exp=exp,
        )

        haproxy_session.additional_properties = d
        return haproxy_session

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
