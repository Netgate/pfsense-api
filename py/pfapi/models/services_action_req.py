from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.services_action_params import ServicesActionParams


T = TypeVar("T", bound="ServicesActionReq")


@_attrs_define
class ServicesActionReq:
    """
    Attributes:
        params (ServicesActionParams | Unset): valid values:
            action = "start", "stop", "restart"
    """

    params: ServicesActionParams | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.services_action_params import ServicesActionParams

        d = dict(src_dict)
        _params = d.pop("params", UNSET)
        params: ServicesActionParams | Unset
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = ServicesActionParams.from_dict(_params)

        services_action_req = cls(
            params=params,
        )

        services_action_req.additional_properties = d
        return services_action_req

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
