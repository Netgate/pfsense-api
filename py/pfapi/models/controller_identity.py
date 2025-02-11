from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ControllerIdentity")


@_attrs_define
class ControllerIdentity:
    """
    Attributes:
        name (str):
        key (str):
        cert (str):
        vpn_listenaddr (str):
        vpn_address (str):
        vpn_pubkey (str):
        vpn_netkey (str):
        vpn_prefix (str):
        oldkey (Union[Unset, str]):
        regentokens (Union[Unset, bool]):
    """

    name: str
    key: str
    cert: str
    vpn_listenaddr: str
    vpn_address: str
    vpn_pubkey: str
    vpn_netkey: str
    vpn_prefix: str
    oldkey: Union[Unset, str] = UNSET
    regentokens: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        key = self.key

        cert = self.cert

        vpn_listenaddr = self.vpn_listenaddr

        vpn_address = self.vpn_address

        vpn_pubkey = self.vpn_pubkey

        vpn_netkey = self.vpn_netkey

        vpn_prefix = self.vpn_prefix

        oldkey = self.oldkey

        regentokens = self.regentokens

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "key": key,
                "cert": cert,
                "vpn_listenaddr": vpn_listenaddr,
                "vpn_address": vpn_address,
                "vpn_pubkey": vpn_pubkey,
                "vpn_netkey": vpn_netkey,
                "vpn_prefix": vpn_prefix,
            }
        )
        if oldkey is not UNSET:
            field_dict["oldkey"] = oldkey
        if regentokens is not UNSET:
            field_dict["regentokens"] = regentokens

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        key = d.pop("key")

        cert = d.pop("cert")

        vpn_listenaddr = d.pop("vpn_listenaddr")

        vpn_address = d.pop("vpn_address")

        vpn_pubkey = d.pop("vpn_pubkey")

        vpn_netkey = d.pop("vpn_netkey")

        vpn_prefix = d.pop("vpn_prefix")

        oldkey = d.pop("oldkey", UNSET)

        regentokens = d.pop("regentokens", UNSET)

        controller_identity = cls(
            name=name,
            key=key,
            cert=cert,
            vpn_listenaddr=vpn_listenaddr,
            vpn_address=vpn_address,
            vpn_pubkey=vpn_pubkey,
            vpn_netkey=vpn_netkey,
            vpn_prefix=vpn_prefix,
            oldkey=oldkey,
            regentokens=regentokens,
        )

        controller_identity.additional_properties = d
        return controller_identity

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
