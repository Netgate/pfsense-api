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
        hostname (str):
        uptime (int): number of seconds since the device started
        product (str): eg pfsense
        product_version (str): eg 24.08
        product_build (str):
        os_name (str):
        os_version (str):
        cpu (str):
        memory (int):
        model (str):
        vendor (str):
        serial (str):
        hw_uuid (str):
        network_ports (Union[Unset, List['DeviceNetworkPort']]):
        services (Union[Unset, List['DeviceServiceBasic']]):
    """

    hostname: str
    uptime: int
    product: str
    product_version: str
    product_build: str
    os_name: str
    os_version: str
    cpu: str
    memory: int
    model: str
    vendor: str
    serial: str
    hw_uuid: str
    network_ports: Union[Unset, List["DeviceNetworkPort"]] = UNSET
    services: Union[Unset, List["DeviceServiceBasic"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hostname = self.hostname

        uptime = self.uptime

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
                "uptime": uptime,
                "product": product,
                "product_version": product_version,
                "product_build": product_build,
                "os_name": os_name,
                "os_version": os_version,
                "cpu": cpu,
                "memory": memory,
                "model": model,
                "vendor": vendor,
                "serial": serial,
                "hw_uuid": hw_uuid,
            }
        )
        if network_ports is not UNSET:
            field_dict["network_ports"] = network_ports
        if services is not UNSET:
            field_dict["services"] = services

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.device_network_port import DeviceNetworkPort
        from ..models.device_service_basic import DeviceServiceBasic

        d = src_dict.copy()
        hostname = d.pop("hostname")

        uptime = d.pop("uptime")

        product = d.pop("product")

        product_version = d.pop("product_version")

        product_build = d.pop("product_build")

        os_name = d.pop("os_name")

        os_version = d.pop("os_version")

        cpu = d.pop("cpu")

        memory = d.pop("memory")

        model = d.pop("model")

        vendor = d.pop("vendor")

        serial = d.pop("serial")

        hw_uuid = d.pop("hw_uuid")

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

        controlled_device_info = cls(
            hostname=hostname,
            uptime=uptime,
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
            network_ports=network_ports,
            services=services,
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
