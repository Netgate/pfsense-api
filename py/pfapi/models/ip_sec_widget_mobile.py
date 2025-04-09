from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IPSecWidgetMobile")


@_attrs_define
class IPSecWidgetMobile:
    """
    Attributes:
        user (Union[Unset, str]):
        ip (Union[Unset, str]):
        status (Union[Unset, str]):
    """

    user: Union[Unset, str] = UNSET
    ip: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user = self.user

        ip = self.ip

        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if ip is not UNSET:
            field_dict["ip"] = ip
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user = d.pop("user", UNSET)

        ip = d.pop("ip", UNSET)

        status = d.pop("status", UNSET)

        ip_sec_widget_mobile = cls(
            user=user,
            ip=ip,
            status=status,
        )

        ip_sec_widget_mobile.additional_properties = d
        return ip_sec_widget_mobile

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
