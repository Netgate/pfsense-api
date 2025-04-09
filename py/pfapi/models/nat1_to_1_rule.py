from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nat_addr_port import NATAddrPort


T = TypeVar("T", bound="NAT1To1Rule")


@_attrs_define
class NAT1To1Rule:
    """
    Attributes:
        id (Union[Unset, str]):
        descr (Union[Unset, str]):
        disabled (Union[Unset, bool]):
        destination (Union[Unset, NATAddrPort]):
        external (Union[Unset, NATAddrPort]):
        interface (Union[Unset, str]):
        ipprotocol (Union[Unset, str]):
        nobinat (Union[Unset, bool]):
        source (Union[Unset, NATAddrPort]):
    """

    id: Union[Unset, str] = UNSET
    descr: Union[Unset, str] = UNSET
    disabled: Union[Unset, bool] = UNSET
    destination: Union[Unset, "NATAddrPort"] = UNSET
    external: Union[Unset, "NATAddrPort"] = UNSET
    interface: Union[Unset, str] = UNSET
    ipprotocol: Union[Unset, str] = UNSET
    nobinat: Union[Unset, bool] = UNSET
    source: Union[Unset, "NATAddrPort"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        descr = self.descr

        disabled = self.disabled

        destination: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.destination, Unset):
            destination = self.destination.to_dict()

        external: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.external, Unset):
            external = self.external.to_dict()

        interface = self.interface

        ipprotocol = self.ipprotocol

        nobinat = self.nobinat

        source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if descr is not UNSET:
            field_dict["descr"] = descr
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if destination is not UNSET:
            field_dict["destination"] = destination
        if external is not UNSET:
            field_dict["external"] = external
        if interface is not UNSET:
            field_dict["interface"] = interface
        if ipprotocol is not UNSET:
            field_dict["ipprotocol"] = ipprotocol
        if nobinat is not UNSET:
            field_dict["nobinat"] = nobinat
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nat_addr_port import NATAddrPort

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        descr = d.pop("descr", UNSET)

        disabled = d.pop("disabled", UNSET)

        _destination = d.pop("destination", UNSET)
        destination: Union[Unset, NATAddrPort]
        if isinstance(_destination, Unset):
            destination = UNSET
        else:
            destination = NATAddrPort.from_dict(_destination)

        _external = d.pop("external", UNSET)
        external: Union[Unset, NATAddrPort]
        if isinstance(_external, Unset):
            external = UNSET
        else:
            external = NATAddrPort.from_dict(_external)

        interface = d.pop("interface", UNSET)

        ipprotocol = d.pop("ipprotocol", UNSET)

        nobinat = d.pop("nobinat", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, NATAddrPort]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = NATAddrPort.from_dict(_source)

        nat1_to_1_rule = cls(
            id=id,
            descr=descr,
            disabled=disabled,
            destination=destination,
            external=external,
            interface=interface,
            ipprotocol=ipprotocol,
            nobinat=nobinat,
            source=source,
        )

        nat1_to_1_rule.additional_properties = d
        return nat1_to_1_rule

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
