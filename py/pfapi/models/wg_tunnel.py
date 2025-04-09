from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wgip_addresses import WGIPAddresses


T = TypeVar("T", bound="WGTunnel")


@_attrs_define
class WGTunnel:
    """valid values:
    enabled = "yes", "no"

        Attributes:
            name (str):
            privatekey (str):
            publickey (str):
            descr (Union[Unset, str]):
            enabled (Union[Unset, bool]):
            listenport (Union[Unset, int]):
            mtu (Union[Unset, str]):
            addresses (Union[Unset, WGIPAddresses]):
    """

    name: str
    privatekey: str
    publickey: str
    descr: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    listenport: Union[Unset, int] = UNSET
    mtu: Union[Unset, str] = UNSET
    addresses: Union[Unset, "WGIPAddresses"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        privatekey = self.privatekey

        publickey = self.publickey

        descr = self.descr

        enabled = self.enabled

        listenport = self.listenport

        mtu = self.mtu

        addresses: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.addresses, Unset):
            addresses = self.addresses.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "privatekey": privatekey,
                "publickey": publickey,
            }
        )
        if descr is not UNSET:
            field_dict["descr"] = descr
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if listenport is not UNSET:
            field_dict["listenport"] = listenport
        if mtu is not UNSET:
            field_dict["mtu"] = mtu
        if addresses is not UNSET:
            field_dict["addresses"] = addresses

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.wgip_addresses import WGIPAddresses

        d = src_dict.copy()
        name = d.pop("name")

        privatekey = d.pop("privatekey")

        publickey = d.pop("publickey")

        descr = d.pop("descr", UNSET)

        enabled = d.pop("enabled", UNSET)

        listenport = d.pop("listenport", UNSET)

        mtu = d.pop("mtu", UNSET)

        _addresses = d.pop("addresses", UNSET)
        addresses: Union[Unset, WGIPAddresses]
        if isinstance(_addresses, Unset):
            addresses = UNSET
        else:
            addresses = WGIPAddresses.from_dict(_addresses)

        wg_tunnel = cls(
            name=name,
            privatekey=privatekey,
            publickey=publickey,
            descr=descr,
            enabled=enabled,
            listenport=listenport,
            mtu=mtu,
            addresses=addresses,
        )

        wg_tunnel.additional_properties = d
        return wg_tunnel

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
