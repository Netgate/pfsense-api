from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.acme_private_key_req_key_type import ACMEPrivateKeyReqKeyType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ACMEPrivateKeyReq")


@_attrs_define
class ACMEPrivateKeyReq:
    """
    Attributes:
        key_type (ACMEPrivateKeyReqKeyType | Unset): type of the cert's private key
            valid value = rsa2048, rsa3072, rsa4096, rsa8192, ec256, ec384
    """

    key_type: ACMEPrivateKeyReqKeyType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key_type: str | Unset = UNSET
        if not isinstance(self.key_type, Unset):
            key_type = self.key_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key_type is not UNSET:
            field_dict["key_type"] = key_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _key_type = d.pop("key_type", UNSET)
        key_type: ACMEPrivateKeyReqKeyType | Unset
        if isinstance(_key_type, Unset):
            key_type = UNSET
        else:
            key_type = ACMEPrivateKeyReqKeyType(_key_type)

        acme_private_key_req = cls(
            key_type=key_type,
        )

        acme_private_key_req.additional_properties = d
        return acme_private_key_req

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
