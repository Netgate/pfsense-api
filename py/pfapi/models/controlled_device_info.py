from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_network_port import DeviceNetworkPort
    from ..models.device_service_basic import DeviceServiceBasic
    from ..models.sysinfo_license import SysinfoLicense


T = TypeVar("T", bound="ControlledDeviceInfo")


@_attrs_define
class ControlledDeviceInfo:
    """Additional information about the device

    Attributes:
        hostname (str | Unset):
        uptime (int | Unset): number of seconds since the device started
        network_ports (list[DeviceNetworkPort] | Unset):
        services (list[DeviceServiceBasic] | Unset):
        product (str | Unset): eg pfsense
        product_version (str | Unset): eg 24.08
        product_build (str | Unset):
        os_name (str | Unset):
        os_version (str | Unset):
        cpu (str | Unset):
        memory (int | Unset):
        model (str | Unset):
        vendor (str | Unset):
        serial (str | Unset):
        hw_uuid (str | Unset):
        gateways (list[str] | Unset):
        license_ (SysinfoLicense | Unset):
    """

    hostname: str | Unset = UNSET
    uptime: int | Unset = UNSET
    network_ports: list[DeviceNetworkPort] | Unset = UNSET
    services: list[DeviceServiceBasic] | Unset = UNSET
    product: str | Unset = UNSET
    product_version: str | Unset = UNSET
    product_build: str | Unset = UNSET
    os_name: str | Unset = UNSET
    os_version: str | Unset = UNSET
    cpu: str | Unset = UNSET
    memory: int | Unset = UNSET
    model: str | Unset = UNSET
    vendor: str | Unset = UNSET
    serial: str | Unset = UNSET
    hw_uuid: str | Unset = UNSET
    gateways: list[str] | Unset = UNSET
    license_: SysinfoLicense | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hostname = self.hostname

        uptime = self.uptime

        network_ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.network_ports, Unset):
            network_ports = []
            for network_ports_item_data in self.network_ports:
                network_ports_item = network_ports_item_data.to_dict()
                network_ports.append(network_ports_item)

        services: list[dict[str, Any]] | Unset = UNSET
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

        gateways: list[str] | Unset = UNSET
        if not isinstance(self.gateways, Unset):
            gateways = self.gateways

        license_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.license_, Unset):
            license_ = self.license_.to_dict()

        field_dict: dict[str, Any] = {}
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
        if gateways is not UNSET:
            field_dict["gateways"] = gateways
        if license_ is not UNSET:
            field_dict["license"] = license_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.device_network_port import DeviceNetworkPort
        from ..models.device_service_basic import DeviceServiceBasic
        from ..models.sysinfo_license import SysinfoLicense

        d = dict(src_dict)
        hostname = d.pop("hostname", UNSET)

        uptime = d.pop("uptime", UNSET)

        _network_ports = d.pop("network_ports", UNSET)
        network_ports: list[DeviceNetworkPort] | Unset = UNSET
        if _network_ports is not UNSET:
            network_ports = []
            for network_ports_item_data in _network_ports:
                network_ports_item = DeviceNetworkPort.from_dict(network_ports_item_data)

                network_ports.append(network_ports_item)

        _services = d.pop("services", UNSET)
        services: list[DeviceServiceBasic] | Unset = UNSET
        if _services is not UNSET:
            services = []
            for services_item_data in _services:
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

        gateways = cast(list[str], d.pop("gateways", UNSET))

        _license_ = d.pop("license", UNSET)
        license_: SysinfoLicense | Unset
        if isinstance(_license_, Unset):
            license_ = UNSET
        else:
            license_ = SysinfoLicense.from_dict(_license_)

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
            gateways=gateways,
            license_=license_,
        )

        controlled_device_info.additional_properties = d
        return controlled_device_info

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
