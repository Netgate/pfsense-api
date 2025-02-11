from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nat_auto_addr import NATAutoAddr


T = TypeVar("T", bound="NATAutoRule")


@_attrs_define
class NATAutoRule:
    """
    Attributes:
        id (str):
        interface (str):
        dstport (str):
        target (str):
        dstaddr (str):
        dstany (bool):
        srcany (bool):
        srcaddr (str):
        staticnatport (bool):
        descr (str):
        destination (Union[Unset, NATAutoAddr]):
        source (Union[Unset, NATAutoAddr]):
    """

    id: str
    interface: str
    dstport: str
    target: str
    dstaddr: str
    dstany: bool
    srcany: bool
    srcaddr: str
    staticnatport: bool
    descr: str
    destination: Union[Unset, "NATAutoAddr"] = UNSET
    source: Union[Unset, "NATAutoAddr"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        interface = self.interface

        dstport = self.dstport

        target = self.target

        dstaddr = self.dstaddr

        dstany = self.dstany

        srcany = self.srcany

        srcaddr = self.srcaddr

        staticnatport = self.staticnatport

        descr = self.descr

        destination: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.destination, Unset):
            destination = self.destination.to_dict()

        source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "interface": interface,
                "dstport": dstport,
                "target": target,
                "dstaddr": dstaddr,
                "dstany": dstany,
                "srcany": srcany,
                "srcaddr": srcaddr,
                "staticnatport": staticnatport,
                "descr": descr,
            }
        )
        if destination is not UNSET:
            field_dict["destination"] = destination
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nat_auto_addr import NATAutoAddr

        d = src_dict.copy()
        id = d.pop("id")

        interface = d.pop("interface")

        dstport = d.pop("dstport")

        target = d.pop("target")

        dstaddr = d.pop("dstaddr")

        dstany = d.pop("dstany")

        srcany = d.pop("srcany")

        srcaddr = d.pop("srcaddr")

        staticnatport = d.pop("staticnatport")

        descr = d.pop("descr")

        _destination = d.pop("destination", UNSET)
        destination: Union[Unset, NATAutoAddr]
        if isinstance(_destination, Unset):
            destination = UNSET
        else:
            destination = NATAutoAddr.from_dict(_destination)

        _source = d.pop("source", UNSET)
        source: Union[Unset, NATAutoAddr]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = NATAutoAddr.from_dict(_source)

        nat_auto_rule = cls(
            id=id,
            interface=interface,
            dstport=dstport,
            target=target,
            dstaddr=dstaddr,
            dstany=dstany,
            srcany=srcany,
            srcaddr=srcaddr,
            staticnatport=staticnatport,
            descr=descr,
            destination=destination,
            source=source,
        )

        nat_auto_rule.additional_properties = d
        return nat_auto_rule

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
