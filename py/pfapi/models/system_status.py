from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SystemStatus")


@_attrs_define
class SystemStatus:
    """
    Attributes:
        prod (Union[Unset, str]):
        host (Union[Unset, str]):
        osver (Union[Unset, str]):
        os (Union[Unset, str]):
        machine (Union[Unset, str]):
        arch (Union[Unset, str]):
        vndr (Union[Unset, str]):
        cores (Union[Unset, int]):
        cpu (Union[Unset, str]):
        up (Union[Unset, str]):
        rev (Union[Unset, str]):
        ram (Union[Unset, int]):
        fram (Union[Unset, int]):
        swap (Union[Unset, int]):
        fswap (Union[Unset, int]):
        timestamp (Union[Unset, str]):
        apiver (Union[Unset, str]):
    """

    prod: Union[Unset, str] = UNSET
    host: Union[Unset, str] = UNSET
    osver: Union[Unset, str] = UNSET
    os: Union[Unset, str] = UNSET
    machine: Union[Unset, str] = UNSET
    arch: Union[Unset, str] = UNSET
    vndr: Union[Unset, str] = UNSET
    cores: Union[Unset, int] = UNSET
    cpu: Union[Unset, str] = UNSET
    up: Union[Unset, str] = UNSET
    rev: Union[Unset, str] = UNSET
    ram: Union[Unset, int] = UNSET
    fram: Union[Unset, int] = UNSET
    swap: Union[Unset, int] = UNSET
    fswap: Union[Unset, int] = UNSET
    timestamp: Union[Unset, str] = UNSET
    apiver: Union[Unset, str] = UNSET
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

        field_dict: Dict[str, Any] = {}
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
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
