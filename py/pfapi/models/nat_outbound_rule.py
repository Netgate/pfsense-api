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
        created (FWUserTimestamp):
        destination (NATAddrPort):
        id (str):
        interface (str):
        ipprotocol (str):
        protocol (str):
        source (NATAddrPort):
        target (NATAddrPort):
        updated (FWUserTimestamp):
        descr (Union[Unset, str]):
        disabled (Union[Unset, bool]):
        nonat (Union[Unset, bool]):
        nosync (Union[Unset, bool]):
        poolopts (Union[Unset, str]):
        source_hash_key (Union[Unset, str]):
        staticnatport (Union[Unset, bool]):
    """

    created: "FWUserTimestamp"
    destination: "NATAddrPort"
    id: str
    interface: str
    ipprotocol: str
    protocol: str
    source: "NATAddrPort"
    target: "NATAddrPort"
    updated: "FWUserTimestamp"
    descr: Union[Unset, str] = UNSET
    disabled: Union[Unset, bool] = UNSET
    nonat: Union[Unset, bool] = UNSET
    nosync: Union[Unset, bool] = UNSET
    poolopts: Union[Unset, str] = UNSET
    source_hash_key: Union[Unset, str] = UNSET
    staticnatport: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created = self.created.to_dict()

        destination = self.destination.to_dict()

        id = self.id

        interface = self.interface

        ipprotocol = self.ipprotocol

        protocol = self.protocol

        source = self.source.to_dict()

        target = self.target.to_dict()

        updated = self.updated.to_dict()

        descr = self.descr

        disabled = self.disabled

        nonat = self.nonat

        nosync = self.nosync

        poolopts = self.poolopts

        source_hash_key = self.source_hash_key

        staticnatport = self.staticnatport

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created": created,
                "destination": destination,
                "id": id,
                "interface": interface,
                "ipprotocol": ipprotocol,
                "protocol": protocol,
                "source": source,
                "target": target,
                "updated": updated,
            }
        )
        if descr is not UNSET:
            field_dict["descr"] = descr
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if nonat is not UNSET:
            field_dict["nonat"] = nonat
        if nosync is not UNSET:
            field_dict["nosync"] = nosync
        if poolopts is not UNSET:
            field_dict["poolopts"] = poolopts
        if source_hash_key is not UNSET:
            field_dict["source-hash-key"] = source_hash_key
        if staticnatport is not UNSET:
            field_dict["staticnatport"] = staticnatport

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fw_user_timestamp import FWUserTimestamp
        from ..models.nat_addr_port import NATAddrPort

        d = src_dict.copy()
        created = FWUserTimestamp.from_dict(d.pop("created"))

        destination = NATAddrPort.from_dict(d.pop("destination"))

        id = d.pop("id")

        interface = d.pop("interface")

        ipprotocol = d.pop("ipprotocol")

        protocol = d.pop("protocol")

        source = NATAddrPort.from_dict(d.pop("source"))

        target = NATAddrPort.from_dict(d.pop("target"))

        updated = FWUserTimestamp.from_dict(d.pop("updated"))

        descr = d.pop("descr", UNSET)

        disabled = d.pop("disabled", UNSET)

        nonat = d.pop("nonat", UNSET)

        nosync = d.pop("nosync", UNSET)

        poolopts = d.pop("poolopts", UNSET)

        source_hash_key = d.pop("source-hash-key", UNSET)

        staticnatport = d.pop("staticnatport", UNSET)

        nat_outbound_rule = cls(
            created=created,
            destination=destination,
            id=id,
            interface=interface,
            ipprotocol=ipprotocol,
            protocol=protocol,
            source=source,
            target=target,
            updated=updated,
            descr=descr,
            disabled=disabled,
            nonat=nonat,
            nosync=nosync,
            poolopts=poolopts,
            source_hash_key=source_hash_key,
            staticnatport=staticnatport,
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
