from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.wgip_addresses import WGIPAddresses


T = TypeVar("T", bound="WGTunnel")


@_attrs_define
class WGTunnel:
    """valid values:
    enabled = "yes", "no"

        Attributes:
            name (str):
            descr (str):
            enabled (bool):
            listenport (str):
            privatekey (str):
            publickey (str):
            mtu (str):
            addresses (WGIPAddresses):
    """

    name: str
    descr: str
    enabled: bool
    listenport: str
    privatekey: str
    publickey: str
    mtu: str
    addresses: "WGIPAddresses"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        descr = self.descr

        enabled = self.enabled

        listenport = self.listenport

        privatekey = self.privatekey

        publickey = self.publickey

        mtu = self.mtu

        addresses = self.addresses.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "descr": descr,
                "enabled": enabled,
                "listenport": listenport,
                "privatekey": privatekey,
                "publickey": publickey,
                "mtu": mtu,
                "addresses": addresses,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.wgip_addresses import WGIPAddresses

        d = src_dict.copy()
        name = d.pop("name")

        descr = d.pop("descr")

        enabled = d.pop("enabled")

        listenport = d.pop("listenport")

        privatekey = d.pop("privatekey")

        publickey = d.pop("publickey")

        mtu = d.pop("mtu")

        addresses = WGIPAddresses.from_dict(d.pop("addresses"))

        wg_tunnel = cls(
            name=name,
            descr=descr,
            enabled=enabled,
            listenport=listenport,
            privatekey=privatekey,
            publickey=publickey,
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
