from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortInspDceSmb")


@_attrs_define
class SnortInspDceSmb:
    """
    Attributes:
        limit_alerts (bool | Unset): limit DCE alert to at most one per signature per flow; default true
        disable_defrag (bool | Unset): disable DCE/RPC defragmentation; default false
        max_frag_len (int | Unset): maximum fragment size for defragmentation { 1514:65535 }; default 65535
        reassemble_threshold (int | Unset): minimum bytes received before performing reassembly { 0:65535 }; default 0
        smb_fingerprint_policy (str | Unset): target based SMB policy to use { none | client | server | both }; default
            none
        policy (str | Unset): target based policy to use { Win2000 | WinXP | WinVista | Win2003 | Win2008 | Win7 | Samba
            | Samba-3.0.37 | Samba-3.0.22 | Samba-3.0.20 }; default WinXP
        smb_max_chain (int | Unset): SMB max chain size { 0:255 }; default 3
        smb_max_compound (int | Unset): SMB max compound size { 0:255 }; default 3
        valid_smb_versions (list[str] | Unset):
        smb_file_depth (int | Unset): SMB file depth for file data (-1 = disabled, 0 = unlimited) { -1:32767 }; default
            16384
        smb_invalid_shares (str | Unset): SMB shares to alert on
        smb_legacy_mode (bool | Unset): inspect only SMBv1; default false
        smb_max_credit (int | Unset): Maximum number of outstanding request { 1:65535 }; default 8192
        memcap (int | Unset): Memory utilization limit on SMBv2 cache { 512:maxSZ }; default 8388608
    """

    limit_alerts: bool | Unset = UNSET
    disable_defrag: bool | Unset = UNSET
    max_frag_len: int | Unset = UNSET
    reassemble_threshold: int | Unset = UNSET
    smb_fingerprint_policy: str | Unset = UNSET
    policy: str | Unset = UNSET
    smb_max_chain: int | Unset = UNSET
    smb_max_compound: int | Unset = UNSET
    valid_smb_versions: list[str] | Unset = UNSET
    smb_file_depth: int | Unset = UNSET
    smb_invalid_shares: str | Unset = UNSET
    smb_legacy_mode: bool | Unset = UNSET
    smb_max_credit: int | Unset = UNSET
    memcap: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        limit_alerts = self.limit_alerts

        disable_defrag = self.disable_defrag

        max_frag_len = self.max_frag_len

        reassemble_threshold = self.reassemble_threshold

        smb_fingerprint_policy = self.smb_fingerprint_policy

        policy = self.policy

        smb_max_chain = self.smb_max_chain

        smb_max_compound = self.smb_max_compound

        valid_smb_versions: list[str] | Unset = UNSET
        if not isinstance(self.valid_smb_versions, Unset):
            valid_smb_versions = self.valid_smb_versions

        smb_file_depth = self.smb_file_depth

        smb_invalid_shares = self.smb_invalid_shares

        smb_legacy_mode = self.smb_legacy_mode

        smb_max_credit = self.smb_max_credit

        memcap = self.memcap

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if limit_alerts is not UNSET:
            field_dict["limit_alerts"] = limit_alerts
        if disable_defrag is not UNSET:
            field_dict["disable_defrag"] = disable_defrag
        if max_frag_len is not UNSET:
            field_dict["max_frag_len"] = max_frag_len
        if reassemble_threshold is not UNSET:
            field_dict["reassemble_threshold"] = reassemble_threshold
        if smb_fingerprint_policy is not UNSET:
            field_dict["smb_fingerprint_policy"] = smb_fingerprint_policy
        if policy is not UNSET:
            field_dict["policy"] = policy
        if smb_max_chain is not UNSET:
            field_dict["smb_max_chain"] = smb_max_chain
        if smb_max_compound is not UNSET:
            field_dict["smb_max_compound"] = smb_max_compound
        if valid_smb_versions is not UNSET:
            field_dict["valid_smb_versions"] = valid_smb_versions
        if smb_file_depth is not UNSET:
            field_dict["smb_file_depth"] = smb_file_depth
        if smb_invalid_shares is not UNSET:
            field_dict["smb_invalid_shares"] = smb_invalid_shares
        if smb_legacy_mode is not UNSET:
            field_dict["smb_legacy_mode"] = smb_legacy_mode
        if smb_max_credit is not UNSET:
            field_dict["smb_max_credit"] = smb_max_credit
        if memcap is not UNSET:
            field_dict["memcap"] = memcap

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        limit_alerts = d.pop("limit_alerts", UNSET)

        disable_defrag = d.pop("disable_defrag", UNSET)

        max_frag_len = d.pop("max_frag_len", UNSET)

        reassemble_threshold = d.pop("reassemble_threshold", UNSET)

        smb_fingerprint_policy = d.pop("smb_fingerprint_policy", UNSET)

        policy = d.pop("policy", UNSET)

        smb_max_chain = d.pop("smb_max_chain", UNSET)

        smb_max_compound = d.pop("smb_max_compound", UNSET)

        valid_smb_versions = cast(list[str], d.pop("valid_smb_versions", UNSET))

        smb_file_depth = d.pop("smb_file_depth", UNSET)

        smb_invalid_shares = d.pop("smb_invalid_shares", UNSET)

        smb_legacy_mode = d.pop("smb_legacy_mode", UNSET)

        smb_max_credit = d.pop("smb_max_credit", UNSET)

        memcap = d.pop("memcap", UNSET)

        snort_insp_dce_smb = cls(
            limit_alerts=limit_alerts,
            disable_defrag=disable_defrag,
            max_frag_len=max_frag_len,
            reassemble_threshold=reassemble_threshold,
            smb_fingerprint_policy=smb_fingerprint_policy,
            policy=policy,
            smb_max_chain=smb_max_chain,
            smb_max_compound=smb_max_compound,
            valid_smb_versions=valid_smb_versions,
            smb_file_depth=smb_file_depth,
            smb_invalid_shares=smb_invalid_shares,
            smb_legacy_mode=smb_legacy_mode,
            smb_max_credit=smb_max_credit,
            memcap=memcap,
        )

        snort_insp_dce_smb.additional_properties = d
        return snort_insp_dce_smb

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
