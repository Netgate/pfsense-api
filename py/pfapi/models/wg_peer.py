from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wgip_addresses import WGIPAddresses


T = TypeVar("T", bound="WGPeer")


@_attrs_define
class WGPeer:
    """valid values:
    enabled = "yes", "no"

        Attributes:
            enabled (Union[Unset, bool]):
            tun (Union[Unset, str]):
            descr (Union[Unset, str]):
            endpoint (Union[Unset, str]):
            port (Union[Unset, str]):
            persistentkeepalive (Union[Unset, str]):
            publickey (Union[Unset, str]):
            presharedkey (Union[Unset, str]):
            allowedips (Union[Unset, WGIPAddresses]):
    """

    enabled: Union[Unset, bool] = UNSET
    tun: Union[Unset, str] = UNSET
    descr: Union[Unset, str] = UNSET
    endpoint: Union[Unset, str] = UNSET
    port: Union[Unset, str] = UNSET
    persistentkeepalive: Union[Unset, str] = UNSET
    publickey: Union[Unset, str] = UNSET
    presharedkey: Union[Unset, str] = UNSET
    allowedips: Union[Unset, "WGIPAddresses"] = UNSET
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

        allowedips: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.allowedips, Unset):
            allowedips = self.allowedips.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if tun is not UNSET:
            field_dict["tun"] = tun
        if descr is not UNSET:
            field_dict["descr"] = descr
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if port is not UNSET:
            field_dict["port"] = port
        if persistentkeepalive is not UNSET:
            field_dict["persistentkeepalive"] = persistentkeepalive
        if publickey is not UNSET:
            field_dict["publickey"] = publickey
        if presharedkey is not UNSET:
            field_dict["presharedkey"] = presharedkey
        if allowedips is not UNSET:
            field_dict["allowedips"] = allowedips

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.wgip_addresses import WGIPAddresses

        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        tun = d.pop("tun", UNSET)

        descr = d.pop("descr", UNSET)

        endpoint = d.pop("endpoint", UNSET)

        port = d.pop("port", UNSET)

        persistentkeepalive = d.pop("persistentkeepalive", UNSET)

        publickey = d.pop("publickey", UNSET)

        presharedkey = d.pop("presharedkey", UNSET)

        _allowedips = d.pop("allowedips", UNSET)
        allowedips: Union[Unset, WGIPAddresses]
        if isinstance(_allowedips, Unset):
            allowedips = UNSET
        else:
            allowedips = WGIPAddresses.from_dict(_allowedips)

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
