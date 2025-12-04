from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.encryption_algorithm import EncryptionAlgorithm
    from ..models.phase_2_local_id import Phase2LocalId
    from ..models.phase_2_remote_id import Phase2RemoteId


T = TypeVar("T", bound="Phase2")


@_attrs_define
class Phase2:
    """
    Attributes:
        ikeid (str | Unset):
        uniqid (str | Unset):
        mode (str | Unset):
        reqid (str | Unset):
        localid (Phase2LocalId | Unset):
        remoteid (Phase2RemoteId | Unset):
        protocol (str | Unset):
        encryption_algorithm_option (list[EncryptionAlgorithm] | Unset):
        hash_algorithm_option (list[str] | Unset):
        pfsgroup (str | Unset):
        lifetime (int | Unset):
        rekey_time (int | Unset):
        rand_time (int | Unset):
        pinghost (str | Unset):
        keepalive (bool | Unset):
        mobile (bool | Unset):
        disabled (bool | Unset):
        descr (str | Unset):
    """

    ikeid: str | Unset = UNSET
    uniqid: str | Unset = UNSET
    mode: str | Unset = UNSET
    reqid: str | Unset = UNSET
    localid: Phase2LocalId | Unset = UNSET
    remoteid: Phase2RemoteId | Unset = UNSET
    protocol: str | Unset = UNSET
    encryption_algorithm_option: list[EncryptionAlgorithm] | Unset = UNSET
    hash_algorithm_option: list[str] | Unset = UNSET
    pfsgroup: str | Unset = UNSET
    lifetime: int | Unset = UNSET
    rekey_time: int | Unset = UNSET
    rand_time: int | Unset = UNSET
    pinghost: str | Unset = UNSET
    keepalive: bool | Unset = UNSET
    mobile: bool | Unset = UNSET
    disabled: bool | Unset = UNSET
    descr: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ikeid = self.ikeid

        uniqid = self.uniqid

        mode = self.mode

        reqid = self.reqid

        localid: dict[str, Any] | Unset = UNSET
        if not isinstance(self.localid, Unset):
            localid = self.localid.to_dict()

        remoteid: dict[str, Any] | Unset = UNSET
        if not isinstance(self.remoteid, Unset):
            remoteid = self.remoteid.to_dict()

        protocol = self.protocol

        encryption_algorithm_option: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.encryption_algorithm_option, Unset):
            encryption_algorithm_option = []
            for encryption_algorithm_option_item_data in self.encryption_algorithm_option:
                encryption_algorithm_option_item = encryption_algorithm_option_item_data.to_dict()
                encryption_algorithm_option.append(encryption_algorithm_option_item)

        hash_algorithm_option: list[str] | Unset = UNSET
        if not isinstance(self.hash_algorithm_option, Unset):
            hash_algorithm_option = self.hash_algorithm_option

        pfsgroup = self.pfsgroup

        lifetime = self.lifetime

        rekey_time = self.rekey_time

        rand_time = self.rand_time

        pinghost = self.pinghost

        keepalive = self.keepalive

        mobile = self.mobile

        disabled = self.disabled

        descr = self.descr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ikeid is not UNSET:
            field_dict["ikeid"] = ikeid
        if uniqid is not UNSET:
            field_dict["uniqid"] = uniqid
        if mode is not UNSET:
            field_dict["mode"] = mode
        if reqid is not UNSET:
            field_dict["reqid"] = reqid
        if localid is not UNSET:
            field_dict["localid"] = localid
        if remoteid is not UNSET:
            field_dict["remoteid"] = remoteid
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if encryption_algorithm_option is not UNSET:
            field_dict["encryption_algorithm_option"] = encryption_algorithm_option
        if hash_algorithm_option is not UNSET:
            field_dict["hash_algorithm_option"] = hash_algorithm_option
        if pfsgroup is not UNSET:
            field_dict["pfsgroup"] = pfsgroup
        if lifetime is not UNSET:
            field_dict["lifetime"] = lifetime
        if rekey_time is not UNSET:
            field_dict["rekey_time"] = rekey_time
        if rand_time is not UNSET:
            field_dict["rand_time"] = rand_time
        if pinghost is not UNSET:
            field_dict["pinghost"] = pinghost
        if keepalive is not UNSET:
            field_dict["keepalive"] = keepalive
        if mobile is not UNSET:
            field_dict["mobile"] = mobile
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if descr is not UNSET:
            field_dict["descr"] = descr

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.encryption_algorithm import EncryptionAlgorithm
        from ..models.phase_2_local_id import Phase2LocalId
        from ..models.phase_2_remote_id import Phase2RemoteId

        d = dict(src_dict)
        ikeid = d.pop("ikeid", UNSET)

        uniqid = d.pop("uniqid", UNSET)

        mode = d.pop("mode", UNSET)

        reqid = d.pop("reqid", UNSET)

        _localid = d.pop("localid", UNSET)
        localid: Phase2LocalId | Unset
        if isinstance(_localid, Unset):
            localid = UNSET
        else:
            localid = Phase2LocalId.from_dict(_localid)

        _remoteid = d.pop("remoteid", UNSET)
        remoteid: Phase2RemoteId | Unset
        if isinstance(_remoteid, Unset):
            remoteid = UNSET
        else:
            remoteid = Phase2RemoteId.from_dict(_remoteid)

        protocol = d.pop("protocol", UNSET)

        _encryption_algorithm_option = d.pop("encryption_algorithm_option", UNSET)
        encryption_algorithm_option: list[EncryptionAlgorithm] | Unset = UNSET
        if _encryption_algorithm_option is not UNSET:
            encryption_algorithm_option = []
            for encryption_algorithm_option_item_data in _encryption_algorithm_option:
                encryption_algorithm_option_item = EncryptionAlgorithm.from_dict(encryption_algorithm_option_item_data)

                encryption_algorithm_option.append(encryption_algorithm_option_item)

        hash_algorithm_option = cast(list[str], d.pop("hash_algorithm_option", UNSET))

        pfsgroup = d.pop("pfsgroup", UNSET)

        lifetime = d.pop("lifetime", UNSET)

        rekey_time = d.pop("rekey_time", UNSET)

        rand_time = d.pop("rand_time", UNSET)

        pinghost = d.pop("pinghost", UNSET)

        keepalive = d.pop("keepalive", UNSET)

        mobile = d.pop("mobile", UNSET)

        disabled = d.pop("disabled", UNSET)

        descr = d.pop("descr", UNSET)

        phase_2 = cls(
            ikeid=ikeid,
            uniqid=uniqid,
            mode=mode,
            reqid=reqid,
            localid=localid,
            remoteid=remoteid,
            protocol=protocol,
            encryption_algorithm_option=encryption_algorithm_option,
            hash_algorithm_option=hash_algorithm_option,
            pfsgroup=pfsgroup,
            lifetime=lifetime,
            rekey_time=rekey_time,
            rand_time=rand_time,
            pinghost=pinghost,
            keepalive=keepalive,
            mobile=mobile,
            disabled=disabled,
            descr=descr,
        )

        phase_2.additional_properties = d
        return phase_2

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
