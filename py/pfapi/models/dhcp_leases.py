from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

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
        v4leases (list[DHCPLease] | Unset):
        v6leases (list[DHCPLease] | Unset):
        prefixes (list[DHCPLease] | Unset):
        interfaces (list[LeaseInterface] | Unset):
        interfacesv6 (list[LeaseInterface] | Unset):
        v4_ha_status (list[DHCPHAState] | Unset):
        v6_ha_status (list[DHCPHAState] | Unset):
    """

    v4leases: list[DHCPLease] | Unset = UNSET
    v6leases: list[DHCPLease] | Unset = UNSET
    prefixes: list[DHCPLease] | Unset = UNSET
    interfaces: list[LeaseInterface] | Unset = UNSET
    interfacesv6: list[LeaseInterface] | Unset = UNSET
    v4_ha_status: list[DHCPHAState] | Unset = UNSET
    v6_ha_status: list[DHCPHAState] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        v4leases: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.v4leases, Unset):
            v4leases = []
            for v4leases_item_data in self.v4leases:
                v4leases_item = v4leases_item_data.to_dict()
                v4leases.append(v4leases_item)

        v6leases: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.v6leases, Unset):
            v6leases = []
            for v6leases_item_data in self.v6leases:
                v6leases_item = v6leases_item_data.to_dict()
                v6leases.append(v6leases_item)

        prefixes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.prefixes, Unset):
            prefixes = []
            for prefixes_item_data in self.prefixes:
                prefixes_item = prefixes_item_data.to_dict()
                prefixes.append(prefixes_item)

        interfaces: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = []
            for interfaces_item_data in self.interfaces:
                interfaces_item = interfaces_item_data.to_dict()
                interfaces.append(interfaces_item)

        interfacesv6: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.interfacesv6, Unset):
            interfacesv6 = []
            for interfacesv6_item_data in self.interfacesv6:
                interfacesv6_item = interfacesv6_item_data.to_dict()
                interfacesv6.append(interfacesv6_item)

        v4_ha_status: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.v4_ha_status, Unset):
            v4_ha_status = []
            for v4_ha_status_item_data in self.v4_ha_status:
                v4_ha_status_item = v4_ha_status_item_data.to_dict()
                v4_ha_status.append(v4_ha_status_item)

        v6_ha_status: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.v6_ha_status, Unset):
            v6_ha_status = []
            for v6_ha_status_item_data in self.v6_ha_status:
                v6_ha_status_item = v6_ha_status_item_data.to_dict()
                v6_ha_status.append(v6_ha_status_item)

        field_dict: dict[str, Any] = {}
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
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dhcp_lease import DHCPLease
        from ..models.dhcpha_state import DHCPHAState
        from ..models.lease_interface import LeaseInterface

        d = dict(src_dict)
        _v4leases = d.pop("v4leases", UNSET)
        v4leases: list[DHCPLease] | Unset = UNSET
        if _v4leases is not UNSET:
            v4leases = []
            for v4leases_item_data in _v4leases:
                v4leases_item = DHCPLease.from_dict(v4leases_item_data)

                v4leases.append(v4leases_item)

        _v6leases = d.pop("v6leases", UNSET)
        v6leases: list[DHCPLease] | Unset = UNSET
        if _v6leases is not UNSET:
            v6leases = []
            for v6leases_item_data in _v6leases:
                v6leases_item = DHCPLease.from_dict(v6leases_item_data)

                v6leases.append(v6leases_item)

        _prefixes = d.pop("prefixes", UNSET)
        prefixes: list[DHCPLease] | Unset = UNSET
        if _prefixes is not UNSET:
            prefixes = []
            for prefixes_item_data in _prefixes:
                prefixes_item = DHCPLease.from_dict(prefixes_item_data)

                prefixes.append(prefixes_item)

        _interfaces = d.pop("interfaces", UNSET)
        interfaces: list[LeaseInterface] | Unset = UNSET
        if _interfaces is not UNSET:
            interfaces = []
            for interfaces_item_data in _interfaces:
                interfaces_item = LeaseInterface.from_dict(interfaces_item_data)

                interfaces.append(interfaces_item)

        _interfacesv6 = d.pop("interfacesv6", UNSET)
        interfacesv6: list[LeaseInterface] | Unset = UNSET
        if _interfacesv6 is not UNSET:
            interfacesv6 = []
            for interfacesv6_item_data in _interfacesv6:
                interfacesv6_item = LeaseInterface.from_dict(interfacesv6_item_data)

                interfacesv6.append(interfacesv6_item)

        _v4_ha_status = d.pop("v4_ha_status", UNSET)
        v4_ha_status: list[DHCPHAState] | Unset = UNSET
        if _v4_ha_status is not UNSET:
            v4_ha_status = []
            for v4_ha_status_item_data in _v4_ha_status:
                v4_ha_status_item = DHCPHAState.from_dict(v4_ha_status_item_data)

                v4_ha_status.append(v4_ha_status_item)

        _v6_ha_status = d.pop("v6_ha_status", UNSET)
        v6_ha_status: list[DHCPHAState] | Unset = UNSET
        if _v6_ha_status is not UNSET:
            v6_ha_status = []
            for v6_ha_status_item_data in _v6_ha_status:
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
