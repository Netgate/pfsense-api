from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetupDNSSetting")


@_attrs_define
class SetupDNSSetting:
    """
    Attributes:
        name (Union[Unset, str]):
        ip (Union[Unset, str]):
        gw (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    ip: Union[Unset, str] = UNSET
    gw: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        ip = self.ip

        gw = self.gw

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if ip is not UNSET:
            field_dict["ip"] = ip
        if gw is not UNSET:
            field_dict["gw"] = gw

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        ip = d.pop("ip", UNSET)

        gw = d.pop("gw", UNSET)

        setup_dns_setting = cls(
            name=name,
            ip=ip,
            gw=gw,
        )

        setup_dns_setting.additional_properties = d
        return setup_dns_setting

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
