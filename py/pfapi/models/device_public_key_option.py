from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DevicePublicKeyOption")


@_attrs_define
class DevicePublicKeyOption:
    """
    Attributes:
        keytype (Union[Unset, str]):
        privkey (Union[Unset, str]):
        pubkey (Union[Unset, str]):
    """

    keytype: Union[Unset, str] = UNSET
    privkey: Union[Unset, str] = UNSET
    pubkey: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        keytype = self.keytype

        privkey = self.privkey

        pubkey = self.pubkey

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if keytype is not UNSET:
            field_dict["keytype"] = keytype
        if privkey is not UNSET:
            field_dict["privkey"] = privkey
        if pubkey is not UNSET:
            field_dict["pubkey"] = pubkey

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        keytype = d.pop("keytype", UNSET)

        privkey = d.pop("privkey", UNSET)

        pubkey = d.pop("pubkey", UNSET)

        device_public_key_option = cls(
            keytype=keytype,
            privkey=privkey,
            pubkey=pubkey,
        )

        device_public_key_option.additional_properties = d
        return device_public_key_option

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
