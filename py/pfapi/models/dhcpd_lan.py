from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dhcp_range import DhcpRange


T = TypeVar("T", bound="DhcpdLan")


@_attrs_define
class DhcpdLan:
    """
    Attributes:
        text (str | Unset):
        enable (str | Unset):
        range_ (DhcpRange | Unset):
    """

    text: str | Unset = UNSET
    enable: str | Unset = UNSET
    range_: DhcpRange | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        enable = self.enable

        range_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.range_, Unset):
            range_ = self.range_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if text is not UNSET:
            field_dict["text"] = text
        if enable is not UNSET:
            field_dict["enable"] = enable
        if range_ is not UNSET:
            field_dict["range"] = range_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dhcp_range import DhcpRange

        d = dict(src_dict)
        text = d.pop("text", UNSET)

        enable = d.pop("enable", UNSET)

        _range_ = d.pop("range", UNSET)
        range_: DhcpRange | Unset
        if isinstance(_range_, Unset):
            range_ = UNSET
        else:
            range_ = DhcpRange.from_dict(_range_)

        dhcpd_lan = cls(
            text=text,
            enable=enable,
            range_=range_,
        )

        dhcpd_lan.additional_properties = d
        return dhcpd_lan

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
