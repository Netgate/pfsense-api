from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.net_if_assign_owner_req_owner_type import NetIfAssignOwnerReqOwnerType
from ..types import UNSET, Unset

T = TypeVar("T", bound="NetIfAssignOwnerReq")


@_attrs_define
class NetIfAssignOwnerReq:
    """owner_id is the identifier of the subsystem taking ownership of the
    interface.

    If the owner_type is set to "host", then it is returned
    to the host.

        Attributes:
            owner_type (NetIfAssignOwnerReqOwnerType | Unset):
            owner_id (str | Unset):
    """

    owner_type: NetIfAssignOwnerReqOwnerType | Unset = UNSET
    owner_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        owner_type: str | Unset = UNSET
        if not isinstance(self.owner_type, Unset):
            owner_type = self.owner_type.value

        owner_id = self.owner_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if owner_type is not UNSET:
            field_dict["owner_type"] = owner_type
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _owner_type = d.pop("owner_type", UNSET)
        owner_type: NetIfAssignOwnerReqOwnerType | Unset
        if isinstance(_owner_type, Unset):
            owner_type = UNSET
        else:
            owner_type = NetIfAssignOwnerReqOwnerType(_owner_type)

        owner_id = d.pop("owner_id", UNSET)

        net_if_assign_owner_req = cls(
            owner_type=owner_type,
            owner_id=owner_id,
        )

        net_if_assign_owner_req.additional_properties = d
        return net_if_assign_owner_req

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
