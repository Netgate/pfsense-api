from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dhcp_lease import DHCPLease
    from ..models.dhcpha_state import DHCPHAState
    from ..models.lease_interface import LeaseInterface


T = TypeVar("T", bound="DHCPLeases")


@_attrs_define
class DHCPLeases:
    """
    Attributes:
        v4leases (Union[Unset, List['DHCPLease']]):
        v6leases (Union[Unset, List['DHCPLease']]):
        prefixes (Union[Unset, List['DHCPLease']]):
        interfaces (Union[Unset, List['LeaseInterface']]):
        interfacesv6 (Union[Unset, List['LeaseInterface']]):
        v4_ha_status (Union[Unset, List['DHCPHAState']]):
        v6_ha_status (Union[Unset, List['DHCPHAState']]):
    """

    v4leases: Union[Unset, List["DHCPLease"]] = UNSET
    v6leases: Union[Unset, List["DHCPLease"]] = UNSET
    prefixes: Union[Unset, List["DHCPLease"]] = UNSET
    interfaces: Union[Unset, List["LeaseInterface"]] = UNSET
    interfacesv6: Union[Unset, List["LeaseInterface"]] = UNSET
    v4_ha_status: Union[Unset, List["DHCPHAState"]] = UNSET
    v6_ha_status: Union[Unset, List["DHCPHAState"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        v4leases: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.v4leases, Unset):
            v4leases = []
            for v4leases_item_data in self.v4leases:
                v4leases_item = v4leases_item_data.to_dict()
                v4leases.append(v4leases_item)

        v6leases: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.v6leases, Unset):
            v6leases = []
            for v6leases_item_data in self.v6leases:
                v6leases_item = v6leases_item_data.to_dict()
                v6leases.append(v6leases_item)

        prefixes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.prefixes, Unset):
            prefixes = []
            for prefixes_item_data in self.prefixes:
                prefixes_item = prefixes_item_data.to_dict()
                prefixes.append(prefixes_item)

        interfaces: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = []
            for interfaces_item_data in self.interfaces:
                interfaces_item = interfaces_item_data.to_dict()
                interfaces.append(interfaces_item)

        interfacesv6: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.interfacesv6, Unset):
            interfacesv6 = []
            for interfacesv6_item_data in self.interfacesv6:
                interfacesv6_item = interfacesv6_item_data.to_dict()
                interfacesv6.append(interfacesv6_item)

        v4_ha_status: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.v4_ha_status, Unset):
            v4_ha_status = []
            for v4_ha_status_item_data in self.v4_ha_status:
                v4_ha_status_item = v4_ha_status_item_data.to_dict()
                v4_ha_status.append(v4_ha_status_item)

        v6_ha_status: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.v6_ha_status, Unset):
            v6_ha_status = []
            for v6_ha_status_item_data in self.v6_ha_status:
                v6_ha_status_item = v6_ha_status_item_data.to_dict()
                v6_ha_status.append(v6_ha_status_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if v4leases is not UNSET:
            field_dict["v4leases"] = v4leases
        if v6leases is not UNSET:
            field_dict["v6leases"] = v6leases
        if prefixes is not UNSET:
            field_dict["prefixes"] = prefixes
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces
        if interfacesv6 is not UNSET:
            field_dict["interfacesv6"] = interfacesv6
        if v4_ha_status is not UNSET:
            field_dict["v4_ha_status"] = v4_ha_status
        if v6_ha_status is not UNSET:
            field_dict["v6_ha_status"] = v6_ha_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dhcp_lease import DHCPLease
        from ..models.dhcpha_state import DHCPHAState
        from ..models.lease_interface import LeaseInterface

        d = src_dict.copy()
        v4leases = []
        _v4leases = d.pop("v4leases", UNSET)
        for v4leases_item_data in _v4leases or []:
            v4leases_item = DHCPLease.from_dict(v4leases_item_data)

            v4leases.append(v4leases_item)

        v6leases = []
        _v6leases = d.pop("v6leases", UNSET)
        for v6leases_item_data in _v6leases or []:
            v6leases_item = DHCPLease.from_dict(v6leases_item_data)

            v6leases.append(v6leases_item)

        prefixes = []
        _prefixes = d.pop("prefixes", UNSET)
        for prefixes_item_data in _prefixes or []:
            prefixes_item = DHCPLease.from_dict(prefixes_item_data)

            prefixes.append(prefixes_item)

        interfaces = []
        _interfaces = d.pop("interfaces", UNSET)
        for interfaces_item_data in _interfaces or []:
            interfaces_item = LeaseInterface.from_dict(interfaces_item_data)

            interfaces.append(interfaces_item)

        interfacesv6 = []
        _interfacesv6 = d.pop("interfacesv6", UNSET)
        for interfacesv6_item_data in _interfacesv6 or []:
            interfacesv6_item = LeaseInterface.from_dict(interfacesv6_item_data)

            interfacesv6.append(interfacesv6_item)

        v4_ha_status = []
        _v4_ha_status = d.pop("v4_ha_status", UNSET)
        for v4_ha_status_item_data in _v4_ha_status or []:
            v4_ha_status_item = DHCPHAState.from_dict(v4_ha_status_item_data)

            v4_ha_status.append(v4_ha_status_item)

        v6_ha_status = []
        _v6_ha_status = d.pop("v6_ha_status", UNSET)
        for v6_ha_status_item_data in _v6_ha_status or []:
            v6_ha_status_item = DHCPHAState.from_dict(v6_ha_status_item_data)

            v6_ha_status.append(v6_ha_status_item)

        dhcp_leases = cls(
            v4leases=v4leases,
            v6leases=v6leases,
            prefixes=prefixes,
            interfaces=interfaces,
            interfacesv6=interfacesv6,
            v4_ha_status=v4_ha_status,
            v6_ha_status=v6_ha_status,
        )

        dhcp_leases.additional_properties = d
        return dhcp_leases

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
