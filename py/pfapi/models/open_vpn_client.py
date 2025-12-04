from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_vpn_client_config import OpenVPNClientConfig


T = TypeVar("T", bound="OpenVPNClient")


@_attrs_define
class OpenVPNClient:
    """
    Attributes:
        client (OpenVPNClientConfig | Unset):
    """

    client: OpenVPNClientConfig | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client: dict[str, Any] | Unset = UNSET
        if not isinstance(self.client, Unset):
            client = self.client.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client is not UNSET:
            field_dict["client"] = client

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.open_vpn_client_config import OpenVPNClientConfig

        d = dict(src_dict)
        _client = d.pop("client", UNSET)
        client: OpenVPNClientConfig | Unset
        if isinstance(_client, Unset):
            client = UNSET
        else:
            client = OpenVPNClientConfig.from_dict(_client)

        open_vpn_client = cls(
            client=client,
        )

        open_vpn_client.additional_properties = d
        return open_vpn_client

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
