from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortInspTelnet")


@_attrs_define
class SnortInspTelnet:
    """
    Attributes:
        ayt_attack_thresh (int | Unset): alert beyond this number of consecutive Telnet AYT commands (-1 is disabled) {
            -1:max31 }; default -1
        check_encrypted (bool | Unset): check for end of encryption; default false
        encrypted_traffic (bool | Unset): check for encrypted Telnet; default false
        normalize (bool | Unset): eliminate escape sequences; default false
    """

    ayt_attack_thresh: int | Unset = UNSET
    check_encrypted: bool | Unset = UNSET
    encrypted_traffic: bool | Unset = UNSET
    normalize: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ayt_attack_thresh = self.ayt_attack_thresh

        check_encrypted = self.check_encrypted

        encrypted_traffic = self.encrypted_traffic

        normalize = self.normalize

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ayt_attack_thresh is not UNSET:
            field_dict["ayt_attack_thresh"] = ayt_attack_thresh
        if check_encrypted is not UNSET:
            field_dict["check_encrypted"] = check_encrypted
        if encrypted_traffic is not UNSET:
            field_dict["encrypted_traffic"] = encrypted_traffic
        if normalize is not UNSET:
            field_dict["normalize"] = normalize

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ayt_attack_thresh = d.pop("ayt_attack_thresh", UNSET)

        check_encrypted = d.pop("check_encrypted", UNSET)

        encrypted_traffic = d.pop("encrypted_traffic", UNSET)

        normalize = d.pop("normalize", UNSET)

        snort_insp_telnet = cls(
            ayt_attack_thresh=ayt_attack_thresh,
            check_encrypted=check_encrypted,
            encrypted_traffic=encrypted_traffic,
            normalize=normalize,
        )

        snort_insp_telnet.additional_properties = d
        return snort_insp_telnet

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
