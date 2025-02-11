from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IfStatsBandwidth")


@_attrs_define
class IfStatsBandwidth:
    """
    Attributes:
        host (str):
        bitsin (str):
        bitsout (str):
    """

    host: str
    bitsin: str
    bitsout: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        host = self.host

        bitsin = self.bitsin

        bitsout = self.bitsout

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "host": host,
                "bitsin": bitsin,
                "bitsout": bitsout,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        host = d.pop("host")

        bitsin = d.pop("bitsin")

        bitsout = d.pop("bitsout")

        if_stats_bandwidth = cls(
            host=host,
            bitsin=bitsin,
            bitsout=bitsout,
        )

        if_stats_bandwidth.additional_properties = d
        return if_stats_bandwidth

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
