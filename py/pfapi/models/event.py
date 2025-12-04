from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_event import ConfigEvent
    from ..models.firewall_event import FirewallEvent
    from ..models.interface_event import InterfaceEvent
    from ..models.system_event import SystemEvent


T = TypeVar("T", bound="Event")


@_attrs_define
class Event:
    """
    Attributes:
        event_type (str | Unset):
        event_id (int | Unset): ID is microsecond timestamp
        firewall (FirewallEvent | Unset):
        interface (InterfaceEvent | Unset):
        system (SystemEvent | Unset): changes to the system that is informational or impacts operation
        config (ConfigEvent | Unset): This event is sent when configuration changes have occurred, with an indicator
            of whether there are dirty subsystems flagged, or if the system requires a reboot
    """

    event_type: str | Unset = UNSET
    event_id: int | Unset = UNSET
    firewall: FirewallEvent | Unset = UNSET
    interface: InterfaceEvent | Unset = UNSET
    system: SystemEvent | Unset = UNSET
    config: ConfigEvent | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_type = self.event_type

        event_id = self.event_id

        firewall: dict[str, Any] | Unset = UNSET
        if not isinstance(self.firewall, Unset):
            firewall = self.firewall.to_dict()

        interface: dict[str, Any] | Unset = UNSET
        if not isinstance(self.interface, Unset):
            interface = self.interface.to_dict()

        system: dict[str, Any] | Unset = UNSET
        if not isinstance(self.system, Unset):
            system = self.system.to_dict()

        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_type is not UNSET:
            field_dict["event_type"] = event_type
        if event_id is not UNSET:
            field_dict["event_id"] = event_id
        if firewall is not UNSET:
            field_dict["firewall"] = firewall
        if interface is not UNSET:
            field_dict["interface"] = interface
        if system is not UNSET:
            field_dict["system"] = system
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_event import ConfigEvent
        from ..models.firewall_event import FirewallEvent
        from ..models.interface_event import InterfaceEvent
        from ..models.system_event import SystemEvent

        d = dict(src_dict)
        event_type = d.pop("event_type", UNSET)

        event_id = d.pop("event_id", UNSET)

        _firewall = d.pop("firewall", UNSET)
        firewall: FirewallEvent | Unset
        if isinstance(_firewall, Unset):
            firewall = UNSET
        else:
            firewall = FirewallEvent.from_dict(_firewall)

        _interface = d.pop("interface", UNSET)
        interface: InterfaceEvent | Unset
        if isinstance(_interface, Unset):
            interface = UNSET
        else:
            interface = InterfaceEvent.from_dict(_interface)

        _system = d.pop("system", UNSET)
        system: SystemEvent | Unset
        if isinstance(_system, Unset):
            system = UNSET
        else:
            system = SystemEvent.from_dict(_system)

        _config = d.pop("config", UNSET)
        config: ConfigEvent | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = ConfigEvent.from_dict(_config)

        event = cls(
            event_type=event_type,
            event_id=event_id,
            firewall=firewall,
            interface=interface,
            system=system,
            config=config,
        )

        event.additional_properties = d
        return event

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
