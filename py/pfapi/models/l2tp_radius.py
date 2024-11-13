from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="L2TPRadius")


@_attrs_define
class L2TPRadius:
    """
    Attributes:
        server (Union[Unset, str]):
        secret (Union[Unset, str]):
        enable (Union[Unset, bool]):
        accounting (Union[Unset, bool]):
        radiusissueips (Union[Unset, bool]):
    """

    server: Union[Unset, str] = UNSET
    secret: Union[Unset, str] = UNSET
    enable: Union[Unset, bool] = UNSET
    accounting: Union[Unset, bool] = UNSET
    radiusissueips: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        server = self.server

        secret = self.secret

        enable = self.enable

        accounting = self.accounting

        radiusissueips = self.radiusissueips

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if server is not UNSET:
            field_dict["server"] = server
        if secret is not UNSET:
            field_dict["secret"] = secret
        if enable is not UNSET:
            field_dict["enable"] = enable
        if accounting is not UNSET:
            field_dict["accounting"] = accounting
        if radiusissueips is not UNSET:
            field_dict["radiusissueips"] = radiusissueips

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        server = d.pop("server", UNSET)

        secret = d.pop("secret", UNSET)

        enable = d.pop("enable", UNSET)

        accounting = d.pop("accounting", UNSET)

        radiusissueips = d.pop("radiusissueips", UNSET)

        l2tp_radius = cls(
            server=server,
            secret=secret,
            enable=enable,
            accounting=accounting,
            radiusissueips=radiusissueips,
        )

        l2tp_radius.additional_properties = d
        return l2tp_radius

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
