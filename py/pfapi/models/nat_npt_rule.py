from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nat_npt_addr import NATNptAddr


T = TypeVar("T", bound="NATNptRule")


@_attrs_define
class NATNptRule:
    """
    Attributes:
        descr (Union[Unset, str]):
        disabled (Union[Unset, bool]):
        destination (Union[Unset, NATNptAddr]):
        id (Union[Unset, str]):
        interface (Union[Unset, str]):
        source (Union[Unset, NATNptAddr]):
    """

    descr: Union[Unset, str] = UNSET
    disabled: Union[Unset, bool] = UNSET
    destination: Union[Unset, "NATNptAddr"] = UNSET
    id: Union[Unset, str] = UNSET
    interface: Union[Unset, str] = UNSET
    source: Union[Unset, "NATNptAddr"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        descr = self.descr

        disabled = self.disabled

        destination: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.destination, Unset):
            destination = self.destination.to_dict()

        id = self.id

        interface = self.interface

        source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if descr is not UNSET:
            field_dict["descr"] = descr
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if destination is not UNSET:
            field_dict["destination"] = destination
        if id is not UNSET:
            field_dict["id"] = id
        if interface is not UNSET:
            field_dict["interface"] = interface
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nat_npt_addr import NATNptAddr

        d = src_dict.copy()
        descr = d.pop("descr", UNSET)

        disabled = d.pop("disabled", UNSET)

        _destination = d.pop("destination", UNSET)
        destination: Union[Unset, NATNptAddr]
        if isinstance(_destination, Unset):
            destination = UNSET
        else:
            destination = NATNptAddr.from_dict(_destination)

        id = d.pop("id", UNSET)

        interface = d.pop("interface", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, NATNptAddr]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = NATNptAddr.from_dict(_source)

        nat_npt_rule = cls(
            descr=descr,
            disabled=disabled,
            destination=destination,
            id=id,
            interface=interface,
            source=source,
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
