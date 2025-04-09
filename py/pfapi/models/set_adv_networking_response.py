from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetAdvNetworkingResponse")


@_attrs_define
class SetAdvNetworkingResponse:
    """
    Attributes:
        reboot_msg (Union[Unset, str]):
    """

    reboot_msg: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reboot_msg = self.reboot_msg

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reboot_msg is not UNSET:
            field_dict["reboot_msg"] = reboot_msg

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        reboot_msg = d.pop("reboot_msg", UNSET)

        set_adv_networking_response = cls(
            reboot_msg=reboot_msg,
        )

        set_adv_networking_response.additional_properties = d
        return set_adv_networking_response

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
