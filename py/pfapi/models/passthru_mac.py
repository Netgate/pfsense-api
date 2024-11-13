from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PassthruMac")


@_attrs_define
class PassthruMac:
    """
    Attributes:
        action (Union[Unset, str]):
        mac (Union[Unset, str]):
        bw_up (Union[Unset, str]):
        bw_down (Union[Unset, str]):
        descr (Union[Unset, str]):
    """

    action: Union[Unset, str] = UNSET
    mac: Union[Unset, str] = UNSET
    bw_up: Union[Unset, str] = UNSET
    bw_down: Union[Unset, str] = UNSET
    descr: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        action = self.action

        mac = self.mac

        bw_up = self.bw_up

        bw_down = self.bw_down

        descr = self.descr

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if mac is not UNSET:
            field_dict["mac"] = mac
        if bw_up is not UNSET:
            field_dict["bw_up"] = bw_up
        if bw_down is not UNSET:
            field_dict["bw_down"] = bw_down
        if descr is not UNSET:
            field_dict["descr"] = descr

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        action = d.pop("action", UNSET)

        mac = d.pop("mac", UNSET)

        bw_up = d.pop("bw_up", UNSET)

        bw_down = d.pop("bw_down", UNSET)

        descr = d.pop("descr", UNSET)

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
