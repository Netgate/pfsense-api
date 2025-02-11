from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IPSecMobileKey")


@_attrs_define
class IPSecMobileKey:
    """
    Attributes:
        ident (str):
        type (str):
        pre_shared_key (str):
        ident_type (str):
        pool_address (str):
        pool_netbits (str):
        dns_address (str):
    """

    ident: str
    type: str
    pre_shared_key: str
    ident_type: str
    pool_address: str
    pool_netbits: str
    dns_address: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ident = self.ident

        type = self.type

        pre_shared_key = self.pre_shared_key

        ident_type = self.ident_type

        pool_address = self.pool_address

        pool_netbits = self.pool_netbits

        dns_address = self.dns_address

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ident": ident,
                "type": type,
                "pre_shared_key": pre_shared_key,
                "ident_type": ident_type,
                "pool_address": pool_address,
                "pool_netbits": pool_netbits,
                "dns_address": dns_address,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ident = d.pop("ident")

        type = d.pop("type")

        pre_shared_key = d.pop("pre_shared_key")

        ident_type = d.pop("ident_type")

        pool_address = d.pop("pool_address")

        pool_netbits = d.pop("pool_netbits")

        dns_address = d.pop("dns_address")

        ip_sec_mobile_key = cls(
            ident=ident,
            type=type,
            pre_shared_key=pre_shared_key,
            ident_type=ident_type,
            pool_address=pool_address,
            pool_netbits=pool_netbits,
            dns_address=dns_address,
        )

        ip_sec_mobile_key.additional_properties = d
        return ip_sec_mobile_key

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
