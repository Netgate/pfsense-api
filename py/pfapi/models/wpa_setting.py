from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WPASetting")


@_attrs_define
class WPASetting:
    """
    Attributes:
        macaddr_acl (str):
        wpa_mode (str):
        wpa_key_mgmt (str):
        wpa_pairwise (str):
        wpa_group_rekey (str):
        wpa_gmk_rekey (str):
        passphrase (str):
        ext_wpa_sw (str):
    """

    macaddr_acl: str
    wpa_mode: str
    wpa_key_mgmt: str
    wpa_pairwise: str
    wpa_group_rekey: str
    wpa_gmk_rekey: str
    passphrase: str
    ext_wpa_sw: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        macaddr_acl = self.macaddr_acl

        wpa_mode = self.wpa_mode

        wpa_key_mgmt = self.wpa_key_mgmt

        wpa_pairwise = self.wpa_pairwise

        wpa_group_rekey = self.wpa_group_rekey

        wpa_gmk_rekey = self.wpa_gmk_rekey

        passphrase = self.passphrase

        ext_wpa_sw = self.ext_wpa_sw

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "macaddr_acl": macaddr_acl,
                "wpa_mode": wpa_mode,
                "wpa_key_mgmt": wpa_key_mgmt,
                "wpa_pairwise": wpa_pairwise,
                "wpa_group_rekey": wpa_group_rekey,
                "wpa_gmk_rekey": wpa_gmk_rekey,
                "passphrase": passphrase,
                "ext_wpa_sw": ext_wpa_sw,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        macaddr_acl = d.pop("macaddr_acl")

        wpa_mode = d.pop("wpa_mode")

        wpa_key_mgmt = d.pop("wpa_key_mgmt")

        wpa_pairwise = d.pop("wpa_pairwise")

        wpa_group_rekey = d.pop("wpa_group_rekey")

        wpa_gmk_rekey = d.pop("wpa_gmk_rekey")

        passphrase = d.pop("passphrase")

        ext_wpa_sw = d.pop("ext_wpa_sw")

        wpa_setting = cls(
            macaddr_acl=macaddr_acl,
            wpa_mode=wpa_mode,
            wpa_key_mgmt=wpa_key_mgmt,
            wpa_pairwise=wpa_pairwise,
            wpa_group_rekey=wpa_group_rekey,
            wpa_gmk_rekey=wpa_gmk_rekey,
            passphrase=passphrase,
            ext_wpa_sw=ext_wpa_sw,
        )

        wpa_setting.additional_properties = d
        return wpa_setting

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
