from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.snort_insp_appid import SnortInspAppid
    from ..models.snort_insp_appid_listener import SnortInspAppidListener
    from ..models.snort_insp_arp_spoof import SnortInspArpSpoof
    from ..models.snort_insp_cip import SnortInspCip
    from ..models.snort_insp_data_log import SnortInspDataLog
    from ..models.snort_insp_dce_smb import SnortInspDceSmb
    from ..models.snort_insp_dce_tcp import SnortInspDceTcp
    from ..models.snort_insp_dce_udp import SnortInspDceUdp
    from ..models.snort_insp_dnp_3 import SnortInspDnp3
    from ..models.snort_insp_dns import SnortInspDns
    from ..models.snort_insp_domain_filter import SnortInspDomainFilter
    from ..models.snort_insp_dpx import SnortInspDpx
    from ..models.snort_insp_extractor import SnortInspExtractor
    from ..models.snort_insp_file_id import SnortInspFileId
    from ..models.snort_insp_file_log import SnortInspFileLog
    from ..models.snort_insp_ftp_client import SnortInspFtpClient
    from ..models.snort_insp_ftp_server import SnortInspFtpServer
    from ..models.snort_insp_gtp_inspect import SnortInspGtpInspect
    from ..models.snort_insp_http_2_inspect import SnortInspHttp2Inspect
    from ..models.snort_insp_http_inspect import SnortInspHttpInspect
    from ..models.snort_insp_imap import SnortInspImap
    from ..models.snort_insp_netflow import SnortInspNetflow
    from ..models.snort_insp_normalizer import SnortInspNormalizer
    from ..models.snort_insp_packet_capture import SnortInspPacketCapture
    from ..models.snort_insp_perf_monitor import SnortInspPerfMonitor
    from ..models.snort_insp_pop import SnortInspPop
    from ..models.snort_insp_port_scan import SnortInspPortScan
    from ..models.snort_insp_rna import SnortInspRna
    from ..models.snort_insp_sip import SnortInspSip
    from ..models.snort_insp_smtp import SnortInspSmtp
    from ..models.snort_insp_snort_ml import SnortInspSnortMl
    from ..models.snort_insp_snort_ml_engine import SnortInspSnortMlEngine
    from ..models.snort_insp_ssh import SnortInspSsh
    from ..models.snort_insp_ssl import SnortInspSsl
    from ..models.snort_insp_stream import SnortInspStream
    from ..models.snort_insp_stream_file import SnortInspStreamFile
    from ..models.snort_insp_stream_icmp import SnortInspStreamIcmp
    from ..models.snort_insp_stream_ip import SnortInspStreamIp
    from ..models.snort_insp_stream_tcp import SnortInspStreamTcp
    from ..models.snort_insp_stream_udp import SnortInspStreamUdp
    from ..models.snort_insp_stream_user import SnortInspStreamUser
    from ..models.snort_insp_telnet import SnortInspTelnet
    from ..models.snort_insp_tlv_pdu import SnortInspTlvPdu
    from ..models.snort_insp_wizard import SnortInspWizard


T = TypeVar("T", bound="SnortInspectors")


