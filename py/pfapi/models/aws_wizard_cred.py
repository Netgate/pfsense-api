from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.aws_wizard_cred_partition import AwsWizardCredPartition
from ..types import UNSET, Unset

T = TypeVar("T", bound="AwsWizardCred")


@_attrs_define
class AwsWizardCred:
    """
    Attributes:
        awskey (str | Unset): access key id
        secret (str | Unset): aws secret key
        awsrole (str | Unset): use ec2 instance profile to assume role instead of keys
        partition (AwsWizardCredPartition | Unset): the aws partition the vpc resides in
        region (str | Unset): aws region for the operation, set it to empty string when list regions
    """

    awskey: str | Unset = UNSET
    secret: str | Unset = UNSET
    awsrole: str | Unset = UNSET
    partition: AwsWizardCredPartition | Unset = UNSET
    region: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        awskey = self.awskey

        secret = self.secret

        awsrole = self.awsrole

        partition: str | Unset = UNSET
        if not isinstance(self.partition, Unset):
            partition = self.partition.value

        region = self.region

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if awskey is not UNSET:
            field_dict["awskey"] = awskey
        if secret is not UNSET:
            field_dict["secret"] = secret
        if awsrole is not UNSET:
            field_dict["awsrole"] = awsrole
        if partition is not UNSET:
            field_dict["partition"] = partition
        if region is not UNSET:
            field_dict["region"] = region

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        awskey = d.pop("awskey", UNSET)

        secret = d.pop("secret", UNSET)

        awsrole = d.pop("awsrole", UNSET)

        _partition = d.pop("partition", UNSET)
        partition: AwsWizardCredPartition | Unset
        if isinstance(_partition, Unset):
            partition = UNSET
        else:
            partition = AwsWizardCredPartition(_partition)

        region = d.pop("region", UNSET)

        aws_wizard_cred = cls(
            awskey=awskey,
            secret=secret,
            awsrole=awsrole,
            partition=partition,
            region=region,
        )

        aws_wizard_cred.additional_properties = d
        return aws_wizard_cred

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
