from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.snort_insp_port_scan_icmp_sweep import SnortInspPortScanIcmpSweep
    from ..models.snort_insp_port_scan_ip_decoy import SnortInspPortScanIpDecoy
    from ..models.snort_insp_port_scan_ip_dist import SnortInspPortScanIpDist
    from ..models.snort_insp_port_scan_ip_proto import SnortInspPortScanIpProto
    from ..models.snort_insp_port_scan_ip_sweep import SnortInspPortScanIpSweep
    from ..models.snort_insp_port_scan_tcp_decoy import SnortInspPortScanTcpDecoy
    from ..models.snort_insp_port_scan_tcp_dist import SnortInspPortScanTcpDist
    from ..models.snort_insp_port_scan_tcp_ports import SnortInspPortScanTcpPorts
    from ..models.snort_insp_port_scan_tcp_sweep import SnortInspPortScanTcpSweep
    from ..models.snort_insp_port_scan_udp_decoy import SnortInspPortScanUdpDecoy
    from ..models.snort_insp_port_scan_udp_dist import SnortInspPortScanUdpDist
    from ..models.snort_insp_port_scan_udp_ports import SnortInspPortScanUdpPorts
    from ..models.snort_insp_port_scan_udp_sweep import SnortInspPortScanUdpSweep


T = TypeVar("T", bound="SnortInspPortScan")


