from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nexus_controller_info import NexusControllerInfo


T = TypeVar("T", bound="SystemStatus")


@_attrs_define
class SystemStatus:
    """
    Attributes:
        prod (str):
        host (str):
        osver (str):
        os (str):
        machine (str):
        arch (str):
        vndr (str):
        cores (int):
        cpu (str):
        up (str):
        rev (str):
        ram (int):
        fram (int):
        swap (int):
        fswap (int):
        timestamp (str):
        apiver (str):
        vpn_addr (str):
        nexus_controllers (Union[Unset, List['NexusControllerInfo']]):
    """

    prod: str
    host: str
    osver: str
    os: str
    machine: str
    arch: str
    vndr: str
    cores: int
    cpu: str
    up: str
    rev: str
    ram: int
    fram: int
    swap: int
    fswap: int
    timestamp: str
    apiver: str
    vpn_addr: str
    nexus_controllers: Union[Unset, List["NexusControllerInfo"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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

        nexus_controllers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.nexus_controllers, Unset):
            nexus_controllers = []
            for nexus_controllers_item_data in self.nexus_controllers:
                nexus_controllers_item = nexus_controllers_item_data.to_dict()
                nexus_controllers.append(nexus_controllers_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "prod": prod,
                "host": host,
                "osver": osver,
                "os": os,
                "machine": machine,
                "arch": arch,
                "vndr": vndr,
                "cores": cores,
                "cpu": cpu,
                "up": up,
                "rev": rev,
                "ram": ram,
                "fram": fram,
                "swap": swap,
                "fswap": fswap,
                "timestamp": timestamp,
                "apiver": apiver,
                "vpn_addr": vpn_addr,
            }
        )
        if nexus_controllers is not UNSET:
            field_dict["nexus_controllers"] = nexus_controllers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nexus_controller_info import NexusControllerInfo

        d = src_dict.copy()
        prod = d.pop("prod")

        host = d.pop("host")

        osver = d.pop("osver")

        os = d.pop("os")

        machine = d.pop("machine")

        arch = d.pop("arch")

        vndr = d.pop("vndr")

        cores = d.pop("cores")

        cpu = d.pop("cpu")

        up = d.pop("up")

        rev = d.pop("rev")

        ram = d.pop("ram")

        fram = d.pop("fram")

        swap = d.pop("swap")

        fswap = d.pop("fswap")

        timestamp = d.pop("timestamp")

        apiver = d.pop("apiver")

        vpn_addr = d.pop("vpn_addr")

        nexus_controllers = []
        _nexus_controllers = d.pop("nexus_controllers", UNSET)
        for nexus_controllers_item_data in _nexus_controllers or []:
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
            nexus_controllers=nexus_controllers,
        )

        system_status.additional_properties = d
        return system_status

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
