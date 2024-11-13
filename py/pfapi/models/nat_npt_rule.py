from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nat_source import NATSource


T = TypeVar("T", bound="NATNptRule")


@_attrs_define
class NATNptRule:
    """
    Attributes:
        after (Union[Unset, str]):
        descr (Union[Unset, str]):
        disabled (Union[Unset, bool]):
        destination (Union[Unset, NATSource]):
        dst (Union[Unset, str]):
        dstmask (Union[Unset, str]):
        dstnot (Union[Unset, bool]):
        dup (Union[Unset, str]):
        idx (Union[Unset, int]):
        interface (Union[Unset, str]):
        source (Union[Unset, NATSource]):
        src (Union[Unset, str]):
        srcmask (Union[Unset, str]):
        srcnot (Union[Unset, bool]):
    """

    after: Union[Unset, str] = UNSET
    descr: Union[Unset, str] = UNSET
    disabled: Union[Unset, bool] = UNSET
    destination: Union[Unset, "NATSource"] = UNSET
    dst: Union[Unset, str] = UNSET
    dstmask: Union[Unset, str] = UNSET
    dstnot: Union[Unset, bool] = UNSET
    dup: Union[Unset, str] = UNSET
    idx: Union[Unset, int] = UNSET
    interface: Union[Unset, str] = UNSET
    source: Union[Unset, "NATSource"] = UNSET
    src: Union[Unset, str] = UNSET
    srcmask: Union[Unset, str] = UNSET
    srcnot: Union[Unset, bool] = UNSET
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

        dstnot = self.dstnot

        dup = self.dup

        idx = self.idx

        interface = self.interface

        source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        src = self.src

        srcmask = self.srcmask

        srcnot = self.srcnot

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
        if dstnot is not UNSET:
            field_dict["dstnot"] = dstnot
        if dup is not UNSET:
            field_dict["dup"] = dup
        if idx is not UNSET:
            field_dict["idx"] = idx
        if interface is not UNSET:
            field_dict["interface"] = interface
        if source is not UNSET:
            field_dict["source"] = source
        if src is not UNSET:
            field_dict["src"] = src
        if srcmask is not UNSET:
            field_dict["srcmask"] = srcmask
        if srcnot is not UNSET:
            field_dict["srcnot"] = srcnot

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nat_source import NATSource

        d = src_dict.copy()
        after = d.pop("after", UNSET)

        descr = d.pop("descr", UNSET)

        disabled = d.pop("disabled", UNSET)

        _destination = d.pop("destination", UNSET)
        destination: Union[Unset, NATSource]
        if isinstance(_destination, Unset):
            destination = UNSET
        else:
            destination = NATSource.from_dict(_destination)

        dst = d.pop("dst", UNSET)

        dstmask = d.pop("dstmask", UNSET)

        dstnot = d.pop("dstnot", UNSET)

        dup = d.pop("dup", UNSET)

        idx = d.pop("idx", UNSET)

        interface = d.pop("interface", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, NATSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = NATSource.from_dict(_source)

        src = d.pop("src", UNSET)

        srcmask = d.pop("srcmask", UNSET)

        srcnot = d.pop("srcnot", UNSET)

        nat_npt_rule = cls(
            after=after,
            descr=descr,
            disabled=disabled,
            destination=destination,
            dst=dst,
            dstmask=dstmask,
            dstnot=dstnot,
            dup=dup,
            idx=idx,
            interface=interface,
            source=source,
            src=src,
            srcmask=srcmask,
            srcnot=srcnot,
        )

        nat_npt_rule.additional_properties = d
        return nat_npt_rule

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
