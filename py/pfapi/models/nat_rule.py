from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fw_user_timestamp import FWUserTimestamp
    from ..models.nat_addr_port import NATAddrPort


T = TypeVar("T", bound="NATRule")


@_attrs_define
class NATRule:
    """
    Attributes:
        idx (Union[Unset, int]):
        after (Union[Unset, str]):
        associated_rule_id (Union[Unset, str]):
        created (Union[Unset, FWUserTimestamp]):
        descr (Union[Unset, str]):
        disabled (Union[Unset, bool]):
        destination (Union[Unset, NATAddrPort]):
        dst (Union[Unset, str]):
        dstbeginport (Union[Unset, str]):
        dstendport (Union[Unset, str]):
        dstbeginport_cust (Union[Unset, str]):
        dstendport_cust (Union[Unset, str]):
        dstmask (Union[Unset, str]):
        dstnot (Union[Unset, bool]):
        dsttype (Union[Unset, str]):
        dup (Union[Unset, str]):
        filter_rule_association (Union[Unset, str]):
        interface (Union[Unset, str]):
        ipprotocol (Union[Unset, str]):
        local_port (Union[Unset, str]):
        localbeginport (Union[Unset, str]):
        localbeginport_cust (Union[Unset, str]):
        localip (Union[Unset, str]):
        localtype (Union[Unset, str]):
        natreflection (Union[Unset, str]):
        nordr (Union[Unset, bool]):
        protocol (Union[Unset, str]):
        proto (Union[Unset, str]):
        source (Union[Unset, NATAddrPort]):
        src (Union[Unset, str]):
        srcbeginport (Union[Unset, str]):
        srcendport (Union[Unset, str]):
        srcbeginport_cust (Union[Unset, str]):
        srcendport_cust (Union[Unset, str]):
        srcmask (Union[Unset, str]):
        srcnot (Union[Unset, bool]):
        srctype (Union[Unset, str]):
        target (Union[Unset, str]):
        updated (Union[Unset, FWUserTimestamp]):
    """

    idx: Union[Unset, int] = UNSET
    after: Union[Unset, str] = UNSET
    associated_rule_id: Union[Unset, str] = UNSET
    created: Union[Unset, "FWUserTimestamp"] = UNSET
    descr: Union[Unset, str] = UNSET
    disabled: Union[Unset, bool] = UNSET
    destination: Union[Unset, "NATAddrPort"] = UNSET
    dst: Union[Unset, str] = UNSET
    dstbeginport: Union[Unset, str] = UNSET
    dstendport: Union[Unset, str] = UNSET
    dstbeginport_cust: Union[Unset, str] = UNSET
    dstendport_cust: Union[Unset, str] = UNSET
    dstmask: Union[Unset, str] = UNSET
    dstnot: Union[Unset, bool] = UNSET
    dsttype: Union[Unset, str] = UNSET
    dup: Union[Unset, str] = UNSET
    filter_rule_association: Union[Unset, str] = UNSET
    interface: Union[Unset, str] = UNSET
    ipprotocol: Union[Unset, str] = UNSET
    local_port: Union[Unset, str] = UNSET
    localbeginport: Union[Unset, str] = UNSET
    localbeginport_cust: Union[Unset, str] = UNSET
    localip: Union[Unset, str] = UNSET
    localtype: Union[Unset, str] = UNSET
    natreflection: Union[Unset, str] = UNSET
    nordr: Union[Unset, bool] = UNSET
    protocol: Union[Unset, str] = UNSET
    proto: Union[Unset, str] = UNSET
    source: Union[Unset, "NATAddrPort"] = UNSET
    src: Union[Unset, str] = UNSET
    srcbeginport: Union[Unset, str] = UNSET
    srcendport: Union[Unset, str] = UNSET
    srcbeginport_cust: Union[Unset, str] = UNSET
    srcendport_cust: Union[Unset, str] = UNSET
    srcmask: Union[Unset, str] = UNSET
    srcnot: Union[Unset, bool] = UNSET
    srctype: Union[Unset, str] = UNSET
    target: Union[Unset, str] = UNSET
    updated: Union[Unset, "FWUserTimestamp"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        idx = self.idx

        after = self.after

        associated_rule_id = self.associated_rule_id

        created: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.to_dict()

        descr = self.descr

        disabled = self.disabled

        destination: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.destination, Unset):
            destination = self.destination.to_dict()

        dst = self.dst

        dstbeginport = self.dstbeginport

        dstendport = self.dstendport

        dstbeginport_cust = self.dstbeginport_cust

        dstendport_cust = self.dstendport_cust

        dstmask = self.dstmask

        dstnot = self.dstnot

        dsttype = self.dsttype

        dup = self.dup

        filter_rule_association = self.filter_rule_association

        interface = self.interface

        ipprotocol = self.ipprotocol

        local_port = self.local_port

        localbeginport = self.localbeginport

        localbeginport_cust = self.localbeginport_cust

        localip = self.localip

        localtype = self.localtype

        natreflection = self.natreflection

        nordr = self.nordr

        protocol = self.protocol

        proto = self.proto

        source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        src = self.src

        srcbeginport = self.srcbeginport

        srcendport = self.srcendport

        srcbeginport_cust = self.srcbeginport_cust

        srcendport_cust = self.srcendport_cust

        srcmask = self.srcmask

        srcnot = self.srcnot

        srctype = self.srctype

        target = self.target

        updated: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if idx is not UNSET:
            field_dict["idx"] = idx
        if after is not UNSET:
            field_dict["after"] = after
        if associated_rule_id is not UNSET:
            field_dict["associated_rule_id"] = associated_rule_id
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
        if dstbeginport is not UNSET:
            field_dict["dstbeginport"] = dstbeginport
        if dstendport is not UNSET:
            field_dict["dstendport"] = dstendport
        if dstbeginport_cust is not UNSET:
            field_dict["dstbeginport_cust"] = dstbeginport_cust
        if dstendport_cust is not UNSET:
            field_dict["dstendport_cust"] = dstendport_cust
        if dstmask is not UNSET:
            field_dict["dstmask"] = dstmask
        if dstnot is not UNSET:
            field_dict["dstnot"] = dstnot
        if dsttype is not UNSET:
            field_dict["dsttype"] = dsttype
        if dup is not UNSET:
            field_dict["dup"] = dup
        if filter_rule_association is not UNSET:
            field_dict["filter_rule_association"] = filter_rule_association
        if interface is not UNSET:
            field_dict["interface"] = interface
        if ipprotocol is not UNSET:
            field_dict["ipprotocol"] = ipprotocol
        if local_port is not UNSET:
            field_dict["local_port"] = local_port
        if localbeginport is not UNSET:
            field_dict["localbeginport"] = localbeginport
        if localbeginport_cust is not UNSET:
            field_dict["localbeginport_cust"] = localbeginport_cust
        if localip is not UNSET:
            field_dict["localip"] = localip
        if localtype is not UNSET:
            field_dict["localtype"] = localtype
        if natreflection is not UNSET:
            field_dict["natreflection"] = natreflection
        if nordr is not UNSET:
            field_dict["nordr"] = nordr
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if proto is not UNSET:
            field_dict["proto"] = proto
        if source is not UNSET:
            field_dict["source"] = source
        if src is not UNSET:
            field_dict["src"] = src
        if srcbeginport is not UNSET:
            field_dict["srcbeginport"] = srcbeginport
        if srcendport is not UNSET:
            field_dict["srcendport"] = srcendport
        if srcbeginport_cust is not UNSET:
            field_dict["srcbeginport_cust"] = srcbeginport_cust
        if srcendport_cust is not UNSET:
            field_dict["srcendport_cust"] = srcendport_cust
        if srcmask is not UNSET:
            field_dict["srcmask"] = srcmask
        if srcnot is not UNSET:
            field_dict["srcnot"] = srcnot
        if srctype is not UNSET:
            field_dict["srctype"] = srctype
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
        idx = d.pop("idx", UNSET)

        after = d.pop("after", UNSET)

        associated_rule_id = d.pop("associated_rule_id", UNSET)

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

        dst = d.pop("dst", UNSET)

        dstbeginport = d.pop("dstbeginport", UNSET)

        dstendport = d.pop("dstendport", UNSET)

        dstbeginport_cust = d.pop("dstbeginport_cust", UNSET)

        dstendport_cust = d.pop("dstendport_cust", UNSET)

        dstmask = d.pop("dstmask", UNSET)

        dstnot = d.pop("dstnot", UNSET)

        dsttype = d.pop("dsttype", UNSET)

        dup = d.pop("dup", UNSET)

        filter_rule_association = d.pop("filter_rule_association", UNSET)

        interface = d.pop("interface", UNSET)

        ipprotocol = d.pop("ipprotocol", UNSET)

        local_port = d.pop("local_port", UNSET)

        localbeginport = d.pop("localbeginport", UNSET)

        localbeginport_cust = d.pop("localbeginport_cust", UNSET)

        localip = d.pop("localip", UNSET)

        localtype = d.pop("localtype", UNSET)

        natreflection = d.pop("natreflection", UNSET)

        nordr = d.pop("nordr", UNSET)

        protocol = d.pop("protocol", UNSET)

        proto = d.pop("proto", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, NATAddrPort]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = NATAddrPort.from_dict(_source)

        src = d.pop("src", UNSET)

        srcbeginport = d.pop("srcbeginport", UNSET)

        srcendport = d.pop("srcendport", UNSET)

        srcbeginport_cust = d.pop("srcbeginport_cust", UNSET)

        srcendport_cust = d.pop("srcendport_cust", UNSET)

        srcmask = d.pop("srcmask", UNSET)

        srcnot = d.pop("srcnot", UNSET)

        srctype = d.pop("srctype", UNSET)

        target = d.pop("target", UNSET)

        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, FWUserTimestamp]
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = FWUserTimestamp.from_dict(_updated)

        nat_rule = cls(
            idx=idx,
            after=after,
            associated_rule_id=associated_rule_id,
            created=created,
            descr=descr,
            disabled=disabled,
            destination=destination,
            dst=dst,
            dstbeginport=dstbeginport,
            dstendport=dstendport,
            dstbeginport_cust=dstbeginport_cust,
            dstendport_cust=dstendport_cust,
            dstmask=dstmask,
            dstnot=dstnot,
            dsttype=dsttype,
            dup=dup,
            filter_rule_association=filter_rule_association,
            interface=interface,
            ipprotocol=ipprotocol,
            local_port=local_port,
            localbeginport=localbeginport,
            localbeginport_cust=localbeginport_cust,
            localip=localip,
            localtype=localtype,
            natreflection=natreflection,
            nordr=nordr,
            protocol=protocol,
            proto=proto,
            source=source,
            src=src,
            srcbeginport=srcbeginport,
            srcendport=srcendport,
            srcbeginport_cust=srcbeginport_cust,
            srcendport_cust=srcendport_cust,
            srcmask=srcmask,
            srcnot=srcnot,
            srctype=srctype,
            target=target,
            updated=updated,
        )

        nat_rule.additional_properties = d
        return nat_rule

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
