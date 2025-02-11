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
        destination (NATNptAddr):
        id (str):
        interface (str):
        source (NATNptAddr):
        descr (Union[Unset, str]):
        disabled (Union[Unset, bool]):
    """

    destination: "NATNptAddr"
    id: str
    interface: str
    source: "NATNptAddr"
    descr: Union[Unset, str] = UNSET
    disabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        destination = self.destination.to_dict()

        id = self.id

        interface = self.interface

        source = self.source.to_dict()

        descr = self.descr

        disabled = self.disabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "destination": destination,
                "id": id,
                "interface": interface,
                "source": source,
            }
        )
        if descr is not UNSET:
            field_dict["descr"] = descr
        if disabled is not UNSET:
            field_dict["disabled"] = disabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nat_npt_addr import NATNptAddr

        d = src_dict.copy()
        destination = NATNptAddr.from_dict(d.pop("destination"))

        id = d.pop("id")

        interface = d.pop("interface")

        source = NATNptAddr.from_dict(d.pop("source"))

        descr = d.pop("descr", UNSET)

        disabled = d.pop("disabled", UNSET)

        nat_npt_rule = cls(
            destination=destination,
            id=id,
            interface=interface,
            source=source,
            descr=descr,
            disabled=disabled,
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
