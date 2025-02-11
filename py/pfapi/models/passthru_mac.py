from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PassthruMac")


@_attrs_define
class PassthruMac:
    """
    Attributes:
        action (str):
        mac (str):
        bw_up (str):
        bw_down (str):
        descr (str):
    """

    action: str
    mac: str
    bw_up: str
    bw_down: str
    descr: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        action = self.action

        mac = self.mac

        bw_up = self.bw_up

        bw_down = self.bw_down

        descr = self.descr

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "mac": mac,
                "bw_up": bw_up,
                "bw_down": bw_down,
                "descr": descr,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        action = d.pop("action")

        mac = d.pop("mac")

        bw_up = d.pop("bw_up")

        bw_down = d.pop("bw_down")

        descr = d.pop("descr")

        passthru_mac = cls(
            action=action,
            mac=mac,
            bw_up=bw_up,
            bw_down=bw_down,
            descr=descr,
        )

        passthru_mac.additional_properties = d
        return passthru_mac

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
