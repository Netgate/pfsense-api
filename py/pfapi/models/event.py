from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.firewall_event import FirewallEvent
    from ..models.interface_event import InterfaceEvent
    from ..models.system_event import SystemEvent


T = TypeVar("T", bound="Event")


@_attrs_define
class Event:
    """
    Attributes:
        event_type (str):
        event_id (int): ID is microsecond timestamp
        firewall (Union[Unset, FirewallEvent]):
        interface (Union[Unset, InterfaceEvent]):
        system (Union[Unset, SystemEvent]): changes to the system that is informational or impacts operation
    """

    event_type: str
    event_id: int
    firewall: Union[Unset, "FirewallEvent"] = UNSET
    interface: Union[Unset, "InterfaceEvent"] = UNSET
    system: Union[Unset, "SystemEvent"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event_type = self.event_type

        event_id = self.event_id

        firewall: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.firewall, Unset):
            firewall = self.firewall.to_dict()

        interface: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.interface, Unset):
            interface = self.interface.to_dict()

        system: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.system, Unset):
            system = self.system.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_type": event_type,
                "event_id": event_id,
            }
        )
        if firewall is not UNSET:
            field_dict["firewall"] = firewall
        if interface is not UNSET:
            field_dict["interface"] = interface
        if system is not UNSET:
            field_dict["system"] = system

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.firewall_event import FirewallEvent
        from ..models.interface_event import InterfaceEvent
        from ..models.system_event import SystemEvent

        d = src_dict.copy()
        event_type = d.pop("event_type")

        event_id = d.pop("event_id")

        _firewall = d.pop("firewall", UNSET)
        firewall: Union[Unset, FirewallEvent]
        if isinstance(_firewall, Unset):
            firewall = UNSET
        else:
            firewall = FirewallEvent.from_dict(_firewall)

        _interface = d.pop("interface", UNSET)
        interface: Union[Unset, InterfaceEvent]
        if isinstance(_interface, Unset):
            interface = UNSET
        else:
            interface = InterfaceEvent.from_dict(_interface)

        _system = d.pop("system", UNSET)
        system: Union[Unset, SystemEvent]
        if isinstance(_system, Unset):
            system = UNSET
        else:
            system = SystemEvent.from_dict(_system)

        event = cls(
            event_type=event_type,
            event_id=event_id,
            firewall=firewall,
            interface=interface,
            system=system,
        )

        event.additional_properties = d
        return event

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
