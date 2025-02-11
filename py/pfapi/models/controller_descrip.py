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
        build (str):
        api_version (str):
        host (str):
        host_os (ControllerDescripHostOs):
        pubkey (str):
        tls_pubkey (str): pulibc key of TLS certificate
        tls_key_id (str): TLS certificate key ID
        mim_vpn_addr (str): multi-instance managment VPN address
        stats (ControllerStats):
        public_addresses (Union[Unset, List[str]]):
    """

    build: str
    api_version: str
    host: str
    host_os: "ControllerDescripHostOs"
    pubkey: str
    tls_pubkey: str
    tls_key_id: str
    mim_vpn_addr: str
    stats: "ControllerStats"
    public_addresses: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        build = self.build

        api_version = self.api_version

        host = self.host

        host_os = self.host_os.to_dict()

        pubkey = self.pubkey

        tls_pubkey = self.tls_pubkey

        tls_key_id = self.tls_key_id

        mim_vpn_addr = self.mim_vpn_addr

        stats = self.stats.to_dict()

        public_addresses: Union[Unset, List[str]] = UNSET
        if not isinstance(self.public_addresses, Unset):
            public_addresses = self.public_addresses

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "build": build,
                "api_version": api_version,
                "host": host,
                "host_os": host_os,
                "pubkey": pubkey,
                "tls_pubkey": tls_pubkey,
                "tls_key_id": tls_key_id,
                "mim_vpn_addr": mim_vpn_addr,
                "stats": stats,
            }
        )
        if public_addresses is not UNSET:
            field_dict["public_addresses"] = public_addresses

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.controller_descrip_host_os import ControllerDescripHostOs
        from ..models.controller_stats import ControllerStats

        d = src_dict.copy()
        build = d.pop("build")

        api_version = d.pop("api_version")

        host = d.pop("host")

        host_os = ControllerDescripHostOs.from_dict(d.pop("host_os"))

        pubkey = d.pop("pubkey")

        tls_pubkey = d.pop("tls_pubkey")

        tls_key_id = d.pop("tls_key_id")

        mim_vpn_addr = d.pop("mim_vpn_addr")

        stats = ControllerStats.from_dict(d.pop("stats"))

        public_addresses = cast(List[str], d.pop("public_addresses", UNSET))

        controller_descrip = cls(
            build=build,
            api_version=api_version,
            host=host,
            host_os=host_os,
            pubkey=pubkey,
            tls_pubkey=tls_pubkey,
            tls_key_id=tls_key_id,
            mim_vpn_addr=mim_vpn_addr,
            stats=stats,
            public_addresses=public_addresses,
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
