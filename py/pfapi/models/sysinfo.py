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
        hostname (Union[Unset, str]):
        address (Union[Unset, List[str]]):
        serial (Union[Unset, str]):
        version (Union[Unset, str]): controller version
        device_id (Union[Unset, str]):
        crypto_id (Union[Unset, str]):
        product (Union[Unset, str]):
        product_version (Union[Unset, str]):
        product_build (Union[Unset, str]):
        os_name (Union[Unset, str]):
        os_version (Union[Unset, str]):
        bios_vendor (Union[Unset, str]):
        bios_type (Union[Unset, str]):
        bios_date (Union[Unset, str]):
        bios_version (Union[Unset, str]):
        cpu_model (Union[Unset, str]):
        cpu_cores (Union[Unset, int]):
        cpu_features (Union[Unset, str]):
        cpu_load (Union[Unset, int]):
        uptime (Union[Unset, int]):
        time (Union[Unset, str]):
        mem_total (Union[Unset, int]):
        mem_used (Union[Unset, int]):
        loadavg (Union[Unset, List[int]]):
        vendor (Union[Unset, str]):
        model (Union[Unset, str]):
        hw_uuid (Union[Unset, str]):
        filesystems (Union[Unset, List['SysinfoFs']]):
        network_ports (Union[Unset, List['SysNetIf']]):
        services (Union[Unset, List['DeviceServiceBasic']]):
        mim_devices (Union[Unset, int]):
    """

    hostname: Union[Unset, str] = UNSET
    address: Union[Unset, List[str]] = UNSET
    serial: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    device_id: Union[Unset, str] = UNSET
    crypto_id: Union[Unset, str] = UNSET
    product: Union[Unset, str] = UNSET
    product_version: Union[Unset, str] = UNSET
    product_build: Union[Unset, str] = UNSET
    os_name: Union[Unset, str] = UNSET
    os_version: Union[Unset, str] = UNSET
    bios_vendor: Union[Unset, str] = UNSET
    bios_type: Union[Unset, str] = UNSET
    bios_date: Union[Unset, str] = UNSET
    bios_version: Union[Unset, str] = UNSET
    cpu_model: Union[Unset, str] = UNSET
    cpu_cores: Union[Unset, int] = UNSET
    cpu_features: Union[Unset, str] = UNSET
    cpu_load: Union[Unset, int] = UNSET
    uptime: Union[Unset, int] = UNSET
    time: Union[Unset, str] = UNSET
    mem_total: Union[Unset, int] = UNSET
    mem_used: Union[Unset, int] = UNSET
    loadavg: Union[Unset, List[int]] = UNSET
    vendor: Union[Unset, str] = UNSET
    model: Union[Unset, str] = UNSET
    hw_uuid: Union[Unset, str] = UNSET
    filesystems: Union[Unset, List["SysinfoFs"]] = UNSET
    network_ports: Union[Unset, List["SysNetIf"]] = UNSET
    services: Union[Unset, List["DeviceServiceBasic"]] = UNSET
    mim_devices: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hostname = self.hostname

        address: Union[Unset, List[str]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address

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

        loadavg: Union[Unset, List[int]] = UNSET
        if not isinstance(self.loadavg, Unset):
            loadavg = self.loadavg

        vendor = self.vendor

        model = self.model

        hw_uuid = self.hw_uuid

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

        mim_devices = self.mim_devices

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if address is not UNSET:
            field_dict["address"] = address
        if serial is not UNSET:
            field_dict["serial"] = serial
        if version is not UNSET:
            field_dict["version"] = version
        if device_id is not UNSET:
            field_dict["device_id"] = device_id
        if crypto_id is not UNSET:
            field_dict["crypto_id"] = crypto_id
        if product is not UNSET:
            field_dict["product"] = product
        if product_version is not UNSET:
            field_dict["product_version"] = product_version
        if product_build is not UNSET:
            field_dict["product_build"] = product_build
        if os_name is not UNSET:
            field_dict["os_name"] = os_name
        if os_version is not UNSET:
            field_dict["os_version"] = os_version
        if bios_vendor is not UNSET:
            field_dict["bios_vendor"] = bios_vendor
        if bios_type is not UNSET:
            field_dict["bios_type"] = bios_type
        if bios_date is not UNSET:
            field_dict["bios_date"] = bios_date
        if bios_version is not UNSET:
            field_dict["bios_version"] = bios_version
        if cpu_model is not UNSET:
            field_dict["cpu_model"] = cpu_model
        if cpu_cores is not UNSET:
            field_dict["cpu_cores"] = cpu_cores
        if cpu_features is not UNSET:
            field_dict["cpu_features"] = cpu_features
        if cpu_load is not UNSET:
            field_dict["cpu_load"] = cpu_load
        if uptime is not UNSET:
            field_dict["uptime"] = uptime
        if time is not UNSET:
            field_dict["time"] = time
        if mem_total is not UNSET:
            field_dict["mem_total"] = mem_total
        if mem_used is not UNSET:
            field_dict["mem_used"] = mem_used
        if loadavg is not UNSET:
            field_dict["loadavg"] = loadavg
        if vendor is not UNSET:
            field_dict["vendor"] = vendor
        if model is not UNSET:
            field_dict["model"] = model
        if hw_uuid is not UNSET:
            field_dict["hw_uuid"] = hw_uuid
        if filesystems is not UNSET:
            field_dict["filesystems"] = filesystems
        if network_ports is not UNSET:
            field_dict["network_ports"] = network_ports
        if services is not UNSET:
            field_dict["services"] = services
        if mim_devices is not UNSET:
            field_dict["mim_devices"] = mim_devices

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.device_service_basic import DeviceServiceBasic
        from ..models.sys_net_if import SysNetIf
        from ..models.sysinfo_fs import SysinfoFs

        d = src_dict.copy()
        hostname = d.pop("hostname", UNSET)

        address = cast(List[str], d.pop("address", UNSET))

        serial = d.pop("serial", UNSET)

        version = d.pop("version", UNSET)

        device_id = d.pop("device_id", UNSET)

        crypto_id = d.pop("crypto_id", UNSET)

        product = d.pop("product", UNSET)

        product_version = d.pop("product_version", UNSET)

        product_build = d.pop("product_build", UNSET)

        os_name = d.pop("os_name", UNSET)

        os_version = d.pop("os_version", UNSET)

        bios_vendor = d.pop("bios_vendor", UNSET)

        bios_type = d.pop("bios_type", UNSET)

        bios_date = d.pop("bios_date", UNSET)

        bios_version = d.pop("bios_version", UNSET)

        cpu_model = d.pop("cpu_model", UNSET)

        cpu_cores = d.pop("cpu_cores", UNSET)

        cpu_features = d.pop("cpu_features", UNSET)

        cpu_load = d.pop("cpu_load", UNSET)

        uptime = d.pop("uptime", UNSET)

        time = d.pop("time", UNSET)

        mem_total = d.pop("mem_total", UNSET)

        mem_used = d.pop("mem_used", UNSET)

        loadavg = cast(List[int], d.pop("loadavg", UNSET))

        vendor = d.pop("vendor", UNSET)

        model = d.pop("model", UNSET)

        hw_uuid = d.pop("hw_uuid", UNSET)

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

        mim_devices = d.pop("mim_devices", UNSET)

        sysinfo = cls(
            hostname=hostname,
            address=address,
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
            filesystems=filesystems,
            network_ports=network_ports,
            services=services,
            mim_devices=mim_devices,
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