@_attrs_define
class SnortInspPortScan:
    """
    Attributes:
        memcap (int | Unset): maximum tracker memory in bytes { 1024:maxSZ }; default 10485760
        protos (list[str] | Unset):
        scan_types (list[str] | Unset):
        watch_ip (str | Unset): list of CIDRs with optional ports to watch
        ignore_scanners (str | Unset): list of CIDRs with optional ports to ignore if the source of scan alerts
        ignore_scanned (str | Unset): list of CIDRs with optional ports to ignore if the destination of scan alerts
        alert_all (bool | Unset): alert on all events over threshold within window if true; else alert on first only;
            default false
        include_midstream (bool | Unset): list of CIDRs with optional ports; default false
        tcp_ports (SnortInspPortScanTcpPorts | Unset):
        tcp_decoy (SnortInspPortScanTcpDecoy | Unset):
        tcp_sweep (SnortInspPortScanTcpSweep | Unset):
        tcp_dist (SnortInspPortScanTcpDist | Unset):
        udp_ports (SnortInspPortScanUdpPorts | Unset):
        udp_decoy (SnortInspPortScanUdpDecoy | Unset):
        udp_sweep (SnortInspPortScanUdpSweep | Unset):
        udp_dist (SnortInspPortScanUdpDist | Unset):
        ip_proto (SnortInspPortScanIpProto | Unset):
        ip_decoy (SnortInspPortScanIpDecoy | Unset):
        ip_sweep (SnortInspPortScanIpSweep | Unset):
        ip_dist (SnortInspPortScanIpDist | Unset):
        icmp_sweep (SnortInspPortScanIcmpSweep | Unset):
        tcp_window (int | Unset): detection interval for all TCP scans { 0:max32 }; default 0
        udp_window (int | Unset): detection interval for all UDP scans { 0:max32 }; default 0
        ip_window (int | Unset): detection interval for all IP scans { 0:max32 }; default 0
        icmp_window (int | Unset): detection interval for all ICMP scans { 0:max32 }; default 0
    """

    memcap: int | Unset = UNSET
    protos: list[str] | Unset = UNSET
    scan_types: list[str] | Unset = UNSET
    watch_ip: str | Unset = UNSET
    ignore_scanners: str | Unset = UNSET
    ignore_scanned: str | Unset = UNSET
    alert_all: bool | Unset = UNSET
    include_midstream: bool | Unset = UNSET
    tcp_ports: SnortInspPortScanTcpPorts | Unset = UNSET
    tcp_decoy: SnortInspPortScanTcpDecoy | Unset = UNSET
    tcp_sweep: SnortInspPortScanTcpSweep | Unset = UNSET
    tcp_dist: SnortInspPortScanTcpDist | Unset = UNSET
    udp_ports: SnortInspPortScanUdpPorts | Unset = UNSET
    udp_decoy: SnortInspPortScanUdpDecoy | Unset = UNSET
    udp_sweep: SnortInspPortScanUdpSweep | Unset = UNSET
    udp_dist: SnortInspPortScanUdpDist | Unset = UNSET
    ip_proto: SnortInspPortScanIpProto | Unset = UNSET
    ip_decoy: SnortInspPortScanIpDecoy | Unset = UNSET
    ip_sweep: SnortInspPortScanIpSweep | Unset = UNSET
    ip_dist: SnortInspPortScanIpDist | Unset = UNSET
    icmp_sweep: SnortInspPortScanIcmpSweep | Unset = UNSET
    tcp_window: int | Unset = UNSET
    udp_window: int | Unset = UNSET
    ip_window: int | Unset = UNSET
    icmp_window: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        memcap = self.memcap

        protos: list[str] | Unset = UNSET
        if not isinstance(self.protos, Unset):
            protos = self.protos

        scan_types: list[str] | Unset = UNSET
        if not isinstance(self.scan_types, Unset):
            scan_types = self.scan_types

        watch_ip = self.watch_ip

        ignore_scanners = self.ignore_scanners

        ignore_scanned = self.ignore_scanned

        alert_all = self.alert_all

        include_midstream = self.include_midstream

        tcp_ports: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tcp_ports, Unset):
            tcp_ports = self.tcp_ports.to_dict()

        tcp_decoy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tcp_decoy, Unset):
            tcp_decoy = self.tcp_decoy.to_dict()

        tcp_sweep: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tcp_sweep, Unset):
            tcp_sweep = self.tcp_sweep.to_dict()

        tcp_dist: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tcp_dist, Unset):
            tcp_dist = self.tcp_dist.to_dict()

        udp_ports: dict[str, Any] | Unset = UNSET
        if not isinstance(self.udp_ports, Unset):
            udp_ports = self.udp_ports.to_dict()

        udp_decoy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.udp_decoy, Unset):
            udp_decoy = self.udp_decoy.to_dict()

        udp_sweep: dict[str, Any] | Unset = UNSET
        if not isinstance(self.udp_sweep, Unset):
            udp_sweep = self.udp_sweep.to_dict()

        udp_dist: dict[str, Any] | Unset = UNSET
        if not isinstance(self.udp_dist, Unset):
            udp_dist = self.udp_dist.to_dict()

        ip_proto: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ip_proto, Unset):
            ip_proto = self.ip_proto.to_dict()

        ip_decoy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ip_decoy, Unset):
            ip_decoy = self.ip_decoy.to_dict()

        ip_sweep: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ip_sweep, Unset):
            ip_sweep = self.ip_sweep.to_dict()

        ip_dist: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ip_dist, Unset):
            ip_dist = self.ip_dist.to_dict()

        icmp_sweep: dict[str, Any] | Unset = UNSET
        if not isinstance(self.icmp_sweep, Unset):
            icmp_sweep = self.icmp_sweep.to_dict()

        tcp_window = self.tcp_window

        udp_window = self.udp_window

        ip_window = self.ip_window

        icmp_window = self.icmp_window

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if memcap is not UNSET:
            field_dict["memcap"] = memcap
        if protos is not UNSET:
            field_dict["protos"] = protos
        if scan_types is not UNSET:
            field_dict["scan_types"] = scan_types
        if watch_ip is not UNSET:
            field_dict["watch_ip"] = watch_ip
        if ignore_scanners is not UNSET:
            field_dict["ignore_scanners"] = ignore_scanners
        if ignore_scanned is not UNSET:
            field_dict["ignore_scanned"] = ignore_scanned
        if alert_all is not UNSET:
            field_dict["alert_all"] = alert_all
        if include_midstream is not UNSET:
            field_dict["include_midstream"] = include_midstream
        if tcp_ports is not UNSET:
            field_dict["tcp_ports"] = tcp_ports
        if tcp_decoy is not UNSET:
            field_dict["tcp_decoy"] = tcp_decoy
        if tcp_sweep is not UNSET:
            field_dict["tcp_sweep"] = tcp_sweep
        if tcp_dist is not UNSET:
            field_dict["tcp_dist"] = tcp_dist
        if udp_ports is not UNSET:
            field_dict["udp_ports"] = udp_ports
        if udp_decoy is not UNSET:
            field_dict["udp_decoy"] = udp_decoy
        if udp_sweep is not UNSET:
            field_dict["udp_sweep"] = udp_sweep
        if udp_dist is not UNSET:
            field_dict["udp_dist"] = udp_dist
        if ip_proto is not UNSET:
            field_dict["ip_proto"] = ip_proto
        if ip_decoy is not UNSET:
            field_dict["ip_decoy"] = ip_decoy
        if ip_sweep is not UNSET:
            field_dict["ip_sweep"] = ip_sweep
        if ip_dist is not UNSET:
            field_dict["ip_dist"] = ip_dist
        if icmp_sweep is not UNSET:
            field_dict["icmp_sweep"] = icmp_sweep
        if tcp_window is not UNSET:
            field_dict["tcp_window"] = tcp_window
        if udp_window is not UNSET:
            field_dict["udp_window"] = udp_window
        if ip_window is not UNSET:
            field_dict["ip_window"] = ip_window
        if icmp_window is not UNSET:
            field_dict["icmp_window"] = icmp_window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.snort_insp_port_scan_icmp_sweep import SnortInspPortScanIcmpSweep
        from ..models.snort_insp_port_scan_ip_decoy import SnortInspPortScanIpDecoy
        from ..models.snort_insp_port_scan_ip_dist import SnortInspPortScanIpDist
        from ..models.snort_insp_port_scan_ip_proto import SnortInspPortScanIpProto
        from ..models.snort_insp_port_scan_ip_sweep import SnortInspPortScanIpSweep
        from ..models.snort_insp_port_scan_tcp_decoy import SnortInspPortScanTcpDecoy
        from ..models.snort_insp_port_scan_tcp_dist import SnortInspPortScanTcpDist
        from ..models.snort_insp_port_scan_tcp_ports import SnortInspPortScanTcpPorts
        from ..models.snort_insp_port_scan_tcp_sweep import SnortInspPortScanTcpSweep
        from ..models.snort_insp_port_scan_udp_decoy import SnortInspPortScanUdpDecoy
        from ..models.snort_insp_port_scan_udp_dist import SnortInspPortScanUdpDist
        from ..models.snort_insp_port_scan_udp_ports import SnortInspPortScanUdpPorts
        from ..models.snort_insp_port_scan_udp_sweep import SnortInspPortScanUdpSweep

        d = dict(src_dict)
        memcap = d.pop("memcap", UNSET)

        protos = cast(list[str], d.pop("protos", UNSET))

        scan_types = cast(list[str], d.pop("scan_types", UNSET))

        watch_ip = d.pop("watch_ip", UNSET)

        ignore_scanners = d.pop("ignore_scanners", UNSET)

        ignore_scanned = d.pop("ignore_scanned", UNSET)

        alert_all = d.pop("alert_all", UNSET)

        include_midstream = d.pop("include_midstream", UNSET)

        _tcp_ports = d.pop("tcp_ports", UNSET)
        tcp_ports: SnortInspPortScanTcpPorts | Unset
        if isinstance(_tcp_ports, Unset):
            tcp_ports = UNSET
        else:
            tcp_ports = SnortInspPortScanTcpPorts.from_dict(_tcp_ports)

        _tcp_decoy = d.pop("tcp_decoy", UNSET)
        tcp_decoy: SnortInspPortScanTcpDecoy | Unset
        if isinstance(_tcp_decoy, Unset):
            tcp_decoy = UNSET
        else:
            tcp_decoy = SnortInspPortScanTcpDecoy.from_dict(_tcp_decoy)

        _tcp_sweep = d.pop("tcp_sweep", UNSET)
        tcp_sweep: SnortInspPortScanTcpSweep | Unset
        if isinstance(_tcp_sweep, Unset):
            tcp_sweep = UNSET
        else:
            tcp_sweep = SnortInspPortScanTcpSweep.from_dict(_tcp_sweep)

        _tcp_dist = d.pop("tcp_dist", UNSET)
        tcp_dist: SnortInspPortScanTcpDist | Unset
        if isinstance(_tcp_dist, Unset):
            tcp_dist = UNSET
        else:
            tcp_dist = SnortInspPortScanTcpDist.from_dict(_tcp_dist)

        _udp_ports = d.pop("udp_ports", UNSET)
        udp_ports: SnortInspPortScanUdpPorts | Unset
        if isinstance(_udp_ports, Unset):
            udp_ports = UNSET
        else:
            udp_ports = SnortInspPortScanUdpPorts.from_dict(_udp_ports)

        _udp_decoy = d.pop("udp_decoy", UNSET)
        udp_decoy: SnortInspPortScanUdpDecoy | Unset
        if isinstance(_udp_decoy, Unset):
            udp_decoy = UNSET
        else:
            udp_decoy = SnortInspPortScanUdpDecoy.from_dict(_udp_decoy)

        _udp_sweep = d.pop("udp_sweep", UNSET)
        udp_sweep: SnortInspPortScanUdpSweep | Unset
        if isinstance(_udp_sweep, Unset):
            udp_sweep = UNSET
        else:
            udp_sweep = SnortInspPortScanUdpSweep.from_dict(_udp_sweep)

        _udp_dist = d.pop("udp_dist", UNSET)
        udp_dist: SnortInspPortScanUdpDist | Unset
        if isinstance(_udp_dist, Unset):
            udp_dist = UNSET
        else:
            udp_dist = SnortInspPortScanUdpDist.from_dict(_udp_dist)

        _ip_proto = d.pop("ip_proto", UNSET)
        ip_proto: SnortInspPortScanIpProto | Unset
        if isinstance(_ip_proto, Unset):
            ip_proto = UNSET
        else:
            ip_proto = SnortInspPortScanIpProto.from_dict(_ip_proto)

        _ip_decoy = d.pop("ip_decoy", UNSET)
        ip_decoy: SnortInspPortScanIpDecoy | Unset
        if isinstance(_ip_decoy, Unset):
            ip_decoy = UNSET
        else:
            ip_decoy = SnortInspPortScanIpDecoy.from_dict(_ip_decoy)

        _ip_sweep = d.pop("ip_sweep", UNSET)
        ip_sweep: SnortInspPortScanIpSweep | Unset
        if isinstance(_ip_sweep, Unset):
            ip_sweep = UNSET
        else:
            ip_sweep = SnortInspPortScanIpSweep.from_dict(_ip_sweep)

        _ip_dist = d.pop("ip_dist", UNSET)
        ip_dist: SnortInspPortScanIpDist | Unset
        if isinstance(_ip_dist, Unset):
            ip_dist = UNSET
        else:
            ip_dist = SnortInspPortScanIpDist.from_dict(_ip_dist)

        _icmp_sweep = d.pop("icmp_sweep", UNSET)
        icmp_sweep: SnortInspPortScanIcmpSweep | Unset
        if isinstance(_icmp_sweep, Unset):
            icmp_sweep = UNSET
        else:
            icmp_sweep = SnortInspPortScanIcmpSweep.from_dict(_icmp_sweep)

        tcp_window = d.pop("tcp_window", UNSET)

        udp_window = d.pop("udp_window", UNSET)

        ip_window = d.pop("ip_window", UNSET)

        icmp_window = d.pop("icmp_window", UNSET)

        snort_insp_port_scan = cls(
            memcap=memcap,
            protos=protos,
            scan_types=scan_types,
            watch_ip=watch_ip,
            ignore_scanners=ignore_scanners,
            ignore_scanned=ignore_scanned,
            alert_all=alert_all,
            include_midstream=include_midstream,
            tcp_ports=tcp_ports,
            tcp_decoy=tcp_decoy,
            tcp_sweep=tcp_sweep,
            tcp_dist=tcp_dist,
            udp_ports=udp_ports,
            udp_decoy=udp_decoy,
            udp_sweep=udp_sweep,
            udp_dist=udp_dist,
            ip_proto=ip_proto,
            ip_decoy=ip_decoy,
            ip_sweep=ip_sweep,
            ip_dist=ip_dist,
            icmp_sweep=icmp_sweep,
            tcp_window=tcp_window,
            udp_window=udp_window,
            ip_window=ip_window,
            icmp_window=icmp_window,
        )

        snort_insp_port_scan.additional_properties = d
        return snort_insp_port_scan

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
