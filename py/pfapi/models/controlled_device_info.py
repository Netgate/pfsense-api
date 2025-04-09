from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_network_port import DeviceNetworkPort
    from ..models.device_service_basic import DeviceServiceBasic


T = TypeVar("T", bound="ControlledDeviceInfo")


@_attrs_define
class ControlledDeviceInfo:
    """Additional information about the device

    Attributes:
        hostname (Union[Unset, str]):
        uptime (Union[Unset, int]): number of seconds since the device started
        network_ports (Union[Unset, List['DeviceNetworkPort']]):
        services (Union[Unset, List['DeviceServiceBasic']]):
        product (Union[Unset, str]): eg pfsense
        product_version (Union[Unset, str]): eg 24.08
        product_build (Union[Unset, str]):
        os_name (Union[Unset, str]):
        os_version (Union[Unset, str]):
        cpu (Union[Unset, str]):
        memory (Union[Unset, int]):
        model (Union[Unset, str]):
        vendor (Union[Unset, str]):
        serial (Union[Unset, str]):
        hw_uuid (Union[Unset, str]):
    """

    hostname: Union[Unset, str] = UNSET
    uptime: Union[Unset, int] = UNSET
    network_ports: Union[Unset, List["DeviceNetworkPort"]] = UNSET
    services: Union[Unset, List["DeviceServiceBasic"]] = UNSET
    product: Union[Unset, str] = UNSET
    product_version: Union[Unset, str] = UNSET
    product_build: Union[Unset, str] = UNSET
    os_name: Union[Unset, str] = UNSET
    os_version: Union[Unset, str] = UNSET
    cpu: Union[Unset, str] = UNSET
    memory: Union[Unset, int] = UNSET
    model: Union[Unset, str] = UNSET
    vendor: Union[Unset, str] = UNSET
    serial: Union[Unset, str] = UNSET
    hw_uuid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hostname = self.hostname

        uptime = self.uptime

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

        product = self.product

        product_version = self.product_version

        product_build = self.product_build

        os_name = self.os_name

        os_version = self.os_version

        cpu = self.cpu

        memory = self.memory

        model = self.model

        vendor = self.vendor

        serial = self.serial

        hw_uuid = self.hw_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if uptime is not UNSET:
            field_dict["uptime"] = uptime
        if network_ports is not UNSET:
            field_dict["network_ports"] = network_ports
        if services is not UNSET:
            field_dict["services"] = services
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
        if cpu is not UNSET:
            field_dict["cpu"] = cpu
        if memory is not UNSET:
            field_dict["memory"] = memory
        if model is not UNSET:
            field_dict["model"] = model
        if vendor is not UNSET:
            field_dict["vendor"] = vendor
        if serial is not UNSET:
            field_dict["serial"] = serial
        if hw_uuid is not UNSET:
            field_dict["hw_uuid"] = hw_uuid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.device_network_port import DeviceNetworkPort
        from ..models.device_service_basic import DeviceServiceBasic

        d = src_dict.copy()
        hostname = d.pop("hostname", UNSET)

        uptime = d.pop("uptime", UNSET)

        network_ports = []
        _network_ports = d.pop("network_ports", UNSET)
        for network_ports_item_data in _network_ports or []:
            network_ports_item = DeviceNetworkPort.from_dict(network_ports_item_data)

            network_ports.append(network_ports_item)

        services = []
        _services = d.pop("services", UNSET)
        for services_item_data in _services or []:
            services_item = DeviceServiceBasic.from_dict(services_item_data)

            services.append(services_item)

        product = d.pop("product", UNSET)

        product_version = d.pop("product_version", UNSET)

        product_build = d.pop("product_build", UNSET)

        os_name = d.pop("os_name", UNSET)

        os_version = d.pop("os_version", UNSET)

        cpu = d.pop("cpu", UNSET)

        memory = d.pop("memory", UNSET)

        model = d.pop("model", UNSET)

        vendor = d.pop("vendor", UNSET)

        serial = d.pop("serial", UNSET)

        hw_uuid = d.pop("hw_uuid", UNSET)

        controlled_device_info = cls(
            hostname=hostname,
            uptime=uptime,
            network_ports=network_ports,
            services=services,
            product=product,
            product_version=product_version,
            product_build=product_build,
            os_name=os_name,
            os_version=os_version,
            cpu=cpu,
            memory=memory,
            model=model,
            vendor=vendor,
            serial=serial,
            hw_uuid=hw_uuid,
        )

        controlled_device_info.additional_properties = d
        return controlled_device_info

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
