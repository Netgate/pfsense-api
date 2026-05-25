from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AwsWizardVPGateway")


@_attrs_define
class AwsWizardVPGateway:
    """
    Attributes:
        vp_gw_id (str | Unset):
    """

    vp_gw_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vp_gw_id = self.vp_gw_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vp_gw_id is not UNSET:
            field_dict["vp_gw_id"] = vp_gw_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        vp_gw_id = d.pop("vp_gw_id", UNSET)

        aws_wizard_vp_gateway = cls(
            vp_gw_id=vp_gw_id,
        )

        aws_wizard_vp_gateway.additional_properties = d
        return aws_wizard_vp_gateway

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
