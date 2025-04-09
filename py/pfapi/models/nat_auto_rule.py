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
        id (Union[Unset, str]):
        interface (Union[Unset, str]):
        dstport (Union[Unset, str]):
        target (Union[Unset, str]):
        destination (Union[Unset, NATAutoAddr]):
        dstaddr (Union[Unset, str]):
        source (Union[Unset, NATAutoAddr]):
        dstany (Union[Unset, bool]):
        srcany (Union[Unset, bool]):
        srcaddr (Union[Unset, str]):
        staticnatport (Union[Unset, bool]):
        descr (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    interface: Union[Unset, str] = UNSET
    dstport: Union[Unset, str] = UNSET
    target: Union[Unset, str] = UNSET
    destination: Union[Unset, "NATAutoAddr"] = UNSET
    dstaddr: Union[Unset, str] = UNSET
    source: Union[Unset, "NATAutoAddr"] = UNSET
    dstany: Union[Unset, bool] = UNSET
    srcany: Union[Unset, bool] = UNSET
    srcaddr: Union[Unset, str] = UNSET
    staticnatport: Union[Unset, bool] = UNSET
    descr: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        interface = self.interface

        dstport = self.dstport

        target = self.target

        destination: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.destination, Unset):
            destination = self.destination.to_dict()

        dstaddr = self.dstaddr

        source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        dstany = self.dstany

        srcany = self.srcany

        srcaddr = self.srcaddr

        staticnatport = self.staticnatport

        descr = self.descr

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if interface is not UNSET:
            field_dict["interface"] = interface
        if dstport is not UNSET:
            field_dict["dstport"] = dstport
        if target is not UNSET:
            field_dict["target"] = target
        if destination is not UNSET:
            field_dict["destination"] = destination
        if dstaddr is not UNSET:
            field_dict["dstaddr"] = dstaddr
        if source is not UNSET:
            field_dict["source"] = source
        if dstany is not UNSET:
            field_dict["dstany"] = dstany
        if srcany is not UNSET:
            field_dict["srcany"] = srcany
        if srcaddr is not UNSET:
            field_dict["srcaddr"] = srcaddr
        if staticnatport is not UNSET:
            field_dict["staticnatport"] = staticnatport
        if descr is not UNSET:
            field_dict["descr"] = descr

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nat_auto_addr import NATAutoAddr

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        interface = d.pop("interface", UNSET)

        dstport = d.pop("dstport", UNSET)

        target = d.pop("target", UNSET)

        _destination = d.pop("destination", UNSET)
        destination: Union[Unset, NATAutoAddr]
        if isinstance(_destination, Unset):
            destination = UNSET
        else:
            destination = NATAutoAddr.from_dict(_destination)

        dstaddr = d.pop("dstaddr", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, NATAutoAddr]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = NATAutoAddr.from_dict(_source)

        dstany = d.pop("dstany", UNSET)

        srcany = d.pop("srcany", UNSET)

        srcaddr = d.pop("srcaddr", UNSET)

        staticnatport = d.pop("staticnatport", UNSET)

        descr = d.pop("descr", UNSET)

        nat_auto_rule = cls(
            id=id,
            interface=interface,
            dstport=dstport,
            target=target,
            destination=destination,
            dstaddr=dstaddr,
            source=source,
            dstany=dstany,
            srcany=srcany,
            srcaddr=srcaddr,
            staticnatport=staticnatport,
            descr=descr,
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
