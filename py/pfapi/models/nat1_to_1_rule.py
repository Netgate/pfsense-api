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
        id (str):
        destination (NATAddrPort):
        external (NATAddrPort):
        interface (str):
        ipprotocol (str):
        source (NATAddrPort):
        descr (Union[Unset, str]):
        disabled (Union[Unset, bool]):
        nobinat (Union[Unset, bool]):
    """

    id: str
    destination: "NATAddrPort"
    external: "NATAddrPort"
    interface: str
    ipprotocol: str
    source: "NATAddrPort"
    descr: Union[Unset, str] = UNSET
    disabled: Union[Unset, bool] = UNSET
    nobinat: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        destination = self.destination.to_dict()

        external = self.external.to_dict()

        interface = self.interface

        ipprotocol = self.ipprotocol

        source = self.source.to_dict()

        descr = self.descr

        disabled = self.disabled

        nobinat = self.nobinat

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "destination": destination,
                "external": external,
                "interface": interface,
                "ipprotocol": ipprotocol,
                "source": source,
            }
        )
        if descr is not UNSET:
            field_dict["descr"] = descr
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if nobinat is not UNSET:
            field_dict["nobinat"] = nobinat

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nat_addr_port import NATAddrPort

        d = src_dict.copy()
        id = d.pop("id")

        destination = NATAddrPort.from_dict(d.pop("destination"))

        external = NATAddrPort.from_dict(d.pop("external"))

        interface = d.pop("interface")

        ipprotocol = d.pop("ipprotocol")

        source = NATAddrPort.from_dict(d.pop("source"))

        descr = d.pop("descr", UNSET)

        disabled = d.pop("disabled", UNSET)

        nobinat = d.pop("nobinat", UNSET)

        nat1_to_1_rule = cls(
            id=id,
            destination=destination,
            external=external,
            interface=interface,
            ipprotocol=ipprotocol,
            source=source,
            descr=descr,
            disabled=disabled,
            nobinat=nobinat,
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
