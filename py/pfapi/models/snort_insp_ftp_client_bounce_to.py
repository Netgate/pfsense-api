from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortInspFtpClientBounceTo")


@_attrs_define
class SnortInspFtpClientBounceTo:
    """
    Attributes:
        address (str | Unset): allowed IP address in CIDR format; default 1.0.0.0/32
        port (int | Unset): allowed port; default 20
        last_port (int | Unset): optional allowed range from port to last_port inclusive
    """

    address: str | Unset = UNSET
    port: int | Unset = UNSET
    last_port: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        port = self.port

        last_port = self.last_port

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if port is not UNSET:
            field_dict["port"] = port
        if last_port is not UNSET:
            field_dict["last_port"] = last_port

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address = d.pop("address", UNSET)

        port = d.pop("port", UNSET)

        last_port = d.pop("last_port", UNSET)

        snort_insp_ftp_client_bounce_to = cls(
            address=address,
            port=port,
            last_port=last_port,
        )

        snort_insp_ftp_client_bounce_to.additional_properties = d
        return snort_insp_ftp_client_bounce_to

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
