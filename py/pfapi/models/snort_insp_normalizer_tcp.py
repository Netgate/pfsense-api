from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortInspNormalizerTcp")


@_attrs_define
class SnortInspNormalizerTcp:
    """
    Attributes:
        base (bool | Unset): clear reserved bits and option padding and fix urgent pointer / flags issues; default false
        block (bool | Unset): allow packet drops during TCP normalization; default false
        urp (bool | Unset): adjust urgent pointer if beyond segment length; default false
        ips (bool | Unset): ensure consistency in retransmitted data; default true
        ecn (str | Unset): clear ecn for all packets | sessions w/o ecn setup { off | packet | stream }; default off
        pad (bool | Unset): clear any option padding bytes; default false
        trim_syn (bool | Unset): remove data on SYN; default false
        trim_rst (bool | Unset): remove any data from RST packet; default false
        trim_win (bool | Unset): trim data to window; default false
        trim_mss (bool | Unset): trim data to MSS; default false
        opts (bool | Unset): clear all options except mss, wscale, timestamp, and any explicitly allowed; default false
        req_urg (bool | Unset): clear the urgent pointer if the urgent flag is not set; default false
        req_pay (bool | Unset): clear the urgent pointer and the urgent flag if there is no payload; default false
        rsv (bool | Unset): clear the reserved bits in the TCP header; default false
        req_urp (bool | Unset): clear the urgent flag if the urgent pointer is not set; default false
        allow_names (list[str] | Unset):
        allow_codes (str | Unset): don’t clear given option codes
    """

    base: bool | Unset = UNSET
    block: bool | Unset = UNSET
    urp: bool | Unset = UNSET
    ips: bool | Unset = UNSET
    ecn: str | Unset = UNSET
    pad: bool | Unset = UNSET
    trim_syn: bool | Unset = UNSET
    trim_rst: bool | Unset = UNSET
    trim_win: bool | Unset = UNSET
    trim_mss: bool | Unset = UNSET
    opts: bool | Unset = UNSET
    req_urg: bool | Unset = UNSET
    req_pay: bool | Unset = UNSET
    rsv: bool | Unset = UNSET
    req_urp: bool | Unset = UNSET
    allow_names: list[str] | Unset = UNSET
    allow_codes: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base = self.base

        block = self.block

        urp = self.urp

        ips = self.ips

        ecn = self.ecn

        pad = self.pad

        trim_syn = self.trim_syn

        trim_rst = self.trim_rst

        trim_win = self.trim_win

        trim_mss = self.trim_mss

        opts = self.opts

        req_urg = self.req_urg

        req_pay = self.req_pay

        rsv = self.rsv

        req_urp = self.req_urp

        allow_names: list[str] | Unset = UNSET
        if not isinstance(self.allow_names, Unset):
            allow_names = self.allow_names

        allow_codes = self.allow_codes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base is not UNSET:
            field_dict["base"] = base
        if block is not UNSET:
            field_dict["block"] = block
        if urp is not UNSET:
            field_dict["urp"] = urp
        if ips is not UNSET:
            field_dict["ips"] = ips
        if ecn is not UNSET:
            field_dict["ecn"] = ecn
        if pad is not UNSET:
            field_dict["pad"] = pad
        if trim_syn is not UNSET:
            field_dict["trim_syn"] = trim_syn
        if trim_rst is not UNSET:
            field_dict["trim_rst"] = trim_rst
        if trim_win is not UNSET:
            field_dict["trim_win"] = trim_win
        if trim_mss is not UNSET:
            field_dict["trim_mss"] = trim_mss
        if opts is not UNSET:
            field_dict["opts"] = opts
        if req_urg is not UNSET:
            field_dict["req_urg"] = req_urg
        if req_pay is not UNSET:
            field_dict["req_pay"] = req_pay
        if rsv is not UNSET:
            field_dict["rsv"] = rsv
        if req_urp is not UNSET:
            field_dict["req_urp"] = req_urp
        if allow_names is not UNSET:
            field_dict["allow_names"] = allow_names
        if allow_codes is not UNSET:
            field_dict["allow_codes"] = allow_codes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        base = d.pop("base", UNSET)

        block = d.pop("block", UNSET)

        urp = d.pop("urp", UNSET)

        ips = d.pop("ips", UNSET)

        ecn = d.pop("ecn", UNSET)

        pad = d.pop("pad", UNSET)

        trim_syn = d.pop("trim_syn", UNSET)

        trim_rst = d.pop("trim_rst", UNSET)

        trim_win = d.pop("trim_win", UNSET)

        trim_mss = d.pop("trim_mss", UNSET)

        opts = d.pop("opts", UNSET)

        req_urg = d.pop("req_urg", UNSET)

        req_pay = d.pop("req_pay", UNSET)

        rsv = d.pop("rsv", UNSET)

        req_urp = d.pop("req_urp", UNSET)

        allow_names = cast(list[str], d.pop("allow_names", UNSET))

        allow_codes = d.pop("allow_codes", UNSET)

        snort_insp_normalizer_tcp = cls(
            base=base,
            block=block,
            urp=urp,
            ips=ips,
            ecn=ecn,
            pad=pad,
            trim_syn=trim_syn,
            trim_rst=trim_rst,
            trim_win=trim_win,
            trim_mss=trim_mss,
            opts=opts,
            req_urg=req_urg,
            req_pay=req_pay,
            rsv=rsv,
            req_urp=req_urp,
            allow_names=allow_names,
            allow_codes=allow_codes,
        )

        snort_insp_normalizer_tcp.additional_properties = d
        return snort_insp_normalizer_tcp

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
