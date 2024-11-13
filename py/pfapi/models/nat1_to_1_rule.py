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
        after (Union[Unset, str]):
        descr (Union[Unset, str]):
        disabled (Union[Unset, bool]):
        destination (Union[Unset, NATAddrPort]):
        dst (Union[Unset, str]):
        dstmask (Union[Unset, str]):
        dsttype (Union[Unset, str]):
        dstnot (Union[Unset, bool]):
        dup (Union[Unset, str]):
        external (Union[Unset, str]):
        exttype (Union[Unset, str]):
        idx (Union[Unset, int]):
        interface (Union[Unset, str]):
        ipprotocol (Union[Unset, str]):
        source (Union[Unset, NATAddrPort]):
        src (Union[Unset, str]):
        srcmask (Union[Unset, str]):
        srcnot (Union[Unset, bool]):
        srctype (Union[Unset, str]):
        target (Union[Unset, str]):
    """

    after: Union[Unset, str] = UNSET
    descr: Union[Unset, str] = UNSET
    disabled: Union[Unset, bool] = UNSET
    destination: Union[Unset, "NATAddrPort"] = UNSET
    dst: Union[Unset, str] = UNSET
    dstmask: Union[Unset, str] = UNSET
    dsttype: Union[Unset, str] = UNSET
    dstnot: Union[Unset, bool] = UNSET
    dup: Union[Unset, str] = UNSET
    external: Union[Unset, str] = UNSET
    exttype: Union[Unset, str] = UNSET
    idx: Union[Unset, int] = UNSET
    interface: Union[Unset, str] = UNSET
    ipprotocol: Union[Unset, str] = UNSET
    source: Union[Unset, "NATAddrPort"] = UNSET
    src: Union[Unset, str] = UNSET
    srcmask: Union[Unset, str] = UNSET
    srcnot: Union[Unset, bool] = UNSET
    srctype: Union[Unset, str] = UNSET
    target: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        after = self.after

        descr = self.descr

        disabled = self.disabled

        destination: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.destination, Unset):
            destination = self.destination.to_dict()

        dst = self.dst

        dstmask = self.dstmask

        dsttype = self.dsttype

        dstnot = self.dstnot

        dup = self.dup

        external = self.external

        exttype = self.exttype

        idx = self.idx

        interface = self.interface

        ipprotocol = self.ipprotocol

        source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        src = self.src

        srcmask = self.srcmask

        srcnot = self.srcnot

        srctype = self.srctype

        target = self.target

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if after is not UNSET:
            field_dict["after"] = after
        if descr is not UNSET:
            field_dict["descr"] = descr
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if destination is not UNSET:
            field_dict["destination"] = destination
        if dst is not UNSET:
            field_dict["dst"] = dst
        if dstmask is not UNSET:
            field_dict["dstmask"] = dstmask
        if dsttype is not UNSET:
            field_dict["dsttype"] = dsttype
        if dstnot is not UNSET:
            field_dict["dstnot"] = dstnot
        if dup is not UNSET:
            field_dict["dup"] = dup
        if external is not UNSET:
            field_dict["external"] = external
        if exttype is not UNSET:
            field_dict["exttype"] = exttype
        if idx is not UNSET:
            field_dict["idx"] = idx
        if interface is not UNSET:
            field_dict["interface"] = interface
        if ipprotocol is not UNSET:
            field_dict["ipprotocol"] = ipprotocol
        if source is not UNSET:
            field_dict["source"] = source
        if src is not UNSET:
            field_dict["src"] = src
        if srcmask is not UNSET:
            field_dict["srcmask"] = srcmask
        if srcnot is not UNSET:
            field_dict["srcnot"] = srcnot
        if srctype is not UNSET:
            field_dict["srctype"] = srctype
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nat_addr_port import NATAddrPort

        d = src_dict.copy()
        after = d.pop("after", UNSET)

        descr = d.pop("descr", UNSET)

        disabled = d.pop("disabled", UNSET)

        _destination = d.pop("destination", UNSET)
        destination: Union[Unset, NATAddrPort]
        if isinstance(_destination, Unset):
            destination = UNSET
        else:
            destination = NATAddrPort.from_dict(_destination)

        dst = d.pop("dst", UNSET)

        dstmask = d.pop("dstmask", UNSET)

        dsttype = d.pop("dsttype", UNSET)

        dstnot = d.pop("dstnot", UNSET)

        dup = d.pop("dup", UNSET)

        external = d.pop("external", UNSET)

        exttype = d.pop("exttype", UNSET)

        idx = d.pop("idx", UNSET)

        interface = d.pop("interface", UNSET)

        ipprotocol = d.pop("ipprotocol", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, NATAddrPort]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = NATAddrPort.from_dict(_source)

        src = d.pop("src", UNSET)

        srcmask = d.pop("srcmask", UNSET)

        srcnot = d.pop("srcnot", UNSET)

        srctype = d.pop("srctype", UNSET)

        target = d.pop("target", UNSET)

        nat1_to_1_rule = cls(
            after=after,
            descr=descr,
            disabled=disabled,
            destination=destination,
            dst=dst,
            dstmask=dstmask,
            dsttype=dsttype,
            dstnot=dstnot,
            dup=dup,
            external=external,
            exttype=exttype,
            idx=idx,
            interface=interface,
            ipprotocol=ipprotocol,
            source=source,
            src=src,
            srcmask=srcmask,
            srcnot=srcnot,
            srctype=srctype,
            target=target,
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
