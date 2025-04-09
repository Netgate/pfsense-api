from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fw_user_timestamp import FWUserTimestamp
    from ..models.nat_addr_port import NATAddrPort


T = TypeVar("T", bound="NATOutboundRule")


@_attrs_define
class NATOutboundRule:
    """
    Attributes:
        created (Union[Unset, FWUserTimestamp]):
        descr (Union[Unset, str]):
        disabled (Union[Unset, bool]):
        destination (Union[Unset, NATAddrPort]):
        id (Union[Unset, str]):
        interface (Union[Unset, str]):
        ipprotocol (Union[Unset, str]):
        nonat (Union[Unset, bool]):
        nosync (Union[Unset, bool]):
        protocol (Union[Unset, str]):
        poolopts (Union[Unset, str]):
        source (Union[Unset, NATAddrPort]):
        source_hash_key (Union[Unset, str]):
        staticnatport (Union[Unset, bool]):
        target (Union[Unset, NATAddrPort]):
        updated (Union[Unset, FWUserTimestamp]):
    """

    created: Union[Unset, "FWUserTimestamp"] = UNSET
    descr: Union[Unset, str] = UNSET
    disabled: Union[Unset, bool] = UNSET
    destination: Union[Unset, "NATAddrPort"] = UNSET
    id: Union[Unset, str] = UNSET
    interface: Union[Unset, str] = UNSET
    ipprotocol: Union[Unset, str] = UNSET
    nonat: Union[Unset, bool] = UNSET
    nosync: Union[Unset, bool] = UNSET
    protocol: Union[Unset, str] = UNSET
    poolopts: Union[Unset, str] = UNSET
    source: Union[Unset, "NATAddrPort"] = UNSET
    source_hash_key: Union[Unset, str] = UNSET
    staticnatport: Union[Unset, bool] = UNSET
    target: Union[Unset, "NATAddrPort"] = UNSET
    updated: Union[Unset, "FWUserTimestamp"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.to_dict()

        descr = self.descr

        disabled = self.disabled

        destination: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.destination, Unset):
            destination = self.destination.to_dict()

        id = self.id

        interface = self.interface

        ipprotocol = self.ipprotocol

        nonat = self.nonat

        nosync = self.nosync

        protocol = self.protocol

        poolopts = self.poolopts

        source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        source_hash_key = self.source_hash_key

        staticnatport = self.staticnatport

        target: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.target, Unset):
            target = self.target.to_dict()

        updated: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if descr is not UNSET:
            field_dict["descr"] = descr
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if destination is not UNSET:
            field_dict["destination"] = destination
        if id is not UNSET:
            field_dict["id"] = id
        if interface is not UNSET:
            field_dict["interface"] = interface
        if ipprotocol is not UNSET:
            field_dict["ipprotocol"] = ipprotocol
        if nonat is not UNSET:
            field_dict["nonat"] = nonat
        if nosync is not UNSET:
            field_dict["nosync"] = nosync
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if poolopts is not UNSET:
            field_dict["poolopts"] = poolopts
        if source is not UNSET:
            field_dict["source"] = source
        if source_hash_key is not UNSET:
            field_dict["source-hash-key"] = source_hash_key
        if staticnatport is not UNSET:
            field_dict["staticnatport"] = staticnatport
        if target is not UNSET:
            field_dict["target"] = target
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fw_user_timestamp import FWUserTimestamp
        from ..models.nat_addr_port import NATAddrPort

        d = src_dict.copy()
        _created = d.pop("created", UNSET)
        created: Union[Unset, FWUserTimestamp]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = FWUserTimestamp.from_dict(_created)

        descr = d.pop("descr", UNSET)

        disabled = d.pop("disabled", UNSET)

        _destination = d.pop("destination", UNSET)
        destination: Union[Unset, NATAddrPort]
        if isinstance(_destination, Unset):
            destination = UNSET
        else:
            destination = NATAddrPort.from_dict(_destination)

        id = d.pop("id", UNSET)

        interface = d.pop("interface", UNSET)

        ipprotocol = d.pop("ipprotocol", UNSET)

        nonat = d.pop("nonat", UNSET)

        nosync = d.pop("nosync", UNSET)

        protocol = d.pop("protocol", UNSET)

        poolopts = d.pop("poolopts", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, NATAddrPort]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = NATAddrPort.from_dict(_source)

        source_hash_key = d.pop("source-hash-key", UNSET)

        staticnatport = d.pop("staticnatport", UNSET)

        _target = d.pop("target", UNSET)
        target: Union[Unset, NATAddrPort]
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = NATAddrPort.from_dict(_target)

        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, FWUserTimestamp]
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = FWUserTimestamp.from_dict(_updated)

        nat_outbound_rule = cls(
            created=created,
            descr=descr,
            disabled=disabled,
            destination=destination,
            id=id,
            interface=interface,
            ipprotocol=ipprotocol,
            nonat=nonat,
            nosync=nosync,
            protocol=protocol,
            poolopts=poolopts,
            source=source,
            source_hash_key=source_hash_key,
            staticnatport=staticnatport,
            target=target,
            updated=updated,
        )

        nat_outbound_rule.additional_properties = d
        return nat_outbound_rule

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
