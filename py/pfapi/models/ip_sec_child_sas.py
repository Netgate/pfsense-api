from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IPSecChildSAS")


@_attrs_define
class IPSecChildSAS:
    """
    Attributes:
        name (str):
        uniqueid (str):
        reqid (str):
        state (str):
        mode (str):
        protocol (str):
        encap (str):
        spi_in (str):
        spi_out (str):
        cpi_in (str):
        cpi_out (str):
        mark_in (str):
        mark_mask_in (str):
        mark_out (str):
        mark_mask_out (str):
        if_id_in (str):
        if_id_out (str):
        label (str):
        encr_alg (str):
        encr_keysize (str):
        integ_alg (str):
        integ_keysize (str):
        prf_alg (str):
        dh_group (str):
        esn (str):
        bytes_in (int):
        packets_in (int):
        use_in (int):
        bytes_out (int):
        packets_out (int):
        use_out (int):
        rekey_time (int):
        life_time (int):
        install_time (int):
        local_ts (Union[Unset, List[str]]):
        remote_ts (Union[Unset, List[str]]):
    """

    name: str
    uniqueid: str
    reqid: str
    state: str
    mode: str
    protocol: str
    encap: str
    spi_in: str
    spi_out: str
    cpi_in: str
    cpi_out: str
    mark_in: str
    mark_mask_in: str
    mark_out: str
    mark_mask_out: str
    if_id_in: str
    if_id_out: str
    label: str
    encr_alg: str
    encr_keysize: str
    integ_alg: str
    integ_keysize: str
    prf_alg: str
    dh_group: str
    esn: str
    bytes_in: int
    packets_in: int
    use_in: int
    bytes_out: int
    packets_out: int
    use_out: int
    rekey_time: int
    life_time: int
    install_time: int
    local_ts: Union[Unset, List[str]] = UNSET
    remote_ts: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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

        local_ts: Union[Unset, List[str]] = UNSET
        if not isinstance(self.local_ts, Unset):
            local_ts = self.local_ts

        remote_ts: Union[Unset, List[str]] = UNSET
        if not isinstance(self.remote_ts, Unset):
            remote_ts = self.remote_ts

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "uniqueid": uniqueid,
                "reqid": reqid,
                "state": state,
                "mode": mode,
                "protocol": protocol,
                "encap": encap,
                "spi_in": spi_in,
                "spi_out": spi_out,
                "cpi_in": cpi_in,
                "cpi_out": cpi_out,
                "mark_in": mark_in,
                "mark_mask_in": mark_mask_in,
                "mark_out": mark_out,
                "mark_mask_out": mark_mask_out,
                "if_id_in": if_id_in,
                "if_id_out": if_id_out,
                "label": label,
                "encr_alg": encr_alg,
                "encr_keysize": encr_keysize,
                "integ_alg": integ_alg,
                "integ_keysize": integ_keysize,
                "prf_alg": prf_alg,
                "dh_group": dh_group,
                "esn": esn,
                "bytes_in": bytes_in,
                "packets_in": packets_in,
                "use_in": use_in,
                "bytes_out": bytes_out,
                "packets_out": packets_out,
                "use_out": use_out,
                "rekey_time": rekey_time,
                "life_time": life_time,
                "install_time": install_time,
            }
        )
        if local_ts is not UNSET:
            field_dict["local_ts"] = local_ts
        if remote_ts is not UNSET:
            field_dict["remote_ts"] = remote_ts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        uniqueid = d.pop("uniqueid")

        reqid = d.pop("reqid")

        state = d.pop("state")

        mode = d.pop("mode")

        protocol = d.pop("protocol")

        encap = d.pop("encap")

        spi_in = d.pop("spi_in")

        spi_out = d.pop("spi_out")

        cpi_in = d.pop("cpi_in")

        cpi_out = d.pop("cpi_out")

        mark_in = d.pop("mark_in")

        mark_mask_in = d.pop("mark_mask_in")

        mark_out = d.pop("mark_out")

        mark_mask_out = d.pop("mark_mask_out")

        if_id_in = d.pop("if_id_in")

        if_id_out = d.pop("if_id_out")

        label = d.pop("label")

        encr_alg = d.pop("encr_alg")

        encr_keysize = d.pop("encr_keysize")

        integ_alg = d.pop("integ_alg")

        integ_keysize = d.pop("integ_keysize")

        prf_alg = d.pop("prf_alg")

        dh_group = d.pop("dh_group")

        esn = d.pop("esn")

        bytes_in = d.pop("bytes_in")

        packets_in = d.pop("packets_in")

        use_in = d.pop("use_in")

        bytes_out = d.pop("bytes_out")

        packets_out = d.pop("packets_out")

        use_out = d.pop("use_out")

        rekey_time = d.pop("rekey_time")

        life_time = d.pop("life_time")

        install_time = d.pop("install_time")

        local_ts = cast(List[str], d.pop("local_ts", UNSET))

        remote_ts = cast(List[str], d.pop("remote_ts", UNSET))

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
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
