from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dhcp_range import DhcpRange


T = TypeVar("T", bound="DhcpdLan")


@_attrs_define
class DhcpdLan:
    """
    Attributes:
        text (str):
        enable (str):
        range_ (DhcpRange):
    """

    text: str
    enable: str
    range_: "DhcpRange"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        text = self.text

        enable = self.enable

        range_ = self.range_.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
                "enable": enable,
                "range": range_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dhcp_range import DhcpRange

        d = src_dict.copy()
        text = d.pop("text")

        enable = d.pop("enable")

        range_ = DhcpRange.from_dict(d.pop("range"))

        dhcpd_lan = cls(
            text=text,
            enable=enable,
            range_=range_,
        )

        dhcpd_lan.additional_properties = d
        return dhcpd_lan

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
