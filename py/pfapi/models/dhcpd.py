from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dhcpd_lan import DhcpdLan


T = TypeVar("T", bound="Dhcpd")


@_attrs_define
class Dhcpd:
    """
    Attributes:
        lan (Union[Unset, DhcpdLan]):
    """

    lan: Union[Unset, "DhcpdLan"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        lan: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lan, Unset):
            lan = self.lan.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lan is not UNSET:
            field_dict["lan"] = lan

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dhcpd_lan import DhcpdLan

        d = src_dict.copy()
        _lan = d.pop("lan", UNSET)
        lan: Union[Unset, DhcpdLan]
        if isinstance(_lan, Unset):
            lan = UNSET
        else:
            lan = DhcpdLan.from_dict(_lan)

        dhcpd = cls(
            lan=lan,
        )

        dhcpd.additional_properties = d
        return dhcpd

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
