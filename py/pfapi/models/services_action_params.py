from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ServicesActionParams")


@_attrs_define
class ServicesActionParams:
    """valid values:
    action = "start", "stop", "restart"

        Attributes:
            service (str):
            action (str):
            vpnid (str):
            mode (str):
            zone (str):
    """

    service: str
    action: str
    vpnid: str
    mode: str
    zone: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service = self.service

        action = self.action

        vpnid = self.vpnid

        mode = self.mode

        zone = self.zone

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "service": service,
                "action": action,
                "vpnid": vpnid,
                "mode": mode,
                "zone": zone,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        service = d.pop("service")

        action = d.pop("action")

        vpnid = d.pop("vpnid")

        mode = d.pop("mode")

        zone = d.pop("zone")

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
