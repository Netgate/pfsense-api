from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServicesActionParams")


@_attrs_define
class ServicesActionParams:
    """valid values:
    action = "start", "stop", "restart"

        Attributes:
            service (Union[Unset, str]):
            action (Union[Unset, str]):
            vpnid (Union[Unset, str]):
            mode (Union[Unset, str]):
            zone (Union[Unset, str]):
    """

    service: Union[Unset, str] = UNSET
    action: Union[Unset, str] = UNSET
    vpnid: Union[Unset, str] = UNSET
    mode: Union[Unset, str] = UNSET
    zone: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service = self.service

        action = self.action

        vpnid = self.vpnid

        mode = self.mode

        zone = self.zone

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service is not UNSET:
            field_dict["service"] = service
        if action is not UNSET:
            field_dict["action"] = action
        if vpnid is not UNSET:
            field_dict["vpnid"] = vpnid
        if mode is not UNSET:
            field_dict["mode"] = mode
        if zone is not UNSET:
            field_dict["zone"] = zone

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        service = d.pop("service", UNSET)

        action = d.pop("action", UNSET)

        vpnid = d.pop("vpnid", UNSET)

        mode = d.pop("mode", UNSET)

        zone = d.pop("zone", UNSET)

        services_action_params = cls(
            service=service,
            action=action,
            vpnid=vpnid,
            mode=mode,
            zone=zone,
        )

        services_action_params.additional_properties = d
        return services_action_params

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
