from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fw_addr_port import FWAddrPort
    from ..models.fw_user_timestamp import FWUserTimestamp


T = TypeVar("T", bound="NATOutboundRule")


@_attrs_define
class NATOutboundRule:
    """
    Attributes:
        after (Union[Unset, str]):
        created (Union[Unset, FWUserTimestamp]):
        descr (Union[Unset, str]):
        disabled (Union[Unset, bool]):
        destination (Union[Unset, FWAddrPort]):
        dst (Union[Unset, str]):
        dstport (Union[Unset, str]):
        dstmask (Union[Unset, str]):
        destination_type (Union[Unset, str]):
        dup (Union[Unset, str]):
        idx (Union[Unset, int]):
        interface (Union[Unset, str]):
        ipprotocol (Union[Unset, str]):
        natport (Union[Unset, str]):
        nosync (Union[Unset, bool]):
        protocol (Union[Unset, str]):
        source (Union[Unset, FWAddrPort]):
        src (Union[Unset, str]):
        sourceport (Union[Unset, str]):
        srcmask (Union[Unset, str]):
        srcnot (Union[Unset, bool]):
        source_type (Union[Unset, str]):
        target (Union[Unset, str]):
        targetip (Union[Unset, str]):
        targetip_subnet (Union[Unset, str]):
        updated (Union[Unset, FWUserTimestamp]):
    """

    after: Union[Unset, str] = UNSET
    created: Union[Unset, "FWUserTimestamp"] = UNSET
    descr: Union[Unset, str] = UNSET
    disabled: Union[Unset, bool] = UNSET
    destination: Union[Unset, "FWAddrPort"] = UNSET
    dst: Union[Unset, str] = UNSET
    dstport: Union[Unset, str] = UNSET
    dstmask: Union[Unset, str] = UNSET
    destination_type: Union[Unset, str] = UNSET
    dup: Union[Unset, str] = UNSET
    idx: Union[Unset, int] = UNSET
    interface: Union[Unset, str] = UNSET
    ipprotocol: Union[Unset, str] = UNSET
    natport: Union[Unset, str] = UNSET
    nosync: Union[Unset, bool] = UNSET
    protocol: Union[Unset, str] = UNSET
    source: Union[Unset, "FWAddrPort"] = UNSET
    src: Union[Unset, str] = UNSET
    sourceport: Union[Unset, str] = UNSET
    srcmask: Union[Unset, str] = UNSET
    srcnot: Union[Unset, bool] = UNSET
    source_type: Union[Unset, str] = UNSET
    target: Union[Unset, str] = UNSET
    targetip: Union[Unset, str] = UNSET
    targetip_subnet: Union[Unset, str] = UNSET
    updated: Union[Unset, "FWUserTimestamp"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        after = self.after

        created: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.to_dict()

        descr = self.descr

        disabled = self.disabled

        destination: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.destination, Unset):
            destination = self.destination.to_dict()

        dst = self.dst

        dstport = self.dstport

        dstmask = self.dstmask

        destination_type = self.destination_type

        dup = self.dup

        idx = self.idx

        interface = self.interface

        ipprotocol = self.ipprotocol

        natport = self.natport

        nosync = self.nosync

        protocol = self.protocol

        source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        src = self.src

        sourceport = self.sourceport

        srcmask = self.srcmask

        srcnot = self.srcnot

        source_type = self.source_type

        target = self.target

        targetip = self.targetip

        targetip_subnet = self.targetip_subnet

        updated: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if after is not UNSET:
            field_dict["after"] = after
        if created is not UNSET:
            field_dict["created"] = created
        if descr is not UNSET:
            field_dict["descr"] = descr
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if destination is not UNSET:
            field_dict["destination"] = destination
        if dst is not UNSET:
            field_dict["dst"] = dst
        if dstport is not UNSET:
            field_dict["dstport"] = dstport
        if dstmask is not UNSET:
            field_dict["dstmask"] = dstmask
        if destination_type is not UNSET:
            field_dict["destination_type"] = destination_type
        if dup is not UNSET:
            field_dict["dup"] = dup
        if idx is not UNSET:
            field_dict["idx"] = idx
        if interface is not UNSET:
            field_dict["interface"] = interface
        if ipprotocol is not UNSET:
            field_dict["ipprotocol"] = ipprotocol
        if natport is not UNSET:
            field_dict["natport"] = natport
        if nosync is not UNSET:
            field_dict["nosync"] = nosync
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if source is not UNSET:
            field_dict["source"] = source
        if src is not UNSET:
            field_dict["src"] = src
        if sourceport is not UNSET:
            field_dict["sourceport"] = sourceport
        if srcmask is not UNSET:
            field_dict["srcmask"] = srcmask
        if srcnot is not UNSET:
            field_dict["srcnot"] = srcnot
        if source_type is not UNSET:
            field_dict["source_type"] = source_type
        if target is not UNSET:
            field_dict["target"] = target
        if targetip is not UNSET:
            field_dict["targetip"] = targetip
        if targetip_subnet is not UNSET:
            field_dict["targetip_subnet"] = targetip_subnet
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fw_addr_port import FWAddrPort
        from ..models.fw_user_timestamp import FWUserTimestamp

        d = src_dict.copy()
        after = d.pop("after", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, FWUserTimestamp]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = FWUserTimestamp.from_dict(_created)

        descr = d.pop("descr", UNSET)

        disabled = d.pop("disabled", UNSET)

        _destination = d.pop("destination", UNSET)
        destination: Union[Unset, FWAddrPort]
        if isinstance(_destination, Unset):
            destination = UNSET
        else:
            destination = FWAddrPort.from_dict(_destination)

        dst = d.pop("dst", UNSET)

        dstport = d.pop("dstport", UNSET)

        dstmask = d.pop("dstmask", UNSET)

        destination_type = d.pop("destination_type", UNSET)

        dup = d.pop("dup", UNSET)

        idx = d.pop("idx", UNSET)

        interface = d.pop("interface", UNSET)

        ipprotocol = d.pop("ipprotocol", UNSET)

        natport = d.pop("natport", UNSET)

        nosync = d.pop("nosync", UNSET)

        protocol = d.pop("protocol", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, FWAddrPort]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = FWAddrPort.from_dict(_source)

        src = d.pop("src", UNSET)

        sourceport = d.pop("sourceport", UNSET)

        srcmask = d.pop("srcmask", UNSET)

        srcnot = d.pop("srcnot", UNSET)

        source_type = d.pop("source_type", UNSET)

        target = d.pop("target", UNSET)

        targetip = d.pop("targetip", UNSET)

        targetip_subnet = d.pop("targetip_subnet", UNSET)

        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, FWUserTimestamp]
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = FWUserTimestamp.from_dict(_updated)

        nat_outbound_rule = cls(
            after=after,
            created=created,
            descr=descr,
            disabled=disabled,
            destination=destination,
            dst=dst,
            dstport=dstport,
            dstmask=dstmask,
            destination_type=destination_type,
            dup=dup,
            idx=idx,
            interface=interface,
            ipprotocol=ipprotocol,
            natport=natport,
            nosync=nosync,
            protocol=protocol,
            source=source,
            src=src,
            sourceport=sourceport,
            srcmask=srcmask,
            srcnot=srcnot,
            source_type=source_type,
            target=target,
            targetip=targetip,
            targetip_subnet=targetip_subnet,
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
