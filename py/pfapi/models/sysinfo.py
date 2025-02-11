from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_service_basic import DeviceServiceBasic
    from ..models.sys_net_if import SysNetIf
    from ..models.sysinfo_fs import SysinfoFs


T = TypeVar("T", bound="Sysinfo")


@_attrs_define
class Sysinfo:
    """
    Attributes:
        hostname (str):
        serial (str):
        version (str): controller version
        device_id (str):
        crypto_id (str):
        product (str):
        product_version (str):
        product_build (str):
        os_name (str):
        os_version (str):
        bios_vendor (str):
        bios_type (str):
        bios_date (str):
        bios_version (str):
        cpu_model (str):
        cpu_cores (int):
        cpu_features (str):
        cpu_load (int):
        uptime (int):
        time (str):
        mem_total (int):
        mem_used (int):
        loadavg (List[int]):
        vendor (str):
        model (str):
        hw_uuid (str):
        mim_devices (int):
        address (Union[Unset, List[str]]):
        filesystems (Union[Unset, List['SysinfoFs']]):
        network_ports (Union[Unset, List['SysNetIf']]):
        services (Union[Unset, List['DeviceServiceBasic']]):
    """

    hostname: str
    serial: str
    version: str
    device_id: str
    crypto_id: str
    product: str
    product_version: str
    product_build: str
    os_name: str
    os_version: str
    bios_vendor: str
    bios_type: str
    bios_date: str
    bios_version: str
    cpu_model: str
    cpu_cores: int
    cpu_features: str
    cpu_load: int
    uptime: int
    time: str
    mem_total: int
    mem_used: int
    loadavg: List[int]
    vendor: str
    model: str
    hw_uuid: str
    mim_devices: int
    address: Union[Unset, List[str]] = UNSET
    filesystems: Union[Unset, List["SysinfoFs"]] = UNSET
    network_ports: Union[Unset, List["SysNetIf"]] = UNSET
    services: Union[Unset, List["DeviceServiceBasic"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hostname = self.hostname

        serial = self.serial

        version = self.version

        device_id = self.device_id

        crypto_id = self.crypto_id

        product = self.product

        product_version = self.product_version

        product_build = self.product_build

        os_name = self.os_name

        os_version = self.os_version

        bios_vendor = self.bios_vendor

        bios_type = self.bios_type

        bios_date = self.bios_date

        bios_version = self.bios_version

        cpu_model = self.cpu_model

        cpu_cores = self.cpu_cores

        cpu_features = self.cpu_features

        cpu_load = self.cpu_load

        uptime = self.uptime

        time = self.time

        mem_total = self.mem_total

        mem_used = self.mem_used

        loadavg = self.loadavg

        vendor = self.vendor

        model = self.model

        hw_uuid = self.hw_uuid

        mim_devices = self.mim_devices

        address: Union[Unset, List[str]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address

        filesystems: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.filesystems, Unset):
            filesystems = []
            for filesystems_item_data in self.filesystems:
                filesystems_item = filesystems_item_data.to_dict()
                filesystems.append(filesystems_item)

        network_ports: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.network_ports, Unset):
            network_ports = []
            for network_ports_item_data in self.network_ports:
                network_ports_item = network_ports_item_data.to_dict()
                network_ports.append(network_ports_item)

        services: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.services, Unset):
            services = []
            for services_item_data in self.services:
                services_item = services_item_data.to_dict()
                services.append(services_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hostname": hostname,
                "serial": serial,
                "version": version,
                "device_id": device_id,
                "crypto_id": crypto_id,
                "product": product,
                "product_version": product_version,
                "product_build": product_build,
                "os_name": os_name,
                "os_version": os_version,
                "bios_vendor": bios_vendor,
                "bios_type": bios_type,
                "bios_date": bios_date,
                "bios_version": bios_version,
                "cpu_model": cpu_model,
                "cpu_cores": cpu_cores,
                "cpu_features": cpu_features,
                "cpu_load": cpu_load,
                "uptime": uptime,
                "time": time,
                "mem_total": mem_total,
                "mem_used": mem_used,
                "loadavg": loadavg,
                "vendor": vendor,
                "model": model,
                "hw_uuid": hw_uuid,
                "mim_devices": mim_devices,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address
        if filesystems is not UNSET:
            field_dict["filesystems"] = filesystems
        if network_ports is not UNSET:
            field_dict["network_ports"] = network_ports
        if services is not UNSET:
            field_dict["services"] = services

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.device_service_basic import DeviceServiceBasic
        from ..models.sys_net_if import SysNetIf
        from ..models.sysinfo_fs import SysinfoFs

        d = src_dict.copy()
        hostname = d.pop("hostname")

        serial = d.pop("serial")

        version = d.pop("version")

        device_id = d.pop("device_id")

        crypto_id = d.pop("crypto_id")

        product = d.pop("product")

        product_version = d.pop("product_version")

        product_build = d.pop("product_build")

        os_name = d.pop("os_name")

        os_version = d.pop("os_version")

        bios_vendor = d.pop("bios_vendor")

        bios_type = d.pop("bios_type")

        bios_date = d.pop("bios_date")

        bios_version = d.pop("bios_version")

        cpu_model = d.pop("cpu_model")

        cpu_cores = d.pop("cpu_cores")

        cpu_features = d.pop("cpu_features")

        cpu_load = d.pop("cpu_load")

        uptime = d.pop("uptime")

        time = d.pop("time")

        mem_total = d.pop("mem_total")

        mem_used = d.pop("mem_used")

        loadavg = cast(List[int], d.pop("loadavg"))

        vendor = d.pop("vendor")

        model = d.pop("model")

        hw_uuid = d.pop("hw_uuid")

        mim_devices = d.pop("mim_devices")

        address = cast(List[str], d.pop("address", UNSET))

        filesystems = []
        _filesystems = d.pop("filesystems", UNSET)
        for filesystems_item_data in _filesystems or []:
            filesystems_item = SysinfoFs.from_dict(filesystems_item_data)

            filesystems.append(filesystems_item)

        network_ports = []
        _network_ports = d.pop("network_ports", UNSET)
        for network_ports_item_data in _network_ports or []:
            network_ports_item = SysNetIf.from_dict(network_ports_item_data)

            network_ports.append(network_ports_item)

        services = []
        _services = d.pop("services", UNSET)
        for services_item_data in _services or []:
            services_item = DeviceServiceBasic.from_dict(services_item_data)

            services.append(services_item)

        sysinfo = cls(
            hostname=hostname,
            serial=serial,
            version=version,
            device_id=device_id,
            crypto_id=crypto_id,
            product=product,
            product_version=product_version,
            product_build=product_build,
            os_name=os_name,
            os_version=os_version,
            bios_vendor=bios_vendor,
            bios_type=bios_type,
            bios_date=bios_date,
            bios_version=bios_version,
            cpu_model=cpu_model,
            cpu_cores=cpu_cores,
            cpu_features=cpu_features,
            cpu_load=cpu_load,
            uptime=uptime,
            time=time,
            mem_total=mem_total,
            mem_used=mem_used,
            loadavg=loadavg,
            vendor=vendor,
            model=model,
            hw_uuid=hw_uuid,
            mim_devices=mim_devices,
            address=address,
            filesystems=filesystems,
            network_ports=network_ports,
            services=services,
        )

        sysinfo.additional_properties = d
        return sysinfo

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
