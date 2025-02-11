from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InterfaceInfo")


@_attrs_define
class InterfaceInfo:
    """
    Attributes:
        assigned_interface (str):
        internal_name (str):
        friendly_name (str):
        enabled (bool):
        status (str):
        mac_address (str):
        mtu (int):
        media (str):
        plugged (str):
        vendor (str):
        temperature (str):
        voltage (str):
        rx (str):
        tx (str):
        channel (int):
        ssid (str):
        bssid (str):
        rate (str):
        rssi (str):
        in_packets (int):
        out_packets (int):
        in_bytes (int):
        out_bytes (int):
        in_packets_pass (int):
        out_packets_pass (int):
        in_bytes_pass (int):
        out_bytes_pass (int):
        in_packets_block (int):
        out_packets_block (int):
        in_bytes_block (int):
        out_bytes_block (int):
        in_errors (int):
        out_errors (int):
        collisions (int):
        ip_address (str):
        subnet_mask (str):
        gateway (str):
        ipv6_link_local (str):
        ipv6_address (str):
        ipv6_subnet_mask (str):
        ipv6_gateway (str):
        lagg_enabled (bool):
        lagg_ports (str):
        current_ppp_uptime (str):
        historical_ppp_uptime (str):
        cell_rssi (str):
        cell_mode (str):
        cell_simstate (str):
        cell_service (str):
        cell_bwupstream (int):
        cell_bwdownstream (int):
        cell_upstream (int):
        cell_downstream (int):
        dhcplink (str):
        pppoelink (str):
        pptplink (str):
        dns_servers (Union[Unset, List[str]]):
    """

    assigned_interface: str
    internal_name: str
    friendly_name: str
    enabled: bool
    status: str
    mac_address: str
    mtu: int
    media: str
    plugged: str
    vendor: str
    temperature: str
    voltage: str
    rx: str
    tx: str
    channel: int
    ssid: str
    bssid: str
    rate: str
    rssi: str
    in_packets: int
    out_packets: int
    in_bytes: int
    out_bytes: int
    in_packets_pass: int
    out_packets_pass: int
    in_bytes_pass: int
    out_bytes_pass: int
    in_packets_block: int
    out_packets_block: int
    in_bytes_block: int
    out_bytes_block: int
    in_errors: int
    out_errors: int
    collisions: int
    ip_address: str
    subnet_mask: str
    gateway: str
    ipv6_link_local: str
    ipv6_address: str
    ipv6_subnet_mask: str
    ipv6_gateway: str
    lagg_enabled: bool
    lagg_ports: str
    current_ppp_uptime: str
    historical_ppp_uptime: str
    cell_rssi: str
    cell_mode: str
    cell_simstate: str
    cell_service: str
    cell_bwupstream: int
    cell_bwdownstream: int
    cell_upstream: int
    cell_downstream: int
    dhcplink: str
    pppoelink: str
    pptplink: str
    dns_servers: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        assigned_interface = self.assigned_interface

        internal_name = self.internal_name

        friendly_name = self.friendly_name

        enabled = self.enabled

        status = self.status

        mac_address = self.mac_address

        mtu = self.mtu

        media = self.media

        plugged = self.plugged

        vendor = self.vendor

        temperature = self.temperature

        voltage = self.voltage

        rx = self.rx

        tx = self.tx

        channel = self.channel

        ssid = self.ssid

        bssid = self.bssid

        rate = self.rate

        rssi = self.rssi

        in_packets = self.in_packets

        out_packets = self.out_packets

        in_bytes = self.in_bytes

        out_bytes = self.out_bytes

        in_packets_pass = self.in_packets_pass

        out_packets_pass = self.out_packets_pass

        in_bytes_pass = self.in_bytes_pass

        out_bytes_pass = self.out_bytes_pass

        in_packets_block = self.in_packets_block

        out_packets_block = self.out_packets_block

        in_bytes_block = self.in_bytes_block

        out_bytes_block = self.out_bytes_block

        in_errors = self.in_errors

        out_errors = self.out_errors

        collisions = self.collisions

        ip_address = self.ip_address

        subnet_mask = self.subnet_mask

        gateway = self.gateway

        ipv6_link_local = self.ipv6_link_local

        ipv6_address = self.ipv6_address

        ipv6_subnet_mask = self.ipv6_subnet_mask

        ipv6_gateway = self.ipv6_gateway

        lagg_enabled = self.lagg_enabled

        lagg_ports = self.lagg_ports

        current_ppp_uptime = self.current_ppp_uptime

        historical_ppp_uptime = self.historical_ppp_uptime

        cell_rssi = self.cell_rssi

        cell_mode = self.cell_mode

        cell_simstate = self.cell_simstate

        cell_service = self.cell_service

        cell_bwupstream = self.cell_bwupstream

        cell_bwdownstream = self.cell_bwdownstream

        cell_upstream = self.cell_upstream

        cell_downstream = self.cell_downstream

        dhcplink = self.dhcplink

        pppoelink = self.pppoelink

        pptplink = self.pptplink

        dns_servers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.dns_servers, Unset):
            dns_servers = self.dns_servers

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assigned_interface": assigned_interface,
                "internal_name": internal_name,
                "friendly_name": friendly_name,
                "enabled": enabled,
                "status": status,
                "mac_address": mac_address,
                "mtu": mtu,
                "media": media,
                "plugged": plugged,
                "vendor": vendor,
                "temperature": temperature,
                "voltage": voltage,
                "rx": rx,
                "tx": tx,
                "channel": channel,
                "ssid": ssid,
                "bssid": bssid,
                "rate": rate,
                "rssi": rssi,
                "in_packets": in_packets,
                "out_packets": out_packets,
                "in_bytes": in_bytes,
                "out_bytes": out_bytes,
                "in_packets_pass": in_packets_pass,
                "out_packets_pass": out_packets_pass,
                "in_bytes_pass": in_bytes_pass,
                "out_bytes_pass": out_bytes_pass,
                "in_packets_block": in_packets_block,
                "out_packets_block": out_packets_block,
                "in_bytes_block": in_bytes_block,
                "out_bytes_block": out_bytes_block,
                "in_errors": in_errors,
                "out_errors": out_errors,
                "collisions": collisions,
                "ip_address": ip_address,
                "subnet_mask": subnet_mask,
                "gateway": gateway,
                "ipv6_link_local": ipv6_link_local,
                "ipv6_address": ipv6_address,
                "ipv6_subnet_mask": ipv6_subnet_mask,
                "ipv6_gateway": ipv6_gateway,
                "lagg_enabled": lagg_enabled,
                "lagg_ports": lagg_ports,
                "current_ppp_uptime": current_ppp_uptime,
                "historical_ppp_uptime": historical_ppp_uptime,
                "cell_rssi": cell_rssi,
                "cell_mode": cell_mode,
                "cell_simstate": cell_simstate,
                "cell_service": cell_service,
                "cell_bwupstream": cell_bwupstream,
                "cell_bwdownstream": cell_bwdownstream,
                "cell_upstream": cell_upstream,
                "cell_downstream": cell_downstream,
                "dhcplink": dhcplink,
                "pppoelink": pppoelink,
                "pptplink": pptplink,
            }
        )
        if dns_servers is not UNSET:
            field_dict["dns_servers"] = dns_servers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        assigned_interface = d.pop("assigned_interface")

        internal_name = d.pop("internal_name")

        friendly_name = d.pop("friendly_name")

        enabled = d.pop("enabled")

        status = d.pop("status")

        mac_address = d.pop("mac_address")

        mtu = d.pop("mtu")

        media = d.pop("media")

        plugged = d.pop("plugged")

        vendor = d.pop("vendor")

        temperature = d.pop("temperature")

        voltage = d.pop("voltage")

        rx = d.pop("rx")

        tx = d.pop("tx")

        channel = d.pop("channel")

        ssid = d.pop("ssid")

        bssid = d.pop("bssid")

        rate = d.pop("rate")

        rssi = d.pop("rssi")

        in_packets = d.pop("in_packets")

        out_packets = d.pop("out_packets")

        in_bytes = d.pop("in_bytes")

        out_bytes = d.pop("out_bytes")

        in_packets_pass = d.pop("in_packets_pass")

        out_packets_pass = d.pop("out_packets_pass")

        in_bytes_pass = d.pop("in_bytes_pass")

        out_bytes_pass = d.pop("out_bytes_pass")

        in_packets_block = d.pop("in_packets_block")

        out_packets_block = d.pop("out_packets_block")

        in_bytes_block = d.pop("in_bytes_block")

        out_bytes_block = d.pop("out_bytes_block")

        in_errors = d.pop("in_errors")

        out_errors = d.pop("out_errors")

        collisions = d.pop("collisions")

        ip_address = d.pop("ip_address")

        subnet_mask = d.pop("subnet_mask")

        gateway = d.pop("gateway")

        ipv6_link_local = d.pop("ipv6_link_local")

        ipv6_address = d.pop("ipv6_address")

        ipv6_subnet_mask = d.pop("ipv6_subnet_mask")

        ipv6_gateway = d.pop("ipv6_gateway")

        lagg_enabled = d.pop("lagg_enabled")

        lagg_ports = d.pop("lagg_ports")

        current_ppp_uptime = d.pop("current_ppp_uptime")

        historical_ppp_uptime = d.pop("historical_ppp_uptime")

        cell_rssi = d.pop("cell_rssi")

        cell_mode = d.pop("cell_mode")

        cell_simstate = d.pop("cell_simstate")

        cell_service = d.pop("cell_service")

        cell_bwupstream = d.pop("cell_bwupstream")

        cell_bwdownstream = d.pop("cell_bwdownstream")

        cell_upstream = d.pop("cell_upstream")

        cell_downstream = d.pop("cell_downstream")

        dhcplink = d.pop("dhcplink")

        pppoelink = d.pop("pppoelink")

        pptplink = d.pop("pptplink")

        dns_servers = cast(List[str], d.pop("dns_servers", UNSET))

        interface_info = cls(
            assigned_interface=assigned_interface,
            internal_name=internal_name,
            friendly_name=friendly_name,
            enabled=enabled,
            status=status,
            mac_address=mac_address,
            mtu=mtu,
            media=media,
            plugged=plugged,
            vendor=vendor,
            temperature=temperature,
            voltage=voltage,
            rx=rx,
            tx=tx,
            channel=channel,
            ssid=ssid,
            bssid=bssid,
            rate=rate,
            rssi=rssi,
            in_packets=in_packets,
            out_packets=out_packets,
            in_bytes=in_bytes,
            out_bytes=out_bytes,
            in_packets_pass=in_packets_pass,
            out_packets_pass=out_packets_pass,
            in_bytes_pass=in_bytes_pass,
            out_bytes_pass=out_bytes_pass,
            in_packets_block=in_packets_block,
            out_packets_block=out_packets_block,
            in_bytes_block=in_bytes_block,
            out_bytes_block=out_bytes_block,
            in_errors=in_errors,
            out_errors=out_errors,
            collisions=collisions,
            ip_address=ip_address,
            subnet_mask=subnet_mask,
            gateway=gateway,
            ipv6_link_local=ipv6_link_local,
            ipv6_address=ipv6_address,
            ipv6_subnet_mask=ipv6_subnet_mask,
            ipv6_gateway=ipv6_gateway,
            lagg_enabled=lagg_enabled,
            lagg_ports=lagg_ports,
            current_ppp_uptime=current_ppp_uptime,
            historical_ppp_uptime=historical_ppp_uptime,
            cell_rssi=cell_rssi,
            cell_mode=cell_mode,
            cell_simstate=cell_simstate,
            cell_service=cell_service,
            cell_bwupstream=cell_bwupstream,
            cell_bwdownstream=cell_bwdownstream,
            cell_upstream=cell_upstream,
            cell_downstream=cell_downstream,
            dhcplink=dhcplink,
            pppoelink=pppoelink,
            pptplink=pptplink,
            dns_servers=dns_servers,
        )

        interface_info.additional_properties = d
        return interface_info

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
