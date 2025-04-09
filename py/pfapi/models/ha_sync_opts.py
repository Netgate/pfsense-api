from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

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
        pfsync (Union[Unset, HAPfsync]):
        xmlrpc (Union[Unset, HAXMLRPCSync]):
        avail_sync_interfaces (Union[Unset, List[str]]):
    """

    pfsync: Union[Unset, "HAPfsync"] = UNSET
    xmlrpc: Union[Unset, "HAXMLRPCSync"] = UNSET
    avail_sync_interfaces: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pfsync: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pfsync, Unset):
            pfsync = self.pfsync.to_dict()

        xmlrpc: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.xmlrpc, Unset):
            xmlrpc = self.xmlrpc.to_dict()

        avail_sync_interfaces: Union[Unset, List[str]] = UNSET
        if not isinstance(self.avail_sync_interfaces, Unset):
            avail_sync_interfaces = self.avail_sync_interfaces

        field_dict: Dict[str, Any] = {}
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ha_pfsync import HAPfsync
        from ..models.haxmlrpc_sync import HAXMLRPCSync

        d = src_dict.copy()
        _pfsync = d.pop("pfsync", UNSET)
        pfsync: Union[Unset, HAPfsync]
        if isinstance(_pfsync, Unset):
            pfsync = UNSET
        else:
            pfsync = HAPfsync.from_dict(_pfsync)

        _xmlrpc = d.pop("xmlrpc", UNSET)
        xmlrpc: Union[Unset, HAXMLRPCSync]
        if isinstance(_xmlrpc, Unset):
            xmlrpc = UNSET
        else:
            xmlrpc = HAXMLRPCSync.from_dict(_xmlrpc)

        avail_sync_interfaces = cast(List[str], d.pop("avail_sync_interfaces", UNSET))

        ha_sync_opts = cls(
            pfsync=pfsync,
            xmlrpc=xmlrpc,
            avail_sync_interfaces=avail_sync_interfaces,
        )

        ha_sync_opts.additional_properties = d
        return ha_sync_opts

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
