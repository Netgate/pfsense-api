from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SyslogConfigOverride")


@_attrs_define
class SyslogConfigOverride:
    """
    Attributes:
        cronorder (str | Unset): reverse, forward, or empty for default
        nentries (int | Unset):
        logfilesize (int | Unset):
        rotatecount (int | Unset):
        format_ (str | Unset): formatted, raw
        lognginx (bool | Unset):
        logipoptions (bool | Unset): log blocked packets due to IP options
        logdefaultblock (bool | Unset): log default "block" rules
        logdefaultpass (bool | Unset): log default "pass" rules
        logbogons (bool | Unset): log Bogon Networks block rules
        logprivatenets (bool | Unset): log Private Networks block rules
        loglinklocal4 (bool | Unset): log IPv4 link-local block rules
        logids (bool | Unset): log hosts blocked by IDS
        showfilterdescrips (str | Unset): where to show firewall rule descriptions:
            * "disable" - don't show,
            * "column"  - as column,
            * "row"     - as second row
    """

    cronorder: str | Unset = UNSET
    nentries: int | Unset = UNSET
    logfilesize: int | Unset = UNSET
    rotatecount: int | Unset = UNSET
    format_: str | Unset = UNSET
    lognginx: bool | Unset = UNSET
    logipoptions: bool | Unset = UNSET
    logdefaultblock: bool | Unset = UNSET
    logdefaultpass: bool | Unset = UNSET
    logbogons: bool | Unset = UNSET
    logprivatenets: bool | Unset = UNSET
    loglinklocal4: bool | Unset = UNSET
    logids: bool | Unset = UNSET
    showfilterdescrips: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cronorder = self.cronorder

        nentries = self.nentries

        logfilesize = self.logfilesize

        rotatecount = self.rotatecount

        format_ = self.format_

        lognginx = self.lognginx

        logipoptions = self.logipoptions

        logdefaultblock = self.logdefaultblock

        logdefaultpass = self.logdefaultpass

        logbogons = self.logbogons

        logprivatenets = self.logprivatenets

        loglinklocal4 = self.loglinklocal4

        logids = self.logids

        showfilterdescrips = self.showfilterdescrips

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cronorder is not UNSET:
            field_dict["cronorder"] = cronorder
        if nentries is not UNSET:
            field_dict["nentries"] = nentries
        if logfilesize is not UNSET:
            field_dict["logfilesize"] = logfilesize
        if rotatecount is not UNSET:
            field_dict["rotatecount"] = rotatecount
        if format_ is not UNSET:
            field_dict["format"] = format_
        if lognginx is not UNSET:
            field_dict["lognginx"] = lognginx
        if logipoptions is not UNSET:
            field_dict["logipoptions"] = logipoptions
        if logdefaultblock is not UNSET:
            field_dict["logdefaultblock"] = logdefaultblock
        if logdefaultpass is not UNSET:
            field_dict["logdefaultpass"] = logdefaultpass
        if logbogons is not UNSET:
            field_dict["logbogons"] = logbogons
        if logprivatenets is not UNSET:
            field_dict["logprivatenets"] = logprivatenets
        if loglinklocal4 is not UNSET:
            field_dict["loglinklocal4"] = loglinklocal4
        if logids is not UNSET:
            field_dict["logids"] = logids
        if showfilterdescrips is not UNSET:
            field_dict["showfilterdescrips"] = showfilterdescrips

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cronorder = d.pop("cronorder", UNSET)

        nentries = d.pop("nentries", UNSET)

        logfilesize = d.pop("logfilesize", UNSET)

        rotatecount = d.pop("rotatecount", UNSET)

        format_ = d.pop("format", UNSET)

        lognginx = d.pop("lognginx", UNSET)

        logipoptions = d.pop("logipoptions", UNSET)

        logdefaultblock = d.pop("logdefaultblock", UNSET)

        logdefaultpass = d.pop("logdefaultpass", UNSET)

        logbogons = d.pop("logbogons", UNSET)

        logprivatenets = d.pop("logprivatenets", UNSET)

        loglinklocal4 = d.pop("loglinklocal4", UNSET)

        logids = d.pop("logids", UNSET)

        showfilterdescrips = d.pop("showfilterdescrips", UNSET)

        syslog_config_override = cls(
            cronorder=cronorder,
            nentries=nentries,
            logfilesize=logfilesize,
            rotatecount=rotatecount,
            format_=format_,
            lognginx=lognginx,
            logipoptions=logipoptions,
            logdefaultblock=logdefaultblock,
            logdefaultpass=logdefaultpass,
            logbogons=logbogons,
            logprivatenets=logprivatenets,
            loglinklocal4=loglinklocal4,
            logids=logids,
            showfilterdescrips=showfilterdescrips,
        )

        syslog_config_override.additional_properties = d
        return syslog_config_override

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
