from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aws_wizard_cred import AwsWizardCred
    from ..models.aws_wizard_vpc import AwsWizardVpc


T = TypeVar("T", bound="AwsWizardSelectVpcReq")


@_attrs_define
class AwsWizardSelectVpcReq:
    """
    Attributes:
        cred (AwsWizardCred | Unset):
        vpc (AwsWizardVpc | Unset):
    """

    cred: AwsWizardCred | Unset = UNSET
    vpc: AwsWizardVpc | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cred: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cred, Unset):
            cred = self.cred.to_dict()

        vpc: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vpc, Unset):
            vpc = self.vpc.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cred is not UNSET:
            field_dict["cred"] = cred
        if vpc is not UNSET:
            field_dict["vpc"] = vpc

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aws_wizard_cred import AwsWizardCred
        from ..models.aws_wizard_vpc import AwsWizardVpc

        d = dict(src_dict)
        _cred = d.pop("cred", UNSET)
        cred: AwsWizardCred | Unset
        if isinstance(_cred, Unset):
            cred = UNSET
        else:
            cred = AwsWizardCred.from_dict(_cred)

        _vpc = d.pop("vpc", UNSET)
        vpc: AwsWizardVpc | Unset
        if isinstance(_vpc, Unset):
            vpc = UNSET
        else:
            vpc = AwsWizardVpc.from_dict(_vpc)

        aws_wizard_select_vpc_req = cls(
            cred=cred,
            vpc=vpc,
        )

        aws_wizard_select_vpc_req.additional_properties = d
        return aws_wizard_select_vpc_req

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
