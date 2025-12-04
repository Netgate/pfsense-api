from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ha_pfsync import HAPfsync
    from ..models.haxmlrpc_sync import HAXMLRPCSync


T = TypeVar("T", bound="HASyncOpts")


@_attrs_define
class HASyncOpts:
    """
    Attributes:
        pfsync (HAPfsync | Unset):
        xmlrpc (HAXMLRPCSync | Unset):
        avail_sync_interfaces (list[str] | Unset):
    """

    pfsync: HAPfsync | Unset = UNSET
    xmlrpc: HAXMLRPCSync | Unset = UNSET
    avail_sync_interfaces: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pfsync: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pfsync, Unset):
            pfsync = self.pfsync.to_dict()

        xmlrpc: dict[str, Any] | Unset = UNSET
        if not isinstance(self.xmlrpc, Unset):
            xmlrpc = self.xmlrpc.to_dict()

        avail_sync_interfaces: list[str] | Unset = UNSET
        if not isinstance(self.avail_sync_interfaces, Unset):
            avail_sync_interfaces = self.avail_sync_interfaces

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pfsync is not UNSET:
            field_dict["pfsync"] = pfsync
        if xmlrpc is not UNSET:
            field_dict["xmlrpc"] = xmlrpc
        if avail_sync_interfaces is not UNSET:
            field_dict["avail_sync_interfaces"] = avail_sync_interfaces

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ha_pfsync import HAPfsync
        from ..models.haxmlrpc_sync import HAXMLRPCSync

        d = dict(src_dict)
        _pfsync = d.pop("pfsync", UNSET)
        pfsync: HAPfsync | Unset
        if isinstance(_pfsync, Unset):
            pfsync = UNSET
        else:
            pfsync = HAPfsync.from_dict(_pfsync)

        _xmlrpc = d.pop("xmlrpc", UNSET)
        xmlrpc: HAXMLRPCSync | Unset
        if isinstance(_xmlrpc, Unset):
            xmlrpc = UNSET
        else:
            xmlrpc = HAXMLRPCSync.from_dict(_xmlrpc)

        avail_sync_interfaces = cast(list[str], d.pop("avail_sync_interfaces", UNSET))

        ha_sync_opts = cls(
            pfsync=pfsync,
            xmlrpc=xmlrpc,
            avail_sync_interfaces=avail_sync_interfaces,
        )

        ha_sync_opts.additional_properties = d
        return ha_sync_opts

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
