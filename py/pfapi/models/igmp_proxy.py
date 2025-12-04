from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IGMPProxy")


@_attrs_define
class IGMPProxy:
    """
    Attributes:
        ifname (str):
        address (list[str]):
        threshold (int | Unset):
        descr (str | Unset):
        type_ (str | Unset):
        id (str | Unset): record ID, read-only
    """

    ifname: str
    address: list[str]
    threshold: int | Unset = UNSET
    descr: str | Unset = UNSET
    type_: str | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ifname = self.ifname

        address = self.address

        threshold = self.threshold

        descr = self.descr

        type_ = self.type_

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ifname": ifname,
                "address": address,
            }
        )
        if threshold is not UNSET:
            field_dict["threshold"] = threshold
        if descr is not UNSET:
            field_dict["descr"] = descr
        if type_ is not UNSET:
            field_dict["type"] = type_
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ifname = d.pop("ifname")

        address = cast(list[str], d.pop("address"))

        threshold = d.pop("threshold", UNSET)

        descr = d.pop("descr", UNSET)

        type_ = d.pop("type", UNSET)

        id = d.pop("id", UNSET)

        igmp_proxy = cls(
            ifname=ifname,
            address=address,
            threshold=threshold,
            descr=descr,
            type_=type_,
            id=id,
        )

        igmp_proxy.additional_properties = d
        return igmp_proxy

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
