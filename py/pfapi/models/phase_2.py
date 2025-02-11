from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

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
        ikeid (str):
        uniqid (str):
        mode (str):
        reqid (str):
        localid (Phase2LocalId):
        remoteid (Phase2RemoteId):
        protocol (str):
        pfsgroup (str):
        lifetime (int):
        rekey_time (int):
        rand_time (int):
        pinghost (str):
        keepalive (bool):
        mobile (bool):
        disabled (bool):
        descr (str):
        encryption_algorithm_option (Union[Unset, List['EncryptionAlgorithm']]):
        hash_algorithm_option (Union[Unset, List[str]]):
    """

    ikeid: str
    uniqid: str
    mode: str
    reqid: str
    localid: "Phase2LocalId"
    remoteid: "Phase2RemoteId"
    protocol: str
    pfsgroup: str
    lifetime: int
    rekey_time: int
    rand_time: int
    pinghost: str
    keepalive: bool
    mobile: bool
    disabled: bool
    descr: str
    encryption_algorithm_option: Union[Unset, List["EncryptionAlgorithm"]] = UNSET
    hash_algorithm_option: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ikeid = self.ikeid

        uniqid = self.uniqid

        mode = self.mode

        reqid = self.reqid

        localid = self.localid.to_dict()

        remoteid = self.remoteid.to_dict()

        protocol = self.protocol

        pfsgroup = self.pfsgroup

        lifetime = self.lifetime

        rekey_time = self.rekey_time

        rand_time = self.rand_time

        pinghost = self.pinghost

        keepalive = self.keepalive

        mobile = self.mobile

        disabled = self.disabled

        descr = self.descr

        encryption_algorithm_option: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.encryption_algorithm_option, Unset):
            encryption_algorithm_option = []
            for encryption_algorithm_option_item_data in self.encryption_algorithm_option:
                encryption_algorithm_option_item = encryption_algorithm_option_item_data.to_dict()
                encryption_algorithm_option.append(encryption_algorithm_option_item)

        hash_algorithm_option: Union[Unset, List[str]] = UNSET
        if not isinstance(self.hash_algorithm_option, Unset):
            hash_algorithm_option = self.hash_algorithm_option

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ikeid": ikeid,
                "uniqid": uniqid,
                "mode": mode,
                "reqid": reqid,
                "localid": localid,
                "remoteid": remoteid,
                "protocol": protocol,
                "pfsgroup": pfsgroup,
                "lifetime": lifetime,
                "rekey_time": rekey_time,
                "rand_time": rand_time,
                "pinghost": pinghost,
                "keepalive": keepalive,
                "mobile": mobile,
                "disabled": disabled,
                "descr": descr,
            }
        )
        if encryption_algorithm_option is not UNSET:
            field_dict["encryption_algorithm_option"] = encryption_algorithm_option
        if hash_algorithm_option is not UNSET:
            field_dict["hash_algorithm_option"] = hash_algorithm_option

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.encryption_algorithm import EncryptionAlgorithm
        from ..models.phase_2_local_id import Phase2LocalId
        from ..models.phase_2_remote_id import Phase2RemoteId

        d = src_dict.copy()
        ikeid = d.pop("ikeid")

        uniqid = d.pop("uniqid")

        mode = d.pop("mode")

        reqid = d.pop("reqid")

        localid = Phase2LocalId.from_dict(d.pop("localid"))

        remoteid = Phase2RemoteId.from_dict(d.pop("remoteid"))

        protocol = d.pop("protocol")

        pfsgroup = d.pop("pfsgroup")

        lifetime = d.pop("lifetime")

        rekey_time = d.pop("rekey_time")

        rand_time = d.pop("rand_time")

        pinghost = d.pop("pinghost")

        keepalive = d.pop("keepalive")

        mobile = d.pop("mobile")

        disabled = d.pop("disabled")

        descr = d.pop("descr")

        encryption_algorithm_option = []
        _encryption_algorithm_option = d.pop("encryption_algorithm_option", UNSET)
        for encryption_algorithm_option_item_data in _encryption_algorithm_option or []:
            encryption_algorithm_option_item = EncryptionAlgorithm.from_dict(encryption_algorithm_option_item_data)

            encryption_algorithm_option.append(encryption_algorithm_option_item)

        hash_algorithm_option = cast(List[str], d.pop("hash_algorithm_option", UNSET))

        phase_2 = cls(
            ikeid=ikeid,
            uniqid=uniqid,
            mode=mode,
            reqid=reqid,
            localid=localid,
            remoteid=remoteid,
            protocol=protocol,
            pfsgroup=pfsgroup,
            lifetime=lifetime,
            rekey_time=rekey_time,
            rand_time=rand_time,
            pinghost=pinghost,
            keepalive=keepalive,
            mobile=mobile,
            disabled=disabled,
            descr=descr,
            encryption_algorithm_option=encryption_algorithm_option,
            hash_algorithm_option=hash_algorithm_option,
        )

        phase_2.additional_properties = d
        return phase_2

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
