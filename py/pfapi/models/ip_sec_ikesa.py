from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ip_sec_child_sas import IPSecChildSAS


T = TypeVar("T", bound="IPSecIKESA")


@_attrs_define
class IPSecIKESA:
    """
    Attributes:
        name (str | Unset):
        uniqueid (str | Unset):
        version (int | Unset):
        state (str | Unset):
        local_host (str | Unset):
        local_port (str | Unset):
        local_id (str | Unset):
        remote_host (str | Unset):
        remote_port (str | Unset):
        remote_id (str | Unset):
        initiator (str | Unset):
        initiator_spi (str | Unset):
        responder_spi (str | Unset):
        encr_alg (str | Unset):
        encr_keysize (int | Unset):
        integ_alg (str | Unset):
        integ_keysize (int | Unset):
        prf_alg (str | Unset):
        dh_group (str | Unset):
        established (int | Unset):
        rekey_time (int | Unset):
        reauth_time (int | Unset):
        childsas (list[IPSecChildSAS] | Unset):
    """

    name: str | Unset = UNSET
    uniqueid: str | Unset = UNSET
    version: int | Unset = UNSET
    state: str | Unset = UNSET
    local_host: str | Unset = UNSET
    local_port: str | Unset = UNSET
    local_id: str | Unset = UNSET
    remote_host: str | Unset = UNSET
    remote_port: str | Unset = UNSET
    remote_id: str | Unset = UNSET
    initiator: str | Unset = UNSET
    initiator_spi: str | Unset = UNSET
    responder_spi: str | Unset = UNSET
    encr_alg: str | Unset = UNSET
    encr_keysize: int | Unset = UNSET
    integ_alg: str | Unset = UNSET
    integ_keysize: int | Unset = UNSET
    prf_alg: str | Unset = UNSET
    dh_group: str | Unset = UNSET
    established: int | Unset = UNSET
    rekey_time: int | Unset = UNSET
    reauth_time: int | Unset = UNSET
    childsas: list[IPSecChildSAS] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        uniqueid = self.uniqueid

        version = self.version

        state = self.state

        local_host = self.local_host

        local_port = self.local_port

        local_id = self.local_id

        remote_host = self.remote_host

        remote_port = self.remote_port

        remote_id = self.remote_id

        initiator = self.initiator

        initiator_spi = self.initiator_spi

        responder_spi = self.responder_spi

        encr_alg = self.encr_alg

        encr_keysize = self.encr_keysize

        integ_alg = self.integ_alg

        integ_keysize = self.integ_keysize

        prf_alg = self.prf_alg

        dh_group = self.dh_group

        established = self.established

        rekey_time = self.rekey_time

        reauth_time = self.reauth_time

        childsas: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.childsas, Unset):
            childsas = []
            for childsas_item_data in self.childsas:
                childsas_item = childsas_item_data.to_dict()
                childsas.append(childsas_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if uniqueid is not UNSET:
            field_dict["uniqueid"] = uniqueid
        if version is not UNSET:
            field_dict["version"] = version
        if state is not UNSET:
            field_dict["state"] = state
        if local_host is not UNSET:
            field_dict["local_host"] = local_host
        if local_port is not UNSET:
            field_dict["local_port"] = local_port
        if local_id is not UNSET:
            field_dict["local_id"] = local_id
        if remote_host is not UNSET:
            field_dict["remote_host"] = remote_host
        if remote_port is not UNSET:
            field_dict["remote_port"] = remote_port
        if remote_id is not UNSET:
            field_dict["remote_id"] = remote_id
        if initiator is not UNSET:
            field_dict["initiator"] = initiator
        if initiator_spi is not UNSET:
            field_dict["initiator_spi"] = initiator_spi
        if responder_spi is not UNSET:
            field_dict["responder_spi"] = responder_spi
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
        if established is not UNSET:
            field_dict["established"] = established
        if rekey_time is not UNSET:
            field_dict["rekey_time"] = rekey_time
        if reauth_time is not UNSET:
            field_dict["reauth_time"] = reauth_time
        if childsas is not UNSET:
            field_dict["childsas"] = childsas

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ip_sec_child_sas import IPSecChildSAS

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        uniqueid = d.pop("uniqueid", UNSET)

        version = d.pop("version", UNSET)

        state = d.pop("state", UNSET)

        local_host = d.pop("local_host", UNSET)

        local_port = d.pop("local_port", UNSET)

        local_id = d.pop("local_id", UNSET)

        remote_host = d.pop("remote_host", UNSET)

        remote_port = d.pop("remote_port", UNSET)

        remote_id = d.pop("remote_id", UNSET)

        initiator = d.pop("initiator", UNSET)

        initiator_spi = d.pop("initiator_spi", UNSET)

        responder_spi = d.pop("responder_spi", UNSET)

        encr_alg = d.pop("encr_alg", UNSET)

        encr_keysize = d.pop("encr_keysize", UNSET)

        integ_alg = d.pop("integ_alg", UNSET)

        integ_keysize = d.pop("integ_keysize", UNSET)

        prf_alg = d.pop("prf_alg", UNSET)

        dh_group = d.pop("dh_group", UNSET)

        established = d.pop("established", UNSET)

        rekey_time = d.pop("rekey_time", UNSET)

        reauth_time = d.pop("reauth_time", UNSET)

        _childsas = d.pop("childsas", UNSET)
        childsas: list[IPSecChildSAS] | Unset = UNSET
        if _childsas is not UNSET:
            childsas = []
            for childsas_item_data in _childsas:
                childsas_item = IPSecChildSAS.from_dict(childsas_item_data)

                childsas.append(childsas_item)

        ip_sec_ikesa = cls(
            name=name,
            uniqueid=uniqueid,
            version=version,
            state=state,
            local_host=local_host,
            local_port=local_port,
            local_id=local_id,
            remote_host=remote_host,
            remote_port=remote_port,
            remote_id=remote_id,
            initiator=initiator,
            initiator_spi=initiator_spi,
            responder_spi=responder_spi,
            encr_alg=encr_alg,
            encr_keysize=encr_keysize,
            integ_alg=integ_alg,
            integ_keysize=integ_keysize,
            prf_alg=prf_alg,
            dh_group=dh_group,
            established=established,
            rekey_time=rekey_time,
            reauth_time=reauth_time,
            childsas=childsas,
        )

        ip_sec_ikesa.additional_properties = d
        return ip_sec_ikesa

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
