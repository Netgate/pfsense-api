from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.fw_alias_req_type import FWAliasReqType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fw_target import FWTarget


T = TypeVar("T", bound="FWAliasReq")


@_attrs_define
class FWAliasReq:
    """
    Attributes:
        name (str):
        address (str | Unset): space separated list of addresses
        targets (list[FWTarget] | Unset):
        descr (str | Unset):
        type_ (FWAliasReqType | Unset): host, network, url, urltable, urltable_ports, port, or url_ports
        detail (str | Unset):
        updatefreq (str | Unset):
        truncated (bool | Unset):
    """

    name: str
    address: str | Unset = UNSET
    targets: list[FWTarget] | Unset = UNSET
    descr: str | Unset = UNSET
    type_: FWAliasReqType | Unset = UNSET
    detail: str | Unset = UNSET
    updatefreq: str | Unset = UNSET
    truncated: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        address = self.address

        targets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.targets, Unset):
            targets = []
            for targets_item_data in self.targets:
                targets_item = targets_item_data.to_dict()
                targets.append(targets_item)

        descr = self.descr

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        detail = self.detail

        updatefreq = self.updatefreq

        truncated = self.truncated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address
        if targets is not UNSET:
            field_dict["targets"] = targets
        if descr is not UNSET:
            field_dict["descr"] = descr
        if type_ is not UNSET:
            field_dict["type"] = type_
        if detail is not UNSET:
            field_dict["detail"] = detail
        if updatefreq is not UNSET:
            field_dict["updatefreq"] = updatefreq
        if truncated is not UNSET:
            field_dict["truncated"] = truncated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fw_target import FWTarget

        d = dict(src_dict)
        name = d.pop("name")

        address = d.pop("address", UNSET)

        _targets = d.pop("targets", UNSET)
        targets: list[FWTarget] | Unset = UNSET
        if _targets is not UNSET:
            targets = []
            for targets_item_data in _targets:
                targets_item = FWTarget.from_dict(targets_item_data)

                targets.append(targets_item)

        descr = d.pop("descr", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: FWAliasReqType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = FWAliasReqType(_type_)

        detail = d.pop("detail", UNSET)

        updatefreq = d.pop("updatefreq", UNSET)

        truncated = d.pop("truncated", UNSET)

        fw_alias_req = cls(
            name=name,
            address=address,
            targets=targets,
            descr=descr,
            type_=type_,
            detail=detail,
            updatefreq=updatefreq,
            truncated=truncated,
        )

        fw_alias_req.additional_properties = d
        return fw_alias_req

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
