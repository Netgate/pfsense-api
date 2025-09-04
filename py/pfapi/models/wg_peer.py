from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wgip_address import WGIPAddress


T = TypeVar("T", bound="WGPeer")


@_attrs_define
class WGPeer:
    """valid values:
    enabled = "yes", "no"

        Attributes:
            publickey (str):
            enabled (Union[Unset, bool]):
            tun (Union[Unset, str]):
            descr (Union[Unset, str]):
            endpoint (Union[Unset, str]):
            port (Union[Unset, str]):
            persistentkeepalive (Union[Unset, str]):
            presharedkey (Union[Unset, str]):
            allowedips (Union[Unset, List['WGIPAddress']]):
    """

    publickey: str
    enabled: Union[Unset, bool] = UNSET
    tun: Union[Unset, str] = UNSET
    descr: Union[Unset, str] = UNSET
    endpoint: Union[Unset, str] = UNSET
    port: Union[Unset, str] = UNSET
    persistentkeepalive: Union[Unset, str] = UNSET
    presharedkey: Union[Unset, str] = UNSET
    allowedips: Union[Unset, List["WGIPAddress"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        publickey = self.publickey

        enabled = self.enabled

        tun = self.tun

        descr = self.descr

        endpoint = self.endpoint

        port = self.port

        persistentkeepalive = self.persistentkeepalive

        presharedkey = self.presharedkey

        allowedips: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.allowedips, Unset):
            allowedips = []
            for allowedips_item_data in self.allowedips:
                allowedips_item = allowedips_item_data.to_dict()
                allowedips.append(allowedips_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "publickey": publickey,
            }
        )
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
        if presharedkey is not UNSET:
            field_dict["presharedkey"] = presharedkey
        if allowedips is not UNSET:
            field_dict["allowedips"] = allowedips

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.wgip_address import WGIPAddress

        d = src_dict.copy()
        publickey = d.pop("publickey")

        enabled = d.pop("enabled", UNSET)

        tun = d.pop("tun", UNSET)

        descr = d.pop("descr", UNSET)

        endpoint = d.pop("endpoint", UNSET)

        port = d.pop("port", UNSET)

        persistentkeepalive = d.pop("persistentkeepalive", UNSET)

        presharedkey = d.pop("presharedkey", UNSET)

        allowedips = []
        _allowedips = d.pop("allowedips", UNSET)
        for allowedips_item_data in _allowedips or []:
            allowedips_item = WGIPAddress.from_dict(allowedips_item_data)

            allowedips.append(allowedips_item)

        wg_peer = cls(
            publickey=publickey,
            enabled=enabled,
            tun=tun,
            descr=descr,
            endpoint=endpoint,
            port=port,
            persistentkeepalive=persistentkeepalive,
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
