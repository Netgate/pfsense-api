from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.netif_status import NetifStatus
    from ..models.nexus_controller_info import NexusControllerInfo


T = TypeVar("T", bound="SystemStatus")


@_attrs_define
class SystemStatus:
    """
    Attributes:
        prod (str | Unset):
        host (str | Unset):
        osver (str | Unset):
        os (str | Unset):
        machine (str | Unset):
        arch (str | Unset):
        vndr (str | Unset):
        cores (int | Unset):
        cpu (str | Unset):
        up (str | Unset):
        rev (str | Unset):
        ram (int | Unset):
        fram (int | Unset):
        swap (int | Unset):
        fswap (int | Unset):
        timestamp (str | Unset):
        apiver (str | Unset):
        vpn_addr (str | Unset):
        alerts (str | Unset):
        net_interfaces (list[NetifStatus] | Unset):
        nexus_controllers (list[NexusControllerInfo] | Unset):
    """

    prod: str | Unset = UNSET
    host: str | Unset = UNSET
    osver: str | Unset = UNSET
    os: str | Unset = UNSET
    machine: str | Unset = UNSET
    arch: str | Unset = UNSET
    vndr: str | Unset = UNSET
    cores: int | Unset = UNSET
    cpu: str | Unset = UNSET
    up: str | Unset = UNSET
    rev: str | Unset = UNSET
    ram: int | Unset = UNSET
    fram: int | Unset = UNSET
    swap: int | Unset = UNSET
    fswap: int | Unset = UNSET
    timestamp: str | Unset = UNSET
    apiver: str | Unset = UNSET
    vpn_addr: str | Unset = UNSET
    alerts: str | Unset = UNSET
    net_interfaces: list[NetifStatus] | Unset = UNSET
    nexus_controllers: list[NexusControllerInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prod = self.prod

        host = self.host

        osver = self.osver

        os = self.os

        machine = self.machine

        arch = self.arch

        vndr = self.vndr

        cores = self.cores

        cpu = self.cpu

        up = self.up

        rev = self.rev

        ram = self.ram

        fram = self.fram

        swap = self.swap

        fswap = self.fswap

        timestamp = self.timestamp

        apiver = self.apiver

        vpn_addr = self.vpn_addr

        alerts = self.alerts

        net_interfaces: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.net_interfaces, Unset):
            net_interfaces = []
            for net_interfaces_item_data in self.net_interfaces:
                net_interfaces_item = net_interfaces_item_data.to_dict()
                net_interfaces.append(net_interfaces_item)

        nexus_controllers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.nexus_controllers, Unset):
            nexus_controllers = []
            for nexus_controllers_item_data in self.nexus_controllers:
                nexus_controllers_item = nexus_controllers_item_data.to_dict()
                nexus_controllers.append(nexus_controllers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if prod is not UNSET:
            field_dict["prod"] = prod
        if host is not UNSET:
            field_dict["host"] = host
        if osver is not UNSET:
            field_dict["osver"] = osver
        if os is not UNSET:
            field_dict["os"] = os
        if machine is not UNSET:
            field_dict["machine"] = machine
        if arch is not UNSET:
            field_dict["arch"] = arch
        if vndr is not UNSET:
            field_dict["vndr"] = vndr
        if cores is not UNSET:
            field_dict["cores"] = cores
        if cpu is not UNSET:
            field_dict["cpu"] = cpu
        if up is not UNSET:
            field_dict["up"] = up
        if rev is not UNSET:
            field_dict["rev"] = rev
        if ram is not UNSET:
            field_dict["ram"] = ram
        if fram is not UNSET:
            field_dict["fram"] = fram
        if swap is not UNSET:
            field_dict["swap"] = swap
        if fswap is not UNSET:
            field_dict["fswap"] = fswap
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if apiver is not UNSET:
            field_dict["apiver"] = apiver
        if vpn_addr is not UNSET:
            field_dict["vpn_addr"] = vpn_addr
        if alerts is not UNSET:
            field_dict["alerts"] = alerts
        if net_interfaces is not UNSET:
            field_dict["net_interfaces"] = net_interfaces
        if nexus_controllers is not UNSET:
            field_dict["nexus_controllers"] = nexus_controllers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.netif_status import NetifStatus
        from ..models.nexus_controller_info import NexusControllerInfo

        d = dict(src_dict)
        prod = d.pop("prod", UNSET)

        host = d.pop("host", UNSET)

        osver = d.pop("osver", UNSET)

        os = d.pop("os", UNSET)

        machine = d.pop("machine", UNSET)

        arch = d.pop("arch", UNSET)

        vndr = d.pop("vndr", UNSET)

        cores = d.pop("cores", UNSET)

        cpu = d.pop("cpu", UNSET)

        up = d.pop("up", UNSET)

        rev = d.pop("rev", UNSET)

        ram = d.pop("ram", UNSET)

        fram = d.pop("fram", UNSET)

        swap = d.pop("swap", UNSET)

        fswap = d.pop("fswap", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        apiver = d.pop("apiver", UNSET)

        vpn_addr = d.pop("vpn_addr", UNSET)

        alerts = d.pop("alerts", UNSET)

        _net_interfaces = d.pop("net_interfaces", UNSET)
        net_interfaces: list[NetifStatus] | Unset = UNSET
        if _net_interfaces is not UNSET:
            net_interfaces = []
            for net_interfaces_item_data in _net_interfaces:
                net_interfaces_item = NetifStatus.from_dict(net_interfaces_item_data)

                net_interfaces.append(net_interfaces_item)

        _nexus_controllers = d.pop("nexus_controllers", UNSET)
        nexus_controllers: list[NexusControllerInfo] | Unset = UNSET
        if _nexus_controllers is not UNSET:
            nexus_controllers = []
            for nexus_controllers_item_data in _nexus_controllers:
                nexus_controllers_item = NexusControllerInfo.from_dict(nexus_controllers_item_data)

                nexus_controllers.append(nexus_controllers_item)

        system_status = cls(
            prod=prod,
            host=host,
            osver=osver,
            os=os,
            machine=machine,
            arch=arch,
            vndr=vndr,
            cores=cores,
            cpu=cpu,
            up=up,
            rev=rev,
            ram=ram,
            fram=fram,
            swap=swap,
            fswap=fswap,
            timestamp=timestamp,
            apiver=apiver,
            vpn_addr=vpn_addr,
            alerts=alerts,
            net_interfaces=net_interfaces,
            nexus_controllers=nexus_controllers,
        )

        system_status.additional_properties = d
        return system_status

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
