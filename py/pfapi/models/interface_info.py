from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InterfaceInfo")


@_attrs_define
class InterfaceInfo:
    """
    Attributes:
        assigned_interface (str | Unset): alias to device
        internal_name (str | Unset): alias to identity
        friendly_name (str | Unset): alias to assigned_name
        assigned_name (str | Unset):
        identity (str | Unset):
        device (str | Unset):
        enabled (bool | Unset):
        status (str | Unset):
        mac_address (str | Unset):
        mtu (int | Unset):
        media (str | Unset):
        plugged (str | Unset):
        vendor (str | Unset):
        temperature (str | Unset):
        voltage (str | Unset):
        rx (str | Unset):
        tx (str | Unset):
        channel (int | Unset):
        ssid (str | Unset):
        bssid (str | Unset):
        rate (str | Unset):
        rssi (str | Unset):
        in_packets (int | Unset):
        out_packets (int | Unset):
        in_bytes (int | Unset):
        out_bytes (int | Unset):
        in_packets_pass (int | Unset):
        out_packets_pass (int | Unset):
        in_bytes_pass (int | Unset):
        out_bytes_pass (int | Unset):
        in_packets_block (int | Unset):
        out_packets_block (int | Unset):
        in_bytes_block (int | Unset):
        out_bytes_block (int | Unset):
        in_errors (int | Unset):
        out_errors (int | Unset):
        collisions (int | Unset):
        ip_address (str | Unset):
        subnet_mask (str | Unset):
        gateway (str | Unset):
        ipv6_link_local (str | Unset):
        ipv6_address (str | Unset):
        ipv6_subnet_mask (str | Unset):
        ipv6_gateway (str | Unset):
        dns_servers (list[str] | Unset):
        lagg_enabled (bool | Unset):
        lagg_ports (str | Unset):
        current_ppp_uptime (str | Unset):
        historical_ppp_uptime (str | Unset):
        cell_rssi (str | Unset):
        cell_mode (str | Unset):
        cell_simstate (str | Unset):
        cell_service (str | Unset):
        cell_bwupstream (int | Unset):
        cell_bwdownstream (int | Unset):
        cell_upstream (int | Unset):
        cell_downstream (int | Unset):
        dhcplink (str | Unset):
        pppoelink (str | Unset):
        pptplink (str | Unset):
    """

    assigned_interface: str | Unset = UNSET
    internal_name: str | Unset = UNSET
    friendly_name: str | Unset = UNSET
    assigned_name: str | Unset = UNSET
    identity: str | Unset = UNSET
    device: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    status: str | Unset = UNSET
    mac_address: str | Unset = UNSET
    mtu: int | Unset = UNSET
    media: str | Unset = UNSET
    plugged: str | Unset = UNSET
    vendor: str | Unset = UNSET
    temperature: str | Unset = UNSET
    voltage: str | Unset = UNSET
    rx: str | Unset = UNSET
    tx: str | Unset = UNSET
    channel: int | Unset = UNSET
    ssid: str | Unset = UNSET
    bssid: str | Unset = UNSET
    rate: str | Unset = UNSET
    rssi: str | Unset = UNSET
    in_packets: int | Unset = UNSET
    out_packets: int | Unset = UNSET
    in_bytes: int | Unset = UNSET
    out_bytes: int | Unset = UNSET
    in_packets_pass: int | Unset = UNSET
    out_packets_pass: int | Unset = UNSET
    in_bytes_pass: int | Unset = UNSET
    out_bytes_pass: int | Unset = UNSET
    in_packets_block: int | Unset = UNSET
    out_packets_block: int | Unset = UNSET
    in_bytes_block: int | Unset = UNSET
    out_bytes_block: int | Unset = UNSET
    in_errors: int | Unset = UNSET
    out_errors: int | Unset = UNSET
    collisions: int | Unset = UNSET
    ip_address: str | Unset = UNSET
    subnet_mask: str | Unset = UNSET
    gateway: str | Unset = UNSET
    ipv6_link_local: str | Unset = UNSET
    ipv6_address: str | Unset = UNSET
    ipv6_subnet_mask: str | Unset = UNSET
    ipv6_gateway: str | Unset = UNSET
    dns_servers: list[str] | Unset = UNSET
    lagg_enabled: bool | Unset = UNSET
    lagg_ports: str | Unset = UNSET
    current_ppp_uptime: str | Unset = UNSET
    historical_ppp_uptime: str | Unset = UNSET
    cell_rssi: str | Unset = UNSET
    cell_mode: str | Unset = UNSET
    cell_simstate: str | Unset = UNSET
    cell_service: str | Unset = UNSET
    cell_bwupstream: int | Unset = UNSET
    cell_bwdownstream: int | Unset = UNSET
    cell_upstream: int | Unset = UNSET
    cell_downstream: int | Unset = UNSET
    dhcplink: str | Unset = UNSET
    pppoelink: str | Unset = UNSET
    pptplink: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assigned_interface = self.assigned_interface

        internal_name = self.internal_name

        friendly_name = self.friendly_name

        assigned_name = self.assigned_name

        identity = self.identity

        device = self.device

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

        dns_servers: list[str] | Unset = UNSET
        if not isinstance(self.dns_servers, Unset):
            dns_servers = self.dns_servers

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assigned_interface is not UNSET:
            field_dict["assigned_interface"] = assigned_interface
        if internal_name is not UNSET:
            field_dict["internal_name"] = internal_name
        if friendly_name is not UNSET:
            field_dict["friendly_name"] = friendly_name
        if assigned_name is not UNSET:
            field_dict["assigned_name"] = assigned_name
        if identity is not UNSET:
            field_dict["identity"] = identity
        if device is not UNSET:
            field_dict["device"] = device
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if status is not UNSET:
            field_dict["status"] = status
        if mac_address is not UNSET:
            field_dict["mac_address"] = mac_address
        if mtu is not UNSET:
            field_dict["mtu"] = mtu
        if media is not UNSET:
            field_dict["media"] = media
        if plugged is not UNSET:
            field_dict["plugged"] = plugged
        if vendor is not UNSET:
            field_dict["vendor"] = vendor
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if voltage is not UNSET:
            field_dict["voltage"] = voltage
        if rx is not UNSET:
            field_dict["rx"] = rx
        if tx is not UNSET:
            field_dict["tx"] = tx
        if channel is not UNSET:
            field_dict["channel"] = channel
        if ssid is not UNSET:
            field_dict["ssid"] = ssid
        if bssid is not UNSET:
            field_dict["bssid"] = bssid
        if rate is not UNSET:
            field_dict["rate"] = rate
        if rssi is not UNSET:
            field_dict["rssi"] = rssi
        if in_packets is not UNSET:
            field_dict["in_packets"] = in_packets
        if out_packets is not UNSET:
            field_dict["out_packets"] = out_packets
        if in_bytes is not UNSET:
            field_dict["in_bytes"] = in_bytes
        if out_bytes is not UNSET:
            field_dict["out_bytes"] = out_bytes
        if in_packets_pass is not UNSET:
            field_dict["in_packets_pass"] = in_packets_pass
        if out_packets_pass is not UNSET:
            field_dict["out_packets_pass"] = out_packets_pass
        if in_bytes_pass is not UNSET:
            field_dict["in_bytes_pass"] = in_bytes_pass
        if out_bytes_pass is not UNSET:
            field_dict["out_bytes_pass"] = out_bytes_pass
        if in_packets_block is not UNSET:
            field_dict["in_packets_block"] = in_packets_block
        if out_packets_block is not UNSET:
            field_dict["out_packets_block"] = out_packets_block
        if in_bytes_block is not UNSET:
            field_dict["in_bytes_block"] = in_bytes_block
        if out_bytes_block is not UNSET:
            field_dict["out_bytes_block"] = out_bytes_block
        if in_errors is not UNSET:
            field_dict["in_errors"] = in_errors
        if out_errors is not UNSET:
            field_dict["out_errors"] = out_errors
        if collisions is not UNSET:
            field_dict["collisions"] = collisions
        if ip_address is not UNSET:
            field_dict["ip_address"] = ip_address
        if subnet_mask is not UNSET:
            field_dict["subnet_mask"] = subnet_mask
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if ipv6_link_local is not UNSET:
            field_dict["ipv6_link_local"] = ipv6_link_local
        if ipv6_address is not UNSET:
            field_dict["ipv6_address"] = ipv6_address
        if ipv6_subnet_mask is not UNSET:
            field_dict["ipv6_subnet_mask"] = ipv6_subnet_mask
        if ipv6_gateway is not UNSET:
            field_dict["ipv6_gateway"] = ipv6_gateway
        if dns_servers is not UNSET:
            field_dict["dns_servers"] = dns_servers
        if lagg_enabled is not UNSET:
            field_dict["lagg_enabled"] = lagg_enabled
        if lagg_ports is not UNSET:
            field_dict["lagg_ports"] = lagg_ports
        if current_ppp_uptime is not UNSET:
            field_dict["current_ppp_uptime"] = current_ppp_uptime
        if historical_ppp_uptime is not UNSET:
            field_dict["historical_ppp_uptime"] = historical_ppp_uptime
        if cell_rssi is not UNSET:
            field_dict["cell_rssi"] = cell_rssi
        if cell_mode is not UNSET:
            field_dict["cell_mode"] = cell_mode
        if cell_simstate is not UNSET:
            field_dict["cell_simstate"] = cell_simstate
        if cell_service is not UNSET:
            field_dict["cell_service"] = cell_service
        if cell_bwupstream is not UNSET:
            field_dict["cell_bwupstream"] = cell_bwupstream
        if cell_bwdownstream is not UNSET:
            field_dict["cell_bwdownstream"] = cell_bwdownstream
        if cell_upstream is not UNSET:
            field_dict["cell_upstream"] = cell_upstream
        if cell_downstream is not UNSET:
            field_dict["cell_downstream"] = cell_downstream
        if dhcplink is not UNSET:
            field_dict["dhcplink"] = dhcplink
        if pppoelink is not UNSET:
            field_dict["pppoelink"] = pppoelink
        if pptplink is not UNSET:
            field_dict["pptplink"] = pptplink

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        assigned_interface = d.pop("assigned_interface", UNSET)

        internal_name = d.pop("internal_name", UNSET)

        friendly_name = d.pop("friendly_name", UNSET)

        assigned_name = d.pop("assigned_name", UNSET)

        identity = d.pop("identity", UNSET)

        device = d.pop("device", UNSET)

        enabled = d.pop("enabled", UNSET)

        status = d.pop("status", UNSET)

        mac_address = d.pop("mac_address", UNSET)

        mtu = d.pop("mtu", UNSET)

        media = d.pop("media", UNSET)

        plugged = d.pop("plugged", UNSET)

        vendor = d.pop("vendor", UNSET)

        temperature = d.pop("temperature", UNSET)

        voltage = d.pop("voltage", UNSET)

        rx = d.pop("rx", UNSET)

        tx = d.pop("tx", UNSET)

        channel = d.pop("channel", UNSET)

        ssid = d.pop("ssid", UNSET)

        bssid = d.pop("bssid", UNSET)

        rate = d.pop("rate", UNSET)

        rssi = d.pop("rssi", UNSET)

        in_packets = d.pop("in_packets", UNSET)

        out_packets = d.pop("out_packets", UNSET)

        in_bytes = d.pop("in_bytes", UNSET)

        out_bytes = d.pop("out_bytes", UNSET)

        in_packets_pass = d.pop("in_packets_pass", UNSET)

        out_packets_pass = d.pop("out_packets_pass", UNSET)

        in_bytes_pass = d.pop("in_bytes_pass", UNSET)

        out_bytes_pass = d.pop("out_bytes_pass", UNSET)

        in_packets_block = d.pop("in_packets_block", UNSET)

        out_packets_block = d.pop("out_packets_block", UNSET)

        in_bytes_block = d.pop("in_bytes_block", UNSET)

        out_bytes_block = d.pop("out_bytes_block", UNSET)

        in_errors = d.pop("in_errors", UNSET)

        out_errors = d.pop("out_errors", UNSET)

        collisions = d.pop("collisions", UNSET)

        ip_address = d.pop("ip_address", UNSET)

        subnet_mask = d.pop("subnet_mask", UNSET)

        gateway = d.pop("gateway", UNSET)

        ipv6_link_local = d.pop("ipv6_link_local", UNSET)

        ipv6_address = d.pop("ipv6_address", UNSET)

        ipv6_subnet_mask = d.pop("ipv6_subnet_mask", UNSET)

        ipv6_gateway = d.pop("ipv6_gateway", UNSET)

        dns_servers = cast(list[str], d.pop("dns_servers", UNSET))

        lagg_enabled = d.pop("lagg_enabled", UNSET)

        lagg_ports = d.pop("lagg_ports", UNSET)

        current_ppp_uptime = d.pop("current_ppp_uptime", UNSET)

        historical_ppp_uptime = d.pop("historical_ppp_uptime", UNSET)

        cell_rssi = d.pop("cell_rssi", UNSET)

        cell_mode = d.pop("cell_mode", UNSET)

        cell_simstate = d.pop("cell_simstate", UNSET)

        cell_service = d.pop("cell_service", UNSET)

        cell_bwupstream = d.pop("cell_bwupstream", UNSET)

        cell_bwdownstream = d.pop("cell_bwdownstream", UNSET)

        cell_upstream = d.pop("cell_upstream", UNSET)

        cell_downstream = d.pop("cell_downstream", UNSET)

        dhcplink = d.pop("dhcplink", UNSET)

        pppoelink = d.pop("pppoelink", UNSET)

        pptplink = d.pop("pptplink", UNSET)

        interface_info = cls(
            assigned_interface=assigned_interface,
            internal_name=internal_name,
            friendly_name=friendly_name,
            assigned_name=assigned_name,
            identity=identity,
            device=device,
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
            dns_servers=dns_servers,
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
        )

        interface_info.additional_properties = d
        return interface_info

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
