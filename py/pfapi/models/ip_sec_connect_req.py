from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IPSecConnectReq")


@_attrs_define
class IPSecConnectReq:
    """
    Attributes:
        connect_p1 (bool | Unset):
        p1_ikeid (str | Unset):
        connect_p2 (bool | Unset):
        p2_reqid (str | Unset):
    """

    connect_p1: bool | Unset = UNSET
    p1_ikeid: str | Unset = UNSET
    connect_p2: bool | Unset = UNSET
    p2_reqid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connect_p1 = self.connect_p1

        p1_ikeid = self.p1_ikeid

        connect_p2 = self.connect_p2

        p2_reqid = self.p2_reqid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connect_p1 is not UNSET:
            field_dict["connect_p1"] = connect_p1
        if p1_ikeid is not UNSET:
            field_dict["p1_ikeid"] = p1_ikeid
        if connect_p2 is not UNSET:
            field_dict["connect_p2"] = connect_p2
        if p2_reqid is not UNSET:
            field_dict["p2_reqid"] = p2_reqid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connect_p1 = d.pop("connect_p1", UNSET)

        p1_ikeid = d.pop("p1_ikeid", UNSET)

        connect_p2 = d.pop("connect_p2", UNSET)

        p2_reqid = d.pop("p2_reqid", UNSET)

        ip_sec_connect_req = cls(
            connect_p1=connect_p1,
            p1_ikeid=p1_ikeid,
            connect_p2=connect_p2,
            p2_reqid=p2_reqid,
        )

        ip_sec_connect_req.additional_properties = d
        return ip_sec_connect_req

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
