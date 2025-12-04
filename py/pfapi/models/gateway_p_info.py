from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gateway_v_address import GatewayVAddress


T = TypeVar("T", bound="GatewayPInfo")


@_attrs_define
class GatewayPInfo:
    """
    Attributes:
        name (str):
        gateway (str): gateway address
        vaddress (list[GatewayVAddress] | Unset):
        descr (str | Unset):
        ipprotocol (str | Unset): inet or inet6
    """

    name: str
    gateway: str
    vaddress: list[GatewayVAddress] | Unset = UNSET
    descr: str | Unset = UNSET
    ipprotocol: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        gateway = self.gateway

        vaddress: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.vaddress, Unset):
            vaddress = []
            for vaddress_item_data in self.vaddress:
                vaddress_item = vaddress_item_data.to_dict()
                vaddress.append(vaddress_item)

        descr = self.descr

        ipprotocol = self.ipprotocol

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "gateway": gateway,
            }
        )
        if vaddress is not UNSET:
            field_dict["vaddress"] = vaddress
        if descr is not UNSET:
            field_dict["descr"] = descr
        if ipprotocol is not UNSET:
            field_dict["ipprotocol"] = ipprotocol

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gateway_v_address import GatewayVAddress

        d = dict(src_dict)
        name = d.pop("name")

        gateway = d.pop("gateway")

        _vaddress = d.pop("vaddress", UNSET)
        vaddress: list[GatewayVAddress] | Unset = UNSET
        if _vaddress is not UNSET:
            vaddress = []
            for vaddress_item_data in _vaddress:
                vaddress_item = GatewayVAddress.from_dict(vaddress_item_data)

                vaddress.append(vaddress_item)

        descr = d.pop("descr", UNSET)

        ipprotocol = d.pop("ipprotocol", UNSET)

        gateway_p_info = cls(
            name=name,
            gateway=gateway,
            vaddress=vaddress,
            descr=descr,
            ipprotocol=ipprotocol,
        )

        gateway_p_info.additional_properties = d
        return gateway_p_info

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
