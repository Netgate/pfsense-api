from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServicesStatus")


@_attrs_define
class ServicesStatus:
    """
    Attributes:
        name (str):
        description (Union[Unset, str]):
        vpnid (Union[Unset, str]): for openvpn service only
        mode (Union[Unset, str]): for openvpn service only
        zone (Union[Unset, str]): for captive portal service only
        enabled (Union[Unset, bool]):
        running (Union[Unset, bool]):
    """

    name: str
    description: Union[Unset, str] = UNSET
    vpnid: Union[Unset, str] = UNSET
    mode: Union[Unset, str] = UNSET
    zone: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    running: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        description = self.description

        vpnid = self.vpnid

        mode = self.mode

        zone = self.zone

        enabled = self.enabled

        running = self.running

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if vpnid is not UNSET:
            field_dict["vpnid"] = vpnid
        if mode is not UNSET:
            field_dict["mode"] = mode
        if zone is not UNSET:
            field_dict["zone"] = zone
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if running is not UNSET:
            field_dict["running"] = running

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        description = d.pop("description", UNSET)

        vpnid = d.pop("vpnid", UNSET)

        mode = d.pop("mode", UNSET)

        zone = d.pop("zone", UNSET)

        enabled = d.pop("enabled", UNSET)

        running = d.pop("running", UNSET)

        services_status = cls(
            name=name,
            description=description,
            vpnid=vpnid,
            mode=mode,
            zone=zone,
            enabled=enabled,
            running=running,
        )

        services_status.additional_properties = d
        return services_status

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
