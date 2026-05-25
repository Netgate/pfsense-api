from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.frr_global_acl import FrrGlobalAcl


T = TypeVar("T", bound="FrrGlobalAclsList")


@_attrs_define
class FrrGlobalAclsList:
    """
    Attributes:
        globalacls (list[FrrGlobalAcl] | Unset):
    """

    globalacls: list[FrrGlobalAcl] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        globalacls: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.globalacls, Unset):
            globalacls = []
            for globalacls_item_data in self.globalacls:
                globalacls_item = globalacls_item_data.to_dict()
                globalacls.append(globalacls_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if globalacls is not UNSET:
            field_dict["globalacls"] = globalacls

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.frr_global_acl import FrrGlobalAcl

        d = dict(src_dict)
        _globalacls = d.pop("globalacls", UNSET)
        globalacls: list[FrrGlobalAcl] | Unset = UNSET
        if _globalacls is not UNSET:
            globalacls = []
            for globalacls_item_data in _globalacls:
                globalacls_item = FrrGlobalAcl.from_dict(globalacls_item_data)

                globalacls.append(globalacls_item)

        frr_global_acls_list = cls(
            globalacls=globalacls,
        )

        frr_global_acls_list.additional_properties = d
        return frr_global_acls_list

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
