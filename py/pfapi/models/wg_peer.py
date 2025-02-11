from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.wgip_addresses import WGIPAddresses


T = TypeVar("T", bound="WGPeer")


@_attrs_define
class WGPeer:
    """valid values:
    enabled = "yes", "no"

        Attributes:
            enabled (bool):
            tun (str):
            descr (str):
            endpoint (str):
            port (str):
            persistentkeepalive (str):
            publickey (str):
            presharedkey (str):
            allowedips (WGIPAddresses):
    """

    enabled: bool
    tun: str
    descr: str
    endpoint: str
    port: str
    persistentkeepalive: str
    publickey: str
    presharedkey: str
    allowedips: "WGIPAddresses"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled

        tun = self.tun

        descr = self.descr

        endpoint = self.endpoint

        port = self.port

        persistentkeepalive = self.persistentkeepalive

        publickey = self.publickey

        presharedkey = self.presharedkey

        allowedips = self.allowedips.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "tun": tun,
                "descr": descr,
                "endpoint": endpoint,
                "port": port,
                "persistentkeepalive": persistentkeepalive,
                "publickey": publickey,
                "presharedkey": presharedkey,
                "allowedips": allowedips,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.wgip_addresses import WGIPAddresses

        d = src_dict.copy()
        enabled = d.pop("enabled")

        tun = d.pop("tun")

        descr = d.pop("descr")

        endpoint = d.pop("endpoint")

        port = d.pop("port")

        persistentkeepalive = d.pop("persistentkeepalive")

        publickey = d.pop("publickey")

        presharedkey = d.pop("presharedkey")

        allowedips = WGIPAddresses.from_dict(d.pop("allowedips"))

        wg_peer = cls(
            enabled=enabled,
            tun=tun,
            descr=descr,
            endpoint=endpoint,
            port=port,
            persistentkeepalive=persistentkeepalive,
            publickey=publickey,
            presharedkey=presharedkey,
            allowedips=allowedips,
        )

        wg_peer.additional_properties = d
        return wg_peer

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
