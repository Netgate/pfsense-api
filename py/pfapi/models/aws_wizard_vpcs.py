from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aws_wizard_vpc import AwsWizardVpc


T = TypeVar("T", bound="AwsWizardVpcs")


@_attrs_define
class AwsWizardVpcs:
    """
    Attributes:
        vpcs (list[AwsWizardVpc] | Unset):
    """

    vpcs: list[AwsWizardVpc] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vpcs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.vpcs, Unset):
            vpcs = []
            for vpcs_item_data in self.vpcs:
                vpcs_item = vpcs_item_data.to_dict()
                vpcs.append(vpcs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vpcs is not UNSET:
            field_dict["vpcs"] = vpcs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aws_wizard_vpc import AwsWizardVpc

        d = dict(src_dict)
        _vpcs = d.pop("vpcs", UNSET)
        vpcs: list[AwsWizardVpc] | Unset = UNSET
        if _vpcs is not UNSET:
            vpcs = []
            for vpcs_item_data in _vpcs:
                vpcs_item = AwsWizardVpc.from_dict(vpcs_item_data)

                vpcs.append(vpcs_item)

        aws_wizard_vpcs = cls(
            vpcs=vpcs,
        )

        aws_wizard_vpcs.additional_properties = d
        return aws_wizard_vpcs

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
