from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.controller_descrip_host_os import ControllerDescripHostOs
    from ..models.controller_stats import ControllerStats


T = TypeVar("T", bound="ControllerDescrip")


@_attrs_define
class ControllerDescrip:
    """
    Attributes:
        build (Union[Unset, str]):
        api_version (Union[Unset, str]):
        host (Union[Unset, str]):
        host_os (Union[Unset, ControllerDescripHostOs]):
        pubkey (Union[Unset, str]):
        tls_pubkey (Union[Unset, str]): pulibc key of TLS certificate
        tls_key_id (Union[Unset, str]): TLS certificate key ID
        public_addresses (Union[Unset, List[str]]):
        mim_vpn_addr (Union[Unset, str]): multi-instance managment VPN address
        stats (Union[Unset, ControllerStats]):
    """

    build: Union[Unset, str] = UNSET
    api_version: Union[Unset, str] = UNSET
    host: Union[Unset, str] = UNSET
    host_os: Union[Unset, "ControllerDescripHostOs"] = UNSET
    pubkey: Union[Unset, str] = UNSET
    tls_pubkey: Union[Unset, str] = UNSET
    tls_key_id: Union[Unset, str] = UNSET
    public_addresses: Union[Unset, List[str]] = UNSET
    mim_vpn_addr: Union[Unset, str] = UNSET
    stats: Union[Unset, "ControllerStats"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        build = self.build

        api_version = self.api_version

        host = self.host

        host_os: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.host_os, Unset):
            host_os = self.host_os.to_dict()

        pubkey = self.pubkey

        tls_pubkey = self.tls_pubkey

        tls_key_id = self.tls_key_id

        public_addresses: Union[Unset, List[str]] = UNSET
        if not isinstance(self.public_addresses, Unset):
            public_addresses = self.public_addresses

        mim_vpn_addr = self.mim_vpn_addr

        stats: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if build is not UNSET:
            field_dict["build"] = build
        if api_version is not UNSET:
            field_dict["api_version"] = api_version
        if host is not UNSET:
            field_dict["host"] = host
        if host_os is not UNSET:
            field_dict["host_os"] = host_os
        if pubkey is not UNSET:
            field_dict["pubkey"] = pubkey
        if tls_pubkey is not UNSET:
            field_dict["tls_pubkey"] = tls_pubkey
        if tls_key_id is not UNSET:
            field_dict["tls_key_id"] = tls_key_id
        if public_addresses is not UNSET:
            field_dict["public_addresses"] = public_addresses
        if mim_vpn_addr is not UNSET:
            field_dict["mim_vpn_addr"] = mim_vpn_addr
        if stats is not UNSET:
            field_dict["stats"] = stats

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.controller_descrip_host_os import ControllerDescripHostOs
        from ..models.controller_stats import ControllerStats

        d = src_dict.copy()
        build = d.pop("build", UNSET)

        api_version = d.pop("api_version", UNSET)

        host = d.pop("host", UNSET)

        _host_os = d.pop("host_os", UNSET)
        host_os: Union[Unset, ControllerDescripHostOs]
        if isinstance(_host_os, Unset):
            host_os = UNSET
        else:
            host_os = ControllerDescripHostOs.from_dict(_host_os)

        pubkey = d.pop("pubkey", UNSET)

        tls_pubkey = d.pop("tls_pubkey", UNSET)

        tls_key_id = d.pop("tls_key_id", UNSET)

        public_addresses = cast(List[str], d.pop("public_addresses", UNSET))

        mim_vpn_addr = d.pop("mim_vpn_addr", UNSET)

        _stats = d.pop("stats", UNSET)
        stats: Union[Unset, ControllerStats]
        if isinstance(_stats, Unset):
            stats = UNSET
        else:
            stats = ControllerStats.from_dict(_stats)

        controller_descrip = cls(
            build=build,
            api_version=api_version,
            host=host,
            host_os=host_os,
            pubkey=pubkey,
            tls_pubkey=tls_pubkey,
            tls_key_id=tls_key_id,
            public_addresses=public_addresses,
            mim_vpn_addr=mim_vpn_addr,
            stats=stats,
        )

        controller_descrip.additional_properties = d
        return controller_descrip

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
