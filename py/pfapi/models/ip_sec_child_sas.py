from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IPSecChildSAS")


@_attrs_define
class IPSecChildSAS:
    """
    Attributes:
        name (str | Unset):
        uniqueid (str | Unset):
        reqid (str | Unset):
        state (str | Unset):
        mode (str | Unset):
        protocol (str | Unset):
        encap (str | Unset):
        spi_in (str | Unset):
        spi_out (str | Unset):
        cpi_in (str | Unset):
        cpi_out (str | Unset):
        mark_in (str | Unset):
        mark_mask_in (str | Unset):
        mark_out (str | Unset):
        mark_mask_out (str | Unset):
        if_id_in (str | Unset):
        if_id_out (str | Unset):
        label (str | Unset):
        encr_alg (str | Unset):
        encr_keysize (str | Unset):
        integ_alg (str | Unset):
        integ_keysize (str | Unset):
        prf_alg (str | Unset):
        dh_group (str | Unset):
        esn (str | Unset):
        bytes_in (int | Unset):
        packets_in (int | Unset):
        use_in (int | Unset):
        bytes_out (int | Unset):
        packets_out (int | Unset):
        use_out (int | Unset):
        rekey_time (int | Unset):
        life_time (int | Unset):
        install_time (int | Unset):
        local_ts (list[str] | Unset):
        remote_ts (list[str] | Unset):
    """

    name: str | Unset = UNSET
    uniqueid: str | Unset = UNSET
    reqid: str | Unset = UNSET
    state: str | Unset = UNSET
    mode: str | Unset = UNSET
    protocol: str | Unset = UNSET
    encap: str | Unset = UNSET
    spi_in: str | Unset = UNSET
    spi_out: str | Unset = UNSET
    cpi_in: str | Unset = UNSET
    cpi_out: str | Unset = UNSET
    mark_in: str | Unset = UNSET
    mark_mask_in: str | Unset = UNSET
    mark_out: str | Unset = UNSET
    mark_mask_out: str | Unset = UNSET
    if_id_in: str | Unset = UNSET
    if_id_out: str | Unset = UNSET
    label: str | Unset = UNSET
    encr_alg: str | Unset = UNSET
    encr_keysize: str | Unset = UNSET
    integ_alg: str | Unset = UNSET
    integ_keysize: str | Unset = UNSET
    prf_alg: str | Unset = UNSET
    dh_group: str | Unset = UNSET
    esn: str | Unset = UNSET
    bytes_in: int | Unset = UNSET
    packets_in: int | Unset = UNSET
    use_in: int | Unset = UNSET
    bytes_out: int | Unset = UNSET
    packets_out: int | Unset = UNSET
    use_out: int | Unset = UNSET
    rekey_time: int | Unset = UNSET
    life_time: int | Unset = UNSET
    install_time: int | Unset = UNSET
    local_ts: list[str] | Unset = UNSET
    remote_ts: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        uniqueid = self.uniqueid

        reqid = self.reqid

        state = self.state

        mode = self.mode

        protocol = self.protocol

        encap = self.encap

        spi_in = self.spi_in

        spi_out = self.spi_out

        cpi_in = self.cpi_in

        cpi_out = self.cpi_out

        mark_in = self.mark_in

        mark_mask_in = self.mark_mask_in

        mark_out = self.mark_out

        mark_mask_out = self.mark_mask_out

        if_id_in = self.if_id_in

        if_id_out = self.if_id_out

        label = self.label

        encr_alg = self.encr_alg

        encr_keysize = self.encr_keysize

        integ_alg = self.integ_alg

        integ_keysize = self.integ_keysize

        prf_alg = self.prf_alg

        dh_group = self.dh_group

        esn = self.esn

        bytes_in = self.bytes_in

        packets_in = self.packets_in

        use_in = self.use_in

        bytes_out = self.bytes_out

        packets_out = self.packets_out

        use_out = self.use_out

        rekey_time = self.rekey_time

        life_time = self.life_time

        install_time = self.install_time

        local_ts: list[str] | Unset = UNSET
        if not isinstance(self.local_ts, Unset):
            local_ts = self.local_ts

        remote_ts: list[str] | Unset = UNSET
        if not isinstance(self.remote_ts, Unset):
            remote_ts = self.remote_ts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if uniqueid is not UNSET:
            field_dict["uniqueid"] = uniqueid
        if reqid is not UNSET:
            field_dict["reqid"] = reqid
        if state is not UNSET:
            field_dict["state"] = state
        if mode is not UNSET:
            field_dict["mode"] = mode
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if encap is not UNSET:
            field_dict["encap"] = encap
        if spi_in is not UNSET:
            field_dict["spi_in"] = spi_in
        if spi_out is not UNSET:
            field_dict["spi_out"] = spi_out
        if cpi_in is not UNSET:
            field_dict["cpi_in"] = cpi_in
        if cpi_out is not UNSET:
            field_dict["cpi_out"] = cpi_out
        if mark_in is not UNSET:
            field_dict["mark_in"] = mark_in
        if mark_mask_in is not UNSET:
            field_dict["mark_mask_in"] = mark_mask_in
        if mark_out is not UNSET:
            field_dict["mark_out"] = mark_out
        if mark_mask_out is not UNSET:
            field_dict["mark_mask_out"] = mark_mask_out
        if if_id_in is not UNSET:
            field_dict["if_id_in"] = if_id_in
        if if_id_out is not UNSET:
            field_dict["if_id_out"] = if_id_out
        if label is not UNSET:
            field_dict["label"] = label
        if encr_alg is not UNSET:
            field_dict["encr_alg"] = encr_alg
        if encr_keysize is not UNSET:
            field_dict["encr_keysize"] = encr_keysize
        if integ_alg is not UNSET:
            field_dict["integ_alg"] = integ_alg
        if integ_keysize is not UNSET:
            field_dict["integ_keysize"] = integ_keysize
        if prf_alg is not UNSET:
            field_dict["prf_alg"] = prf_alg
        if dh_group is not UNSET:
            field_dict["dh_group"] = dh_group
        if esn is not UNSET:
            field_dict["esn"] = esn
        if bytes_in is not UNSET:
            field_dict["bytes_in"] = bytes_in
        if packets_in is not UNSET:
            field_dict["packets_in"] = packets_in
        if use_in is not UNSET:
            field_dict["use_in"] = use_in
        if bytes_out is not UNSET:
            field_dict["bytes_out"] = bytes_out
        if packets_out is not UNSET:
            field_dict["packets_out"] = packets_out
        if use_out is not UNSET:
            field_dict["use_out"] = use_out
        if rekey_time is not UNSET:
            field_dict["rekey_time"] = rekey_time
        if life_time is not UNSET:
            field_dict["life_time"] = life_time
        if install_time is not UNSET:
            field_dict["install_time"] = install_time
        if local_ts is not UNSET:
            field_dict["local_ts"] = local_ts
        if remote_ts is not UNSET:
            field_dict["remote_ts"] = remote_ts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        uniqueid = d.pop("uniqueid", UNSET)

        reqid = d.pop("reqid", UNSET)

        state = d.pop("state", UNSET)

        mode = d.pop("mode", UNSET)

        protocol = d.pop("protocol", UNSET)

        encap = d.pop("encap", UNSET)

        spi_in = d.pop("spi_in", UNSET)

        spi_out = d.pop("spi_out", UNSET)

        cpi_in = d.pop("cpi_in", UNSET)

        cpi_out = d.pop("cpi_out", UNSET)

        mark_in = d.pop("mark_in", UNSET)

        mark_mask_in = d.pop("mark_mask_in", UNSET)

        mark_out = d.pop("mark_out", UNSET)

        mark_mask_out = d.pop("mark_mask_out", UNSET)

        if_id_in = d.pop("if_id_in", UNSET)

        if_id_out = d.pop("if_id_out", UNSET)

        label = d.pop("label", UNSET)

        encr_alg = d.pop("encr_alg", UNSET)

        encr_keysize = d.pop("encr_keysize", UNSET)

        integ_alg = d.pop("integ_alg", UNSET)

        integ_keysize = d.pop("integ_keysize", UNSET)

        prf_alg = d.pop("prf_alg", UNSET)

        dh_group = d.pop("dh_group", UNSET)

        esn = d.pop("esn", UNSET)

        bytes_in = d.pop("bytes_in", UNSET)

        packets_in = d.pop("packets_in", UNSET)

        use_in = d.pop("use_in", UNSET)

        bytes_out = d.pop("bytes_out", UNSET)

        packets_out = d.pop("packets_out", UNSET)

        use_out = d.pop("use_out", UNSET)

        rekey_time = d.pop("rekey_time", UNSET)

        life_time = d.pop("life_time", UNSET)

        install_time = d.pop("install_time", UNSET)

        local_ts = cast(list[str], d.pop("local_ts", UNSET))

        remote_ts = cast(list[str], d.pop("remote_ts", UNSET))

        ip_sec_child_sas = cls(
            name=name,
            uniqueid=uniqueid,
            reqid=reqid,
            state=state,
            mode=mode,
            protocol=protocol,
            encap=encap,
            spi_in=spi_in,
            spi_out=spi_out,
            cpi_in=cpi_in,
            cpi_out=cpi_out,
            mark_in=mark_in,
            mark_mask_in=mark_mask_in,
            mark_out=mark_out,
            mark_mask_out=mark_mask_out,
            if_id_in=if_id_in,
            if_id_out=if_id_out,
            label=label,
            encr_alg=encr_alg,
            encr_keysize=encr_keysize,
            integ_alg=integ_alg,
            integ_keysize=integ_keysize,
            prf_alg=prf_alg,
            dh_group=dh_group,
            esn=esn,
            bytes_in=bytes_in,
            packets_in=packets_in,
            use_in=use_in,
            bytes_out=bytes_out,
            packets_out=packets_out,
            use_out=use_out,
            rekey_time=rekey_time,
            life_time=life_time,
            install_time=install_time,
            local_ts=local_ts,
            remote_ts=remote_ts,
        )

        ip_sec_child_sas.additional_properties = d
        return ip_sec_child_sas

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