@_attrs_define
class SnortInspectors:
    """Snort inspectors, also known is preprocessors, are modules
    that perform a variety of functions. The configuration of each
    inspector is complex and should only have defaults overridden
    with care.

        Attributes:
            enabled (list[str] | Unset):
            appid (SnortInspAppid | Unset):
            appid_listener (SnortInspAppidListener | Unset):
            arp_spoof (SnortInspArpSpoof | Unset):
            cip (SnortInspCip | Unset):
            data_log (SnortInspDataLog | Unset):
            dce_smb (SnortInspDceSmb | Unset):
            dce_tcp (SnortInspDceTcp | Unset):
            dce_udp (SnortInspDceUdp | Unset):
            dnp3 (SnortInspDnp3 | Unset):
            dns (SnortInspDns | Unset):
            domain_filter (SnortInspDomainFilter | Unset):
            dpx (SnortInspDpx | Unset):
            extractor (SnortInspExtractor | Unset):
            file_id (SnortInspFileId | Unset):
            file_log (SnortInspFileLog | Unset):
            ftp_client (SnortInspFtpClient | Unset):
            ftp_server (SnortInspFtpServer | Unset):
            gtp_inspect (SnortInspGtpInspect | Unset):
            http2_inspect (SnortInspHttp2Inspect | Unset):
            http_inspect (SnortInspHttpInspect | Unset):
            imap (SnortInspImap | Unset):
            netflow (SnortInspNetflow | Unset):
            normalizer (SnortInspNormalizer | Unset):
            packet_capture (SnortInspPacketCapture | Unset):
            perf_monitor (SnortInspPerfMonitor | Unset):
            pop (SnortInspPop | Unset):
            port_scan (SnortInspPortScan | Unset):
            rna (SnortInspRna | Unset):
            sip (SnortInspSip | Unset):
            smtp (SnortInspSmtp | Unset):
            snort_ml (SnortInspSnortMl | Unset):
            snort_ml_engine (SnortInspSnortMlEngine | Unset):
            ssh (SnortInspSsh | Unset):
            ssl (SnortInspSsl | Unset):
            stream (SnortInspStream | Unset):
            stream_file (SnortInspStreamFile | Unset):
            stream_icmp (SnortInspStreamIcmp | Unset):
            stream_ip (SnortInspStreamIp | Unset):
            stream_tcp (SnortInspStreamTcp | Unset):
            stream_udp (SnortInspStreamUdp | Unset):
            stream_user (SnortInspStreamUser | Unset):
            telnet (SnortInspTelnet | Unset):
            tlv_pdu (SnortInspTlvPdu | Unset):
            wizard (SnortInspWizard | Unset):
    """

    enabled: list[str] | Unset = UNSET
    appid: SnortInspAppid | Unset = UNSET
    appid_listener: SnortInspAppidListener | Unset = UNSET
    arp_spoof: SnortInspArpSpoof | Unset = UNSET
    cip: SnortInspCip | Unset = UNSET
    data_log: SnortInspDataLog | Unset = UNSET
    dce_smb: SnortInspDceSmb | Unset = UNSET
    dce_tcp: SnortInspDceTcp | Unset = UNSET
    dce_udp: SnortInspDceUdp | Unset = UNSET
    dnp3: SnortInspDnp3 | Unset = UNSET
    dns: SnortInspDns | Unset = UNSET
    domain_filter: SnortInspDomainFilter | Unset = UNSET
    dpx: SnortInspDpx | Unset = UNSET
    extractor: SnortInspExtractor | Unset = UNSET
    file_id: SnortInspFileId | Unset = UNSET
    file_log: SnortInspFileLog | Unset = UNSET
    ftp_client: SnortInspFtpClient | Unset = UNSET
    ftp_server: SnortInspFtpServer | Unset = UNSET
    gtp_inspect: SnortInspGtpInspect | Unset = UNSET
    http2_inspect: SnortInspHttp2Inspect | Unset = UNSET
    http_inspect: SnortInspHttpInspect | Unset = UNSET
    imap: SnortInspImap | Unset = UNSET
    netflow: SnortInspNetflow | Unset = UNSET
    normalizer: SnortInspNormalizer | Unset = UNSET
    packet_capture: SnortInspPacketCapture | Unset = UNSET
    perf_monitor: SnortInspPerfMonitor | Unset = UNSET
    pop: SnortInspPop | Unset = UNSET
    port_scan: SnortInspPortScan | Unset = UNSET
    rna: SnortInspRna | Unset = UNSET
    sip: SnortInspSip | Unset = UNSET
    smtp: SnortInspSmtp | Unset = UNSET
    snort_ml: SnortInspSnortMl | Unset = UNSET
    snort_ml_engine: SnortInspSnortMlEngine | Unset = UNSET
    ssh: SnortInspSsh | Unset = UNSET
    ssl: SnortInspSsl | Unset = UNSET
    stream: SnortInspStream | Unset = UNSET
    stream_file: SnortInspStreamFile | Unset = UNSET
    stream_icmp: SnortInspStreamIcmp | Unset = UNSET
    stream_ip: SnortInspStreamIp | Unset = UNSET
    stream_tcp: SnortInspStreamTcp | Unset = UNSET
    stream_udp: SnortInspStreamUdp | Unset = UNSET
    stream_user: SnortInspStreamUser | Unset = UNSET
    telnet: SnortInspTelnet | Unset = UNSET
    tlv_pdu: SnortInspTlvPdu | Unset = UNSET
    wizard: SnortInspWizard | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled: list[str] | Unset = UNSET
        if not isinstance(self.enabled, Unset):
            enabled = self.enabled

        appid: dict[str, Any] | Unset = UNSET
        if not isinstance(self.appid, Unset):
            appid = self.appid.to_dict()

        appid_listener: dict[str, Any] | Unset = UNSET
        if not isinstance(self.appid_listener, Unset):
            appid_listener = self.appid_listener.to_dict()

        arp_spoof: dict[str, Any] | Unset = UNSET
        if not isinstance(self.arp_spoof, Unset):
            arp_spoof = self.arp_spoof.to_dict()

        cip: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cip, Unset):
            cip = self.cip.to_dict()

        data_log: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_log, Unset):
            data_log = self.data_log.to_dict()

        dce_smb: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dce_smb, Unset):
            dce_smb = self.dce_smb.to_dict()

        dce_tcp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dce_tcp, Unset):
            dce_tcp = self.dce_tcp.to_dict()

        dce_udp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dce_udp, Unset):
            dce_udp = self.dce_udp.to_dict()

        dnp3: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dnp3, Unset):
            dnp3 = self.dnp3.to_dict()

        dns: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dns, Unset):
            dns = self.dns.to_dict()

        domain_filter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.domain_filter, Unset):
            domain_filter = self.domain_filter.to_dict()

        dpx: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dpx, Unset):
            dpx = self.dpx.to_dict()

        extractor: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extractor, Unset):
            extractor = self.extractor.to_dict()

        file_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.file_id, Unset):
            file_id = self.file_id.to_dict()

        file_log: dict[str, Any] | Unset = UNSET
        if not isinstance(self.file_log, Unset):
            file_log = self.file_log.to_dict()

        ftp_client: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ftp_client, Unset):
            ftp_client = self.ftp_client.to_dict()

        ftp_server: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ftp_server, Unset):
            ftp_server = self.ftp_server.to_dict()

        gtp_inspect: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gtp_inspect, Unset):
            gtp_inspect = self.gtp_inspect.to_dict()

        http2_inspect: dict[str, Any] | Unset = UNSET
        if not isinstance(self.http2_inspect, Unset):
            http2_inspect = self.http2_inspect.to_dict()

        http_inspect: dict[str, Any] | Unset = UNSET
        if not isinstance(self.http_inspect, Unset):
            http_inspect = self.http_inspect.to_dict()

        imap: dict[str, Any] | Unset = UNSET
        if not isinstance(self.imap, Unset):
            imap = self.imap.to_dict()

        netflow: dict[str, Any] | Unset = UNSET
        if not isinstance(self.netflow, Unset):
            netflow = self.netflow.to_dict()

        normalizer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.normalizer, Unset):
            normalizer = self.normalizer.to_dict()

        packet_capture: dict[str, Any] | Unset = UNSET
        if not isinstance(self.packet_capture, Unset):
            packet_capture = self.packet_capture.to_dict()

        perf_monitor: dict[str, Any] | Unset = UNSET
        if not isinstance(self.perf_monitor, Unset):
            perf_monitor = self.perf_monitor.to_dict()

        pop: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pop, Unset):
            pop = self.pop.to_dict()

        port_scan: dict[str, Any] | Unset = UNSET
        if not isinstance(self.port_scan, Unset):
            port_scan = self.port_scan.to_dict()

        rna: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rna, Unset):
            rna = self.rna.to_dict()

        sip: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sip, Unset):
            sip = self.sip.to_dict()

        smtp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.smtp, Unset):
            smtp = self.smtp.to_dict()

        snort_ml: dict[str, Any] | Unset = UNSET
        if not isinstance(self.snort_ml, Unset):
            snort_ml = self.snort_ml.to_dict()

        snort_ml_engine: dict[str, Any] | Unset = UNSET
        if not isinstance(self.snort_ml_engine, Unset):
            snort_ml_engine = self.snort_ml_engine.to_dict()

        ssh: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ssh, Unset):
            ssh = self.ssh.to_dict()

        ssl: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ssl, Unset):
            ssl = self.ssl.to_dict()

        stream: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stream, Unset):
            stream = self.stream.to_dict()

        stream_file: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stream_file, Unset):
            stream_file = self.stream_file.to_dict()

        stream_icmp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stream_icmp, Unset):
            stream_icmp = self.stream_icmp.to_dict()

        stream_ip: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stream_ip, Unset):
            stream_ip = self.stream_ip.to_dict()

        stream_tcp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stream_tcp, Unset):
            stream_tcp = self.stream_tcp.to_dict()

        stream_udp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stream_udp, Unset):
            stream_udp = self.stream_udp.to_dict()

        stream_user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stream_user, Unset):
            stream_user = self.stream_user.to_dict()

        telnet: dict[str, Any] | Unset = UNSET
        if not isinstance(self.telnet, Unset):
            telnet = self.telnet.to_dict()

        tlv_pdu: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tlv_pdu, Unset):
            tlv_pdu = self.tlv_pdu.to_dict()

        wizard: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wizard, Unset):
            wizard = self.wizard.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if appid is not UNSET:
            field_dict["appid"] = appid
        if appid_listener is not UNSET:
            field_dict["appid_listener"] = appid_listener
        if arp_spoof is not UNSET:
            field_dict["arp_spoof"] = arp_spoof
        if cip is not UNSET:
            field_dict["cip"] = cip
        if data_log is not UNSET:
            field_dict["data_log"] = data_log
        if dce_smb is not UNSET:
            field_dict["dce_smb"] = dce_smb
        if dce_tcp is not UNSET:
            field_dict["dce_tcp"] = dce_tcp
        if dce_udp is not UNSET:
            field_dict["dce_udp"] = dce_udp
        if dnp3 is not UNSET:
            field_dict["dnp3"] = dnp3
        if dns is not UNSET:
            field_dict["dns"] = dns
        if domain_filter is not UNSET:
            field_dict["domain_filter"] = domain_filter
        if dpx is not UNSET:
            field_dict["dpx"] = dpx
        if extractor is not UNSET:
            field_dict["extractor"] = extractor
        if file_id is not UNSET:
            field_dict["file_id"] = file_id
        if file_log is not UNSET:
            field_dict["file_log"] = file_log
        if ftp_client is not UNSET:
            field_dict["ftp_client"] = ftp_client
        if ftp_server is not UNSET:
            field_dict["ftp_server"] = ftp_server
        if gtp_inspect is not UNSET:
            field_dict["gtp_inspect"] = gtp_inspect
        if http2_inspect is not UNSET:
            field_dict["http2_inspect"] = http2_inspect
        if http_inspect is not UNSET:
            field_dict["http_inspect"] = http_inspect
        if imap is not UNSET:
            field_dict["imap"] = imap
        if netflow is not UNSET:
            field_dict["netflow"] = netflow
        if normalizer is not UNSET:
            field_dict["normalizer"] = normalizer
        if packet_capture is not UNSET:
            field_dict["packet_capture"] = packet_capture
        if perf_monitor is not UNSET:
            field_dict["perf_monitor"] = perf_monitor
        if pop is not UNSET:
            field_dict["pop"] = pop
        if port_scan is not UNSET:
            field_dict["port_scan"] = port_scan
        if rna is not UNSET:
            field_dict["rna"] = rna
        if sip is not UNSET:
            field_dict["sip"] = sip
        if smtp is not UNSET:
            field_dict["smtp"] = smtp
        if snort_ml is not UNSET:
            field_dict["snort_ml"] = snort_ml
        if snort_ml_engine is not UNSET:
            field_dict["snort_ml_engine"] = snort_ml_engine
        if ssh is not UNSET:
            field_dict["ssh"] = ssh
        if ssl is not UNSET:
            field_dict["ssl"] = ssl
        if stream is not UNSET:
            field_dict["stream"] = stream
        if stream_file is not UNSET:
            field_dict["stream_file"] = stream_file
        if stream_icmp is not UNSET:
            field_dict["stream_icmp"] = stream_icmp
        if stream_ip is not UNSET:
            field_dict["stream_ip"] = stream_ip
        if stream_tcp is not UNSET:
            field_dict["stream_tcp"] = stream_tcp
        if stream_udp is not UNSET:
            field_dict["stream_udp"] = stream_udp
        if stream_user is not UNSET:
            field_dict["stream_user"] = stream_user
        if telnet is not UNSET:
            field_dict["telnet"] = telnet
        if tlv_pdu is not UNSET:
            field_dict["tlv_pdu"] = tlv_pdu
        if wizard is not UNSET:
            field_dict["wizard"] = wizard

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.snort_insp_appid import SnortInspAppid
        from ..models.snort_insp_appid_listener import SnortInspAppidListener
        from ..models.snort_insp_arp_spoof import SnortInspArpSpoof
        from ..models.snort_insp_cip import SnortInspCip
        from ..models.snort_insp_data_log import SnortInspDataLog
        from ..models.snort_insp_dce_smb import SnortInspDceSmb
        from ..models.snort_insp_dce_tcp import SnortInspDceTcp
        from ..models.snort_insp_dce_udp import SnortInspDceUdp
        from ..models.snort_insp_dnp_3 import SnortInspDnp3
        from ..models.snort_insp_dns import SnortInspDns
        from ..models.snort_insp_domain_filter import SnortInspDomainFilter
        from ..models.snort_insp_dpx import SnortInspDpx
        from ..models.snort_insp_extractor import SnortInspExtractor
        from ..models.snort_insp_file_id import SnortInspFileId
        from ..models.snort_insp_file_log import SnortInspFileLog
        from ..models.snort_insp_ftp_client import SnortInspFtpClient
        from ..models.snort_insp_ftp_server import SnortInspFtpServer
        from ..models.snort_insp_gtp_inspect import SnortInspGtpInspect
        from ..models.snort_insp_http_2_inspect import SnortInspHttp2Inspect
        from ..models.snort_insp_http_inspect import SnortInspHttpInspect
        from ..models.snort_insp_imap import SnortInspImap
        from ..models.snort_insp_netflow import SnortInspNetflow
        from ..models.snort_insp_normalizer import SnortInspNormalizer
        from ..models.snort_insp_packet_capture import SnortInspPacketCapture
        from ..models.snort_insp_perf_monitor import SnortInspPerfMonitor
        from ..models.snort_insp_pop import SnortInspPop
        from ..models.snort_insp_port_scan import SnortInspPortScan
        from ..models.snort_insp_rna import SnortInspRna
        from ..models.snort_insp_sip import SnortInspSip
        from ..models.snort_insp_smtp import SnortInspSmtp
        from ..models.snort_insp_snort_ml import SnortInspSnortMl
        from ..models.snort_insp_snort_ml_engine import SnortInspSnortMlEngine
        from ..models.snort_insp_ssh import SnortInspSsh
        from ..models.snort_insp_ssl import SnortInspSsl
        from ..models.snort_insp_stream import SnortInspStream
        from ..models.snort_insp_stream_file import SnortInspStreamFile
        from ..models.snort_insp_stream_icmp import SnortInspStreamIcmp
        from ..models.snort_insp_stream_ip import SnortInspStreamIp
        from ..models.snort_insp_stream_tcp import SnortInspStreamTcp
        from ..models.snort_insp_stream_udp import SnortInspStreamUdp
        from ..models.snort_insp_stream_user import SnortInspStreamUser
        from ..models.snort_insp_telnet import SnortInspTelnet
        from ..models.snort_insp_tlv_pdu import SnortInspTlvPdu
        from ..models.snort_insp_wizard import SnortInspWizard

        d = dict(src_dict)
        enabled = cast(list[str], d.pop("enabled", UNSET))

        _appid = d.pop("appid", UNSET)
        appid: SnortInspAppid | Unset
        if isinstance(_appid, Unset):
            appid = UNSET
        else:
            appid = SnortInspAppid.from_dict(_appid)

        _appid_listener = d.pop("appid_listener", UNSET)
        appid_listener: SnortInspAppidListener | Unset
        if isinstance(_appid_listener, Unset):
            appid_listener = UNSET
        else:
            appid_listener = SnortInspAppidListener.from_dict(_appid_listener)

        _arp_spoof = d.pop("arp_spoof", UNSET)
        arp_spoof: SnortInspArpSpoof | Unset
        if isinstance(_arp_spoof, Unset):
            arp_spoof = UNSET
        else:
            arp_spoof = SnortInspArpSpoof.from_dict(_arp_spoof)

        _cip = d.pop("cip", UNSET)
        cip: SnortInspCip | Unset
        if isinstance(_cip, Unset):
            cip = UNSET
        else:
            cip = SnortInspCip.from_dict(_cip)

        _data_log = d.pop("data_log", UNSET)
        data_log: SnortInspDataLog | Unset
        if isinstance(_data_log, Unset):
            data_log = UNSET
        else:
            data_log = SnortInspDataLog.from_dict(_data_log)

        _dce_smb = d.pop("dce_smb", UNSET)
        dce_smb: SnortInspDceSmb | Unset
        if isinstance(_dce_smb, Unset):
            dce_smb = UNSET
        else:
            dce_smb = SnortInspDceSmb.from_dict(_dce_smb)

        _dce_tcp = d.pop("dce_tcp", UNSET)
        dce_tcp: SnortInspDceTcp | Unset
        if isinstance(_dce_tcp, Unset):
            dce_tcp = UNSET
        else:
            dce_tcp = SnortInspDceTcp.from_dict(_dce_tcp)

        _dce_udp = d.pop("dce_udp", UNSET)
        dce_udp: SnortInspDceUdp | Unset
        if isinstance(_dce_udp, Unset):
            dce_udp = UNSET
        else:
            dce_udp = SnortInspDceUdp.from_dict(_dce_udp)

        _dnp3 = d.pop("dnp3", UNSET)
        dnp3: SnortInspDnp3 | Unset
        if isinstance(_dnp3, Unset):
            dnp3 = UNSET
        else:
            dnp3 = SnortInspDnp3.from_dict(_dnp3)

        _dns = d.pop("dns", UNSET)
        dns: SnortInspDns | Unset
        if isinstance(_dns, Unset):
            dns = UNSET
        else:
            dns = SnortInspDns.from_dict(_dns)

        _domain_filter = d.pop("domain_filter", UNSET)
        domain_filter: SnortInspDomainFilter | Unset
        if isinstance(_domain_filter, Unset):
            domain_filter = UNSET
        else:
            domain_filter = SnortInspDomainFilter.from_dict(_domain_filter)

        _dpx = d.pop("dpx", UNSET)
        dpx: SnortInspDpx | Unset
        if isinstance(_dpx, Unset):
            dpx = UNSET
        else:
            dpx = SnortInspDpx.from_dict(_dpx)

        _extractor = d.pop("extractor", UNSET)
        extractor: SnortInspExtractor | Unset
        if isinstance(_extractor, Unset):
            extractor = UNSET
        else:
            extractor = SnortInspExtractor.from_dict(_extractor)

        _file_id = d.pop("file_id", UNSET)
        file_id: SnortInspFileId | Unset
        if isinstance(_file_id, Unset):
            file_id = UNSET
        else:
            file_id = SnortInspFileId.from_dict(_file_id)

        _file_log = d.pop("file_log", UNSET)
        file_log: SnortInspFileLog | Unset
        if isinstance(_file_log, Unset):
            file_log = UNSET
        else:
            file_log = SnortInspFileLog.from_dict(_file_log)

        _ftp_client = d.pop("ftp_client", UNSET)
        ftp_client: SnortInspFtpClient | Unset
        if isinstance(_ftp_client, Unset):
            ftp_client = UNSET
        else:
            ftp_client = SnortInspFtpClient.from_dict(_ftp_client)

        _ftp_server = d.pop("ftp_server", UNSET)
        ftp_server: SnortInspFtpServer | Unset
        if isinstance(_ftp_server, Unset):
            ftp_server = UNSET
        else:
            ftp_server = SnortInspFtpServer.from_dict(_ftp_server)

        _gtp_inspect = d.pop("gtp_inspect", UNSET)
        gtp_inspect: SnortInspGtpInspect | Unset
        if isinstance(_gtp_inspect, Unset):
            gtp_inspect = UNSET
        else:
            gtp_inspect = SnortInspGtpInspect.from_dict(_gtp_inspect)

        _http2_inspect = d.pop("http2_inspect", UNSET)
        http2_inspect: SnortInspHttp2Inspect | Unset
        if isinstance(_http2_inspect, Unset):
            http2_inspect = UNSET
        else:
            http2_inspect = SnortInspHttp2Inspect.from_dict(_http2_inspect)

        _http_inspect = d.pop("http_inspect", UNSET)
        http_inspect: SnortInspHttpInspect | Unset
        if isinstance(_http_inspect, Unset):
            http_inspect = UNSET
        else:
            http_inspect = SnortInspHttpInspect.from_dict(_http_inspect)

        _imap = d.pop("imap", UNSET)
        imap: SnortInspImap | Unset
        if isinstance(_imap, Unset):
            imap = UNSET
        else:
            imap = SnortInspImap.from_dict(_imap)

        _netflow = d.pop("netflow", UNSET)
        netflow: SnortInspNetflow | Unset
        if isinstance(_netflow, Unset):
            netflow = UNSET
        else:
            netflow = SnortInspNetflow.from_dict(_netflow)

        _normalizer = d.pop("normalizer", UNSET)
        normalizer: SnortInspNormalizer | Unset
        if isinstance(_normalizer, Unset):
            normalizer = UNSET
        else:
            normalizer = SnortInspNormalizer.from_dict(_normalizer)

        _packet_capture = d.pop("packet_capture", UNSET)
        packet_capture: SnortInspPacketCapture | Unset
        if isinstance(_packet_capture, Unset):
            packet_capture = UNSET
        else:
            packet_capture = SnortInspPacketCapture.from_dict(_packet_capture)

        _perf_monitor = d.pop("perf_monitor", UNSET)
        perf_monitor: SnortInspPerfMonitor | Unset
        if isinstance(_perf_monitor, Unset):
            perf_monitor = UNSET
        else:
            perf_monitor = SnortInspPerfMonitor.from_dict(_perf_monitor)

        _pop = d.pop("pop", UNSET)
        pop: SnortInspPop | Unset
        if isinstance(_pop, Unset):
            pop = UNSET
        else:
            pop = SnortInspPop.from_dict(_pop)

        _port_scan = d.pop("port_scan", UNSET)
        port_scan: SnortInspPortScan | Unset
        if isinstance(_port_scan, Unset):
            port_scan = UNSET
        else:
            port_scan = SnortInspPortScan.from_dict(_port_scan)

        _rna = d.pop("rna", UNSET)
        rna: SnortInspRna | Unset
        if isinstance(_rna, Unset):
            rna = UNSET
        else:
            rna = SnortInspRna.from_dict(_rna)

        _sip = d.pop("sip", UNSET)
        sip: SnortInspSip | Unset
        if isinstance(_sip, Unset):
            sip = UNSET
        else:
            sip = SnortInspSip.from_dict(_sip)

        _smtp = d.pop("smtp", UNSET)
        smtp: SnortInspSmtp | Unset
        if isinstance(_smtp, Unset):
            smtp = UNSET
        else:
            smtp = SnortInspSmtp.from_dict(_smtp)

        _snort_ml = d.pop("snort_ml", UNSET)
        snort_ml: SnortInspSnortMl | Unset
        if isinstance(_snort_ml, Unset):
            snort_ml = UNSET
        else:
            snort_ml = SnortInspSnortMl.from_dict(_snort_ml)

        _snort_ml_engine = d.pop("snort_ml_engine", UNSET)
        snort_ml_engine: SnortInspSnortMlEngine | Unset
        if isinstance(_snort_ml_engine, Unset):
            snort_ml_engine = UNSET
        else:
            snort_ml_engine = SnortInspSnortMlEngine.from_dict(_snort_ml_engine)

        _ssh = d.pop("ssh", UNSET)
        ssh: SnortInspSsh | Unset
        if isinstance(_ssh, Unset):
            ssh = UNSET
        else:
            ssh = SnortInspSsh.from_dict(_ssh)

        _ssl = d.pop("ssl", UNSET)
        ssl: SnortInspSsl | Unset
        if isinstance(_ssl, Unset):
            ssl = UNSET
        else:
            ssl = SnortInspSsl.from_dict(_ssl)

        _stream = d.pop("stream", UNSET)
        stream: SnortInspStream | Unset
        if isinstance(_stream, Unset):
            stream = UNSET
        else:
            stream = SnortInspStream.from_dict(_stream)

        _stream_file = d.pop("stream_file", UNSET)
        stream_file: SnortInspStreamFile | Unset
        if isinstance(_stream_file, Unset):
            stream_file = UNSET
        else:
            stream_file = SnortInspStreamFile.from_dict(_stream_file)

        _stream_icmp = d.pop("stream_icmp", UNSET)
        stream_icmp: SnortInspStreamIcmp | Unset
        if isinstance(_stream_icmp, Unset):
            stream_icmp = UNSET
        else:
            stream_icmp = SnortInspStreamIcmp.from_dict(_stream_icmp)

        _stream_ip = d.pop("stream_ip", UNSET)
        stream_ip: SnortInspStreamIp | Unset
        if isinstance(_stream_ip, Unset):
            stream_ip = UNSET
        else:
            stream_ip = SnortInspStreamIp.from_dict(_stream_ip)

        _stream_tcp = d.pop("stream_tcp", UNSET)
        stream_tcp: SnortInspStreamTcp | Unset
        if isinstance(_stream_tcp, Unset):
            stream_tcp = UNSET
        else:
            stream_tcp = SnortInspStreamTcp.from_dict(_stream_tcp)

        _stream_udp = d.pop("stream_udp", UNSET)
        stream_udp: SnortInspStreamUdp | Unset
        if isinstance(_stream_udp, Unset):
            stream_udp = UNSET
        else:
            stream_udp = SnortInspStreamUdp.from_dict(_stream_udp)

        _stream_user = d.pop("stream_user", UNSET)
        stream_user: SnortInspStreamUser | Unset
        if isinstance(_stream_user, Unset):
            stream_user = UNSET
        else:
            stream_user = SnortInspStreamUser.from_dict(_stream_user)

        _telnet = d.pop("telnet", UNSET)
        telnet: SnortInspTelnet | Unset
        if isinstance(_telnet, Unset):
            telnet = UNSET
        else:
            telnet = SnortInspTelnet.from_dict(_telnet)

        _tlv_pdu = d.pop("tlv_pdu", UNSET)
        tlv_pdu: SnortInspTlvPdu | Unset
        if isinstance(_tlv_pdu, Unset):
            tlv_pdu = UNSET
        else:
            tlv_pdu = SnortInspTlvPdu.from_dict(_tlv_pdu)

        _wizard = d.pop("wizard", UNSET)
        wizard: SnortInspWizard | Unset
        if isinstance(_wizard, Unset):
            wizard = UNSET
        else:
            wizard = SnortInspWizard.from_dict(_wizard)

        snort_inspectors = cls(
            enabled=enabled,
            appid=appid,
            appid_listener=appid_listener,
            arp_spoof=arp_spoof,
            cip=cip,
            data_log=data_log,
            dce_smb=dce_smb,
            dce_tcp=dce_tcp,
            dce_udp=dce_udp,
            dnp3=dnp3,
            dns=dns,
            domain_filter=domain_filter,
            dpx=dpx,
            extractor=extractor,
            file_id=file_id,
            file_log=file_log,
            ftp_client=ftp_client,
            ftp_server=ftp_server,
            gtp_inspect=gtp_inspect,
            http2_inspect=http2_inspect,
            http_inspect=http_inspect,
            imap=imap,
            netflow=netflow,
            normalizer=normalizer,
            packet_capture=packet_capture,
            perf_monitor=perf_monitor,
            pop=pop,
            port_scan=port_scan,
            rna=rna,
            sip=sip,
            smtp=smtp,
            snort_ml=snort_ml,
            snort_ml_engine=snort_ml_engine,
            ssh=ssh,
            ssl=ssl,
            stream=stream,
            stream_file=stream_file,
            stream_icmp=stream_icmp,
            stream_ip=stream_ip,
            stream_tcp=stream_tcp,
            stream_udp=stream_udp,
            stream_user=stream_user,
            telnet=telnet,
            tlv_pdu=tlv_pdu,
            wizard=wizard,
        )

        snort_inspectors.additional_properties = d
        return snort_inspectors

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
