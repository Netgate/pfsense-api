from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortInspBinderLUse")


@_attrs_define
class SnortInspBinderLUse:
    """
    Attributes:
        action (str | Unset): what to do with matching traffic { reset | block | allow | inspect }; default inspect
        file (str | Unset): use configuration in given file
        inspection_policy (str | Unset): use inspection policy from given file
        ips_policy (str | Unset): use ips policy from given file
        service (str | Unset): override automatic service identification
        type_ (str | Unset): select module for binding
        name (str | Unset): symbol name (defaults to type)
    """

    action: str | Unset = UNSET
    file: str | Unset = UNSET
    inspection_policy: str | Unset = UNSET
    ips_policy: str | Unset = UNSET
    service: str | Unset = UNSET
    type_: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        file = self.file

        inspection_policy = self.inspection_policy

        ips_policy = self.ips_policy

        service = self.service

        type_ = self.type_

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if file is not UNSET:
            field_dict["file"] = file
        if inspection_policy is not UNSET:
            field_dict["inspection_policy"] = inspection_policy
        if ips_policy is not UNSET:
            field_dict["ips_policy"] = ips_policy
        if service is not UNSET:
            field_dict["service"] = service
        if type_ is not UNSET:
            field_dict["type"] = type_
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = d.pop("action", UNSET)

        file = d.pop("file", UNSET)

        inspection_policy = d.pop("inspection_policy", UNSET)

        ips_policy = d.pop("ips_policy", UNSET)

        service = d.pop("service", UNSET)

        type_ = d.pop("type", UNSET)

        name = d.pop("name", UNSET)

        snort_insp_binder_l_use = cls(
            action=action,
            file=file,
            inspection_policy=inspection_policy,
            ips_policy=ips_policy,
            service=service,
            type_=type_,
            name=name,
        )

        snort_insp_binder_l_use.additional_properties = d
        return snort_insp_binder_l_use

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
