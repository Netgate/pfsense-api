from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VXLANInterface")


@_attrs_define
class VXLANInterface:
    """
    Attributes:
        if_device (str):
        remote_addr (str | Unset):
        ttl (int | Unset):
        id (int | Unset):
        local_port (int | Unset):
        remote_port (int | Unset):
        learn (bool | Unset):
        descr (str | Unset):
        vxlanif (str | Unset):
    """

    if_device: str
    remote_addr: str | Unset = UNSET
    ttl: int | Unset = UNSET
    id: int | Unset = UNSET
    local_port: int | Unset = UNSET
    remote_port: int | Unset = UNSET
    learn: bool | Unset = UNSET
    descr: str | Unset = UNSET
    vxlanif: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        if_device = self.if_device

        remote_addr = self.remote_addr

        ttl = self.ttl

        id = self.id

        local_port = self.local_port

        remote_port = self.remote_port

        learn = self.learn

        descr = self.descr

        vxlanif = self.vxlanif

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "if_device": if_device,
            }
        )
        if remote_addr is not UNSET:
            field_dict["remote_addr"] = remote_addr
        if ttl is not UNSET:
            field_dict["ttl"] = ttl
        if id is not UNSET:
            field_dict["id"] = id
        if local_port is not UNSET:
            field_dict["local_port"] = local_port
        if remote_port is not UNSET:
            field_dict["remote_port"] = remote_port
        if learn is not UNSET:
            field_dict["learn"] = learn
        if descr is not UNSET:
            field_dict["descr"] = descr
        if vxlanif is not UNSET:
            field_dict["vxlanif"] = vxlanif

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        if_device = d.pop("if_device")

        remote_addr = d.pop("remote_addr", UNSET)

        ttl = d.pop("ttl", UNSET)

        id = d.pop("id", UNSET)

        local_port = d.pop("local_port", UNSET)

        remote_port = d.pop("remote_port", UNSET)

        learn = d.pop("learn", UNSET)

        descr = d.pop("descr", UNSET)

        vxlanif = d.pop("vxlanif", UNSET)

        vxlan_interface = cls(
            if_device=if_device,
            remote_addr=remote_addr,
            ttl=ttl,
            id=id,
            local_port=local_port,
            remote_port=remote_port,
            learn=learn,
            descr=descr,
            vxlanif=vxlanif,
        )

        vxlan_interface.additional_properties = d
        return vxlan_interface

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
