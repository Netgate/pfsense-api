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
        id (str):
        associated_rule_id (str):
        created (FWUserTimestamp):
        destination (NATAddrPort):
        interface (str):
        natreflection (str):
        protocol (str):
        ipprotocol (str):
        source (NATAddrPort):
        updated (FWUserTimestamp):
        descr (Union[Unset, str]):
        disabled (Union[Unset, bool]):
        filter_rule_association (Union[Unset, str]):
        target (Union[Unset, NATAddrPort]):
        nordr (Union[Unset, bool]):
    """

    id: str
    associated_rule_id: str
    created: "FWUserTimestamp"
    destination: "NATAddrPort"
    interface: str
    natreflection: str
    protocol: str
    ipprotocol: str
    source: "NATAddrPort"
    updated: "FWUserTimestamp"
    descr: Union[Unset, str] = UNSET
    disabled: Union[Unset, bool] = UNSET
    filter_rule_association: Union[Unset, str] = UNSET
    target: Union[Unset, "NATAddrPort"] = UNSET
    nordr: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        associated_rule_id = self.associated_rule_id

        created = self.created.to_dict()

        destination = self.destination.to_dict()

        interface = self.interface

        natreflection = self.natreflection

        protocol = self.protocol

        ipprotocol = self.ipprotocol

        source = self.source.to_dict()

        updated = self.updated.to_dict()

        descr = self.descr

        disabled = self.disabled

        filter_rule_association = self.filter_rule_association

        target: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.target, Unset):
            target = self.target.to_dict()

        nordr = self.nordr

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "associated_rule_id": associated_rule_id,
                "created": created,
                "destination": destination,
                "interface": interface,
                "natreflection": natreflection,
                "protocol": protocol,
                "ipprotocol": ipprotocol,
                "source": source,
                "updated": updated,
            }
        )
        if descr is not UNSET:
            field_dict["descr"] = descr
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if filter_rule_association is not UNSET:
            field_dict["filter_rule_association"] = filter_rule_association
        if target is not UNSET:
            field_dict["target"] = target
        if nordr is not UNSET:
            field_dict["nordr"] = nordr

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fw_user_timestamp import FWUserTimestamp
        from ..models.nat_addr_port import NATAddrPort

        d = src_dict.copy()
        id = d.pop("id")

        associated_rule_id = d.pop("associated_rule_id")

        created = FWUserTimestamp.from_dict(d.pop("created"))

        destination = NATAddrPort.from_dict(d.pop("destination"))

        interface = d.pop("interface")

        natreflection = d.pop("natreflection")

        protocol = d.pop("protocol")

        ipprotocol = d.pop("ipprotocol")

        source = NATAddrPort.from_dict(d.pop("source"))

        updated = FWUserTimestamp.from_dict(d.pop("updated"))

        descr = d.pop("descr", UNSET)

        disabled = d.pop("disabled", UNSET)

        filter_rule_association = d.pop("filter_rule_association", UNSET)

        _target = d.pop("target", UNSET)
        target: Union[Unset, NATAddrPort]
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = NATAddrPort.from_dict(_target)

        nordr = d.pop("nordr", UNSET)

        nat_rule = cls(
            id=id,
            associated_rule_id=associated_rule_id,
            created=created,
            destination=destination,
            interface=interface,
            natreflection=natreflection,
            protocol=protocol,
            ipprotocol=ipprotocol,
            source=source,
            updated=updated,
            descr=descr,
            disabled=disabled,
            filter_rule_association=filter_rule_association,
            target=target,
            nordr=nordr,
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
