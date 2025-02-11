from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Interface")


@_attrs_define
class Interface:
    """Detailed interface information

    Attributes:
        name (str): alias to assigned name
        if_ (str): alias to device_name
        assigned_name (str): user assigned name, e.g. MYLAN
        device_name (str): host device name, e.g. ix1
        identity (str): unique identity of device, e.g. opt1
        enable (bool):
        blockbogons (bool):
        pseudo (bool):
        blockpriv (bool):
        slaacusev4iface (bool):
        descr (str):
        type (str):
        type6 (str):
        promisc (bool):
        ipaddr (str):
        member (str):
        mac (str):
        mediaopt (str):
        spoofmac (str):
        gateway (str):
        ipaddrv6 (str):
        ipv6usev4iface (bool):
        defaultgw6 (bool):
        gatewayip6 (str):
        gatewayv6 (str):
        gatewaydescr6 (str):
        gatewayname6 (str):
        alias_address (str):
        dhcphostname (str):
        dhcprejectfrom (str):
        dhcprejectfromarray (List[str]):
        dhcpvlanenable (bool):
        dhcp6usev4iface (bool):
        dhcp6prefixonly (bool):
        dhcp6_ia_pd_send_hint (bool):
        dhcp6debug (bool):
        dhcp6withoutra (bool):
        dhcp6norelease (bool):
        dhcpcvpt (str):
        dhcp6cvpt (str):
        prefix_6rd (str):
        gateway_6rd (str):
        track6_prefix_id_hex (str):
        dhcp6_ia_pd_len (str):
        prefix_6rd_v4plen (str):
        track6_interface (str):
        adv_dhcp_config_advanced (bool):
        adv_dhcp_config_file_override (bool):
        adv_dhcp_pt_timeout (str):
        adv_dhcp_pt_retry (str):
        adv_dhcp_pt_select_timeout (str):
        adv_dhcp_pt_reboot (str):
        adv_dhcp_pt_backoff_cutoff (str):
        adv_dhcp_pt_initial_interval (str):
        adv_dhcp_pt_values (str):
        adv_dhcp_config_file_override_path (str):
        adv_dhcp_send_options (str):
        adv_dhcp_request_options (str):
        adv_dhcp_required_options (str):
        adv_dhcp_option_modifiers (str):
        adv_dhcp6_config_advanced (bool):
        adv_dhcp6_config_file_override (bool):
        adv_dhcp6_prefix_selected_interface (str):
        adv_dhcp6_config_file_override_path (str):
        adv_dhcp6_interface_statement_information_only_enable (bool):
        adv_dhcp6_interface_statement_send_options (str):
        adv_dhcp6_interface_statement_request_options (str):
        adv_dhcp6_interface_statement_script (str):
        adv_dhcp6_id_assoc_statement_address_enable (bool):
        adv_dhcp6_id_assoc_statement_address_id (str):
        adv_dhcp6_id_assoc_statement_address (str):
        adv_dhcp6_id_assoc_statement_address_pltime (str):
        adv_dhcp6_id_assoc_statement_address_vltime (str):
        adv_dhcp6_id_assoc_statement_prefix_enable (bool):
        adv_dhcp6_id_assoc_statement_prefix_id (str):
        adv_dhcp6_id_assoc_statement_prefix (str):
        adv_dhcp6_id_assoc_statement_prefix_pltime (str):
        adv_dhcp6_id_assoc_statement_prefix_vltime (str):
        adv_dhcp6_prefix_interface_statement_sla_id (str):
        adv_dhcp6_prefix_interface_statement_sla_len (str):
        adv_dhcp6_authentication_statement_authname (str):
        adv_dhcp6_authentication_statement_protocol (str):
        adv_dhcp6_authentication_statement_algorithm (str):
        adv_dhcp6_authentication_statement_rdm (str):
        adv_dhcp6_key_info_statement_keyname (str):
        adv_dhcp6_key_info_statement_realm (str):
        adv_dhcp6_key_info_statement_keyid (str):
        adv_dhcp6_key_info_statement_secret (str):
        adv_dhcp6_key_info_statement_expire (str):
        mtu (Union[Unset, int]):
        mss (Union[Unset, int]):
        pcp (Union[Unset, int]):
        media (Union[Unset, str]):
        tag (Union[Unset, int]):
    """

    name: str
    if_: str
    assigned_name: str
    device_name: str
    identity: str
    enable: bool
    blockbogons: bool
    pseudo: bool
    blockpriv: bool
    slaacusev4iface: bool
    descr: str
    type: str
    type6: str
    promisc: bool
    ipaddr: str
    member: str
    mac: str
    mediaopt: str
    spoofmac: str
    gateway: str
    ipaddrv6: str
    ipv6usev4iface: bool
    defaultgw6: bool
    gatewayip6: str
    gatewayv6: str
    gatewaydescr6: str
    gatewayname6: str
    alias_address: str
    dhcphostname: str
    dhcprejectfrom: str
    dhcprejectfromarray: List[str]
    dhcpvlanenable: bool
    dhcp6usev4iface: bool
    dhcp6prefixonly: bool
    dhcp6_ia_pd_send_hint: bool
    dhcp6debug: bool
    dhcp6withoutra: bool
    dhcp6norelease: bool
    dhcpcvpt: str
    dhcp6cvpt: str
    prefix_6rd: str
    gateway_6rd: str
    track6_prefix_id_hex: str
    dhcp6_ia_pd_len: str
    prefix_6rd_v4plen: str
    track6_interface: str
    adv_dhcp_config_advanced: bool
    adv_dhcp_config_file_override: bool
    adv_dhcp_pt_timeout: str
    adv_dhcp_pt_retry: str
    adv_dhcp_pt_select_timeout: str
    adv_dhcp_pt_reboot: str
    adv_dhcp_pt_backoff_cutoff: str
    adv_dhcp_pt_initial_interval: str
    adv_dhcp_pt_values: str
    adv_dhcp_config_file_override_path: str
    adv_dhcp_send_options: str
    adv_dhcp_request_options: str
    adv_dhcp_required_options: str
    adv_dhcp_option_modifiers: str
    adv_dhcp6_config_advanced: bool
    adv_dhcp6_config_file_override: bool
    adv_dhcp6_prefix_selected_interface: str
    adv_dhcp6_config_file_override_path: str
    adv_dhcp6_interface_statement_information_only_enable: bool
    adv_dhcp6_interface_statement_send_options: str
    adv_dhcp6_interface_statement_request_options: str
    adv_dhcp6_interface_statement_script: str
    adv_dhcp6_id_assoc_statement_address_enable: bool
    adv_dhcp6_id_assoc_statement_address_id: str
    adv_dhcp6_id_assoc_statement_address: str
    adv_dhcp6_id_assoc_statement_address_pltime: str
    adv_dhcp6_id_assoc_statement_address_vltime: str
    adv_dhcp6_id_assoc_statement_prefix_enable: bool
    adv_dhcp6_id_assoc_statement_prefix_id: str
    adv_dhcp6_id_assoc_statement_prefix: str
    adv_dhcp6_id_assoc_statement_prefix_pltime: str
    adv_dhcp6_id_assoc_statement_prefix_vltime: str
    adv_dhcp6_prefix_interface_statement_sla_id: str
    adv_dhcp6_prefix_interface_statement_sla_len: str
    adv_dhcp6_authentication_statement_authname: str
    adv_dhcp6_authentication_statement_protocol: str
    adv_dhcp6_authentication_statement_algorithm: str
    adv_dhcp6_authentication_statement_rdm: str
    adv_dhcp6_key_info_statement_keyname: str
    adv_dhcp6_key_info_statement_realm: str
    adv_dhcp6_key_info_statement_keyid: str
    adv_dhcp6_key_info_statement_secret: str
    adv_dhcp6_key_info_statement_expire: str
    mtu: Union[Unset, int] = UNSET
    mss: Union[Unset, int] = UNSET
    pcp: Union[Unset, int] = UNSET
    media: Union[Unset, str] = UNSET
    tag: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        if_ = self.if_

        assigned_name = self.assigned_name

        device_name = self.device_name

        identity = self.identity

        enable = self.enable

        blockbogons = self.blockbogons

        pseudo = self.pseudo

        blockpriv = self.blockpriv

        slaacusev4iface = self.slaacusev4iface

        descr = self.descr

        type = self.type

        type6 = self.type6

        promisc = self.promisc

        ipaddr = self.ipaddr

        member = self.member

        mac = self.mac

        mediaopt = self.mediaopt

        spoofmac = self.spoofmac

        gateway = self.gateway

        ipaddrv6 = self.ipaddrv6

        ipv6usev4iface = self.ipv6usev4iface

        defaultgw6 = self.defaultgw6

        gatewayip6 = self.gatewayip6

        gatewayv6 = self.gatewayv6

        gatewaydescr6 = self.gatewaydescr6

        gatewayname6 = self.gatewayname6

        alias_address = self.alias_address

        dhcphostname = self.dhcphostname

        dhcprejectfrom = self.dhcprejectfrom

        dhcprejectfromarray = self.dhcprejectfromarray

        dhcpvlanenable = self.dhcpvlanenable

        dhcp6usev4iface = self.dhcp6usev4iface

        dhcp6prefixonly = self.dhcp6prefixonly

        dhcp6_ia_pd_send_hint = self.dhcp6_ia_pd_send_hint

        dhcp6debug = self.dhcp6debug

        dhcp6withoutra = self.dhcp6withoutra

        dhcp6norelease = self.dhcp6norelease

        dhcpcvpt = self.dhcpcvpt

        dhcp6cvpt = self.dhcp6cvpt

        prefix_6rd = self.prefix_6rd

        gateway_6rd = self.gateway_6rd

        track6_prefix_id_hex = self.track6_prefix_id_hex

        dhcp6_ia_pd_len = self.dhcp6_ia_pd_len

        prefix_6rd_v4plen = self.prefix_6rd_v4plen

        track6_interface = self.track6_interface

        adv_dhcp_config_advanced = self.adv_dhcp_config_advanced

        adv_dhcp_config_file_override = self.adv_dhcp_config_file_override

        adv_dhcp_pt_timeout = self.adv_dhcp_pt_timeout

        adv_dhcp_pt_retry = self.adv_dhcp_pt_retry

        adv_dhcp_pt_select_timeout = self.adv_dhcp_pt_select_timeout

        adv_dhcp_pt_reboot = self.adv_dhcp_pt_reboot

        adv_dhcp_pt_backoff_cutoff = self.adv_dhcp_pt_backoff_cutoff

        adv_dhcp_pt_initial_interval = self.adv_dhcp_pt_initial_interval

        adv_dhcp_pt_values = self.adv_dhcp_pt_values

        adv_dhcp_config_file_override_path = self.adv_dhcp_config_file_override_path

        adv_dhcp_send_options = self.adv_dhcp_send_options

        adv_dhcp_request_options = self.adv_dhcp_request_options

        adv_dhcp_required_options = self.adv_dhcp_required_options

        adv_dhcp_option_modifiers = self.adv_dhcp_option_modifiers

        adv_dhcp6_config_advanced = self.adv_dhcp6_config_advanced

        adv_dhcp6_config_file_override = self.adv_dhcp6_config_file_override

        adv_dhcp6_prefix_selected_interface = self.adv_dhcp6_prefix_selected_interface

        adv_dhcp6_config_file_override_path = self.adv_dhcp6_config_file_override_path

        adv_dhcp6_interface_statement_information_only_enable = (
            self.adv_dhcp6_interface_statement_information_only_enable
        )

        adv_dhcp6_interface_statement_send_options = self.adv_dhcp6_interface_statement_send_options

        adv_dhcp6_interface_statement_request_options = self.adv_dhcp6_interface_statement_request_options

        adv_dhcp6_interface_statement_script = self.adv_dhcp6_interface_statement_script

        adv_dhcp6_id_assoc_statement_address_enable = self.adv_dhcp6_id_assoc_statement_address_enable

        adv_dhcp6_id_assoc_statement_address_id = self.adv_dhcp6_id_assoc_statement_address_id

        adv_dhcp6_id_assoc_statement_address = self.adv_dhcp6_id_assoc_statement_address

        adv_dhcp6_id_assoc_statement_address_pltime = self.adv_dhcp6_id_assoc_statement_address_pltime

        adv_dhcp6_id_assoc_statement_address_vltime = self.adv_dhcp6_id_assoc_statement_address_vltime

        adv_dhcp6_id_assoc_statement_prefix_enable = self.adv_dhcp6_id_assoc_statement_prefix_enable

        adv_dhcp6_id_assoc_statement_prefix_id = self.adv_dhcp6_id_assoc_statement_prefix_id

        adv_dhcp6_id_assoc_statement_prefix = self.adv_dhcp6_id_assoc_statement_prefix

        adv_dhcp6_id_assoc_statement_prefix_pltime = self.adv_dhcp6_id_assoc_statement_prefix_pltime

        adv_dhcp6_id_assoc_statement_prefix_vltime = self.adv_dhcp6_id_assoc_statement_prefix_vltime

        adv_dhcp6_prefix_interface_statement_sla_id = self.adv_dhcp6_prefix_interface_statement_sla_id

        adv_dhcp6_prefix_interface_statement_sla_len = self.adv_dhcp6_prefix_interface_statement_sla_len

        adv_dhcp6_authentication_statement_authname = self.adv_dhcp6_authentication_statement_authname

        adv_dhcp6_authentication_statement_protocol = self.adv_dhcp6_authentication_statement_protocol

        adv_dhcp6_authentication_statement_algorithm = self.adv_dhcp6_authentication_statement_algorithm

        adv_dhcp6_authentication_statement_rdm = self.adv_dhcp6_authentication_statement_rdm

        adv_dhcp6_key_info_statement_keyname = self.adv_dhcp6_key_info_statement_keyname

        adv_dhcp6_key_info_statement_realm = self.adv_dhcp6_key_info_statement_realm

        adv_dhcp6_key_info_statement_keyid = self.adv_dhcp6_key_info_statement_keyid

        adv_dhcp6_key_info_statement_secret = self.adv_dhcp6_key_info_statement_secret

        adv_dhcp6_key_info_statement_expire = self.adv_dhcp6_key_info_statement_expire

        mtu = self.mtu

        mss = self.mss

        pcp = self.pcp

        media = self.media

        tag = self.tag

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "if": if_,
                "assigned_name": assigned_name,
                "device_name": device_name,
                "identity": identity,
                "enable": enable,
                "blockbogons": blockbogons,
                "pseudo": pseudo,
                "blockpriv": blockpriv,
                "slaacusev4iface": slaacusev4iface,
                "descr": descr,
                "type": type,
                "type6": type6,
                "promisc": promisc,
                "ipaddr": ipaddr,
                "member": member,
                "mac": mac,
                "mediaopt": mediaopt,
                "spoofmac": spoofmac,
                "gateway": gateway,
                "ipaddrv6": ipaddrv6,
                "ipv6usev4iface": ipv6usev4iface,
                "defaultgw6": defaultgw6,
                "gatewayip6": gatewayip6,
                "gatewayv6": gatewayv6,
                "gatewaydescr6": gatewaydescr6,
                "gatewayname6": gatewayname6,
                "alias_address": alias_address,
                "dhcphostname": dhcphostname,
                "dhcprejectfrom": dhcprejectfrom,
                "dhcprejectfromarray": dhcprejectfromarray,
                "dhcpvlanenable": dhcpvlanenable,
                "dhcp6usev4iface": dhcp6usev4iface,
                "dhcp6prefixonly": dhcp6prefixonly,
                "dhcp6_ia_pd_send_hint": dhcp6_ia_pd_send_hint,
                "dhcp6debug": dhcp6debug,
                "dhcp6withoutra": dhcp6withoutra,
                "dhcp6norelease": dhcp6norelease,
                "dhcpcvpt": dhcpcvpt,
                "dhcp6cvpt": dhcp6cvpt,
                "prefix_6rd": prefix_6rd,
                "gateway_6rd": gateway_6rd,
                "track6_prefix_id__hex": track6_prefix_id_hex,
                "dhcp6_ia_pd_len": dhcp6_ia_pd_len,
                "prefix_6rd_v4plen": prefix_6rd_v4plen,
                "track6_interface": track6_interface,
                "adv_dhcp_config_advanced": adv_dhcp_config_advanced,
                "adv_dhcp_config_file_override": adv_dhcp_config_file_override,
                "adv_dhcp_pt_timeout": adv_dhcp_pt_timeout,
                "adv_dhcp_pt_retry": adv_dhcp_pt_retry,
                "adv_dhcp_pt_select_timeout": adv_dhcp_pt_select_timeout,
                "adv_dhcp_pt_reboot": adv_dhcp_pt_reboot,
                "adv_dhcp_pt_backoff_cutoff": adv_dhcp_pt_backoff_cutoff,
                "adv_dhcp_pt_initial_interval": adv_dhcp_pt_initial_interval,
                "adv_dhcp_pt_values": adv_dhcp_pt_values,
                "adv_dhcp_config_file_override_path": adv_dhcp_config_file_override_path,
                "adv_dhcp_send_options": adv_dhcp_send_options,
                "adv_dhcp_request_options": adv_dhcp_request_options,
                "adv_dhcp_required_options": adv_dhcp_required_options,
                "adv_dhcp_option_modifiers": adv_dhcp_option_modifiers,
                "adv_dhcp6_config_advanced": adv_dhcp6_config_advanced,
                "adv_dhcp6_config_file_override": adv_dhcp6_config_file_override,
                "adv_dhcp6_prefix_selected_interface": adv_dhcp6_prefix_selected_interface,
                "adv_dhcp6_config_file_override_path": adv_dhcp6_config_file_override_path,
                "adv_dhcp6_interface_statement_information_only_enable": adv_dhcp6_interface_statement_information_only_enable,
                "adv_dhcp6_interface_statement_send_options": adv_dhcp6_interface_statement_send_options,
                "adv_dhcp6_interface_statement_request_options": adv_dhcp6_interface_statement_request_options,
                "adv_dhcp6_interface_statement_script": adv_dhcp6_interface_statement_script,
                "adv_dhcp6_id_assoc_statement_address_enable": adv_dhcp6_id_assoc_statement_address_enable,
                "adv_dhcp6_id_assoc_statement_address_id": adv_dhcp6_id_assoc_statement_address_id,
                "adv_dhcp6_id_assoc_statement_address": adv_dhcp6_id_assoc_statement_address,
                "adv_dhcp6_id_assoc_statement_address_pltime": adv_dhcp6_id_assoc_statement_address_pltime,
                "adv_dhcp6_id_assoc_statement_address_vltime": adv_dhcp6_id_assoc_statement_address_vltime,
                "adv_dhcp6_id_assoc_statement_prefix_enable": adv_dhcp6_id_assoc_statement_prefix_enable,
                "adv_dhcp6_id_assoc_statement_prefix_id": adv_dhcp6_id_assoc_statement_prefix_id,
                "adv_dhcp6_id_assoc_statement_prefix": adv_dhcp6_id_assoc_statement_prefix,
                "adv_dhcp6_id_assoc_statement_prefix_pltime": adv_dhcp6_id_assoc_statement_prefix_pltime,
                "adv_dhcp6_id_assoc_statement_prefix_vltime": adv_dhcp6_id_assoc_statement_prefix_vltime,
                "adv_dhcp6_prefix_interface_statement_sla_id": adv_dhcp6_prefix_interface_statement_sla_id,
                "adv_dhcp6_prefix_interface_statement_sla_len": adv_dhcp6_prefix_interface_statement_sla_len,
                "adv_dhcp6_authentication_statement_authname": adv_dhcp6_authentication_statement_authname,
                "adv_dhcp6_authentication_statement_protocol": adv_dhcp6_authentication_statement_protocol,
                "adv_dhcp6_authentication_statement_algorithm": adv_dhcp6_authentication_statement_algorithm,
                "adv_dhcp6_authentication_statement_rdm": adv_dhcp6_authentication_statement_rdm,
                "adv_dhcp6_key_info_statement_keyname": adv_dhcp6_key_info_statement_keyname,
                "adv_dhcp6_key_info_statement_realm": adv_dhcp6_key_info_statement_realm,
                "adv_dhcp6_key_info_statement_keyid": adv_dhcp6_key_info_statement_keyid,
                "adv_dhcp6_key_info_statement_secret": adv_dhcp6_key_info_statement_secret,
                "adv_dhcp6_key_info_statement_expire": adv_dhcp6_key_info_statement_expire,
            }
        )
        if mtu is not UNSET:
            field_dict["mtu"] = mtu
        if mss is not UNSET:
            field_dict["mss"] = mss
        if pcp is not UNSET:
            field_dict["pcp"] = pcp
        if media is not UNSET:
            field_dict["media"] = media
        if tag is not UNSET:
            field_dict["tag"] = tag

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        if_ = d.pop("if")

        assigned_name = d.pop("assigned_name")

        device_name = d.pop("device_name")

        identity = d.pop("identity")

        enable = d.pop("enable")

        blockbogons = d.pop("blockbogons")

        pseudo = d.pop("pseudo")

        blockpriv = d.pop("blockpriv")

        slaacusev4iface = d.pop("slaacusev4iface")

        descr = d.pop("descr")

        type = d.pop("type")

        type6 = d.pop("type6")

        promisc = d.pop("promisc")

        ipaddr = d.pop("ipaddr")

        member = d.pop("member")

        mac = d.pop("mac")

        mediaopt = d.pop("mediaopt")

        spoofmac = d.pop("spoofmac")

        gateway = d.pop("gateway")

        ipaddrv6 = d.pop("ipaddrv6")

        ipv6usev4iface = d.pop("ipv6usev4iface")

        defaultgw6 = d.pop("defaultgw6")

        gatewayip6 = d.pop("gatewayip6")

        gatewayv6 = d.pop("gatewayv6")

        gatewaydescr6 = d.pop("gatewaydescr6")

        gatewayname6 = d.pop("gatewayname6")

        alias_address = d.pop("alias_address")

        dhcphostname = d.pop("dhcphostname")

        dhcprejectfrom = d.pop("dhcprejectfrom")

        dhcprejectfromarray = cast(List[str], d.pop("dhcprejectfromarray"))

        dhcpvlanenable = d.pop("dhcpvlanenable")

        dhcp6usev4iface = d.pop("dhcp6usev4iface")

        dhcp6prefixonly = d.pop("dhcp6prefixonly")

        dhcp6_ia_pd_send_hint = d.pop("dhcp6_ia_pd_send_hint")

        dhcp6debug = d.pop("dhcp6debug")

        dhcp6withoutra = d.pop("dhcp6withoutra")

        dhcp6norelease = d.pop("dhcp6norelease")

        dhcpcvpt = d.pop("dhcpcvpt")

        dhcp6cvpt = d.pop("dhcp6cvpt")

        prefix_6rd = d.pop("prefix_6rd")

        gateway_6rd = d.pop("gateway_6rd")

        track6_prefix_id_hex = d.pop("track6_prefix_id__hex")

        dhcp6_ia_pd_len = d.pop("dhcp6_ia_pd_len")

        prefix_6rd_v4plen = d.pop("prefix_6rd_v4plen")

        track6_interface = d.pop("track6_interface")

        adv_dhcp_config_advanced = d.pop("adv_dhcp_config_advanced")

        adv_dhcp_config_file_override = d.pop("adv_dhcp_config_file_override")

        adv_dhcp_pt_timeout = d.pop("adv_dhcp_pt_timeout")

        adv_dhcp_pt_retry = d.pop("adv_dhcp_pt_retry")

        adv_dhcp_pt_select_timeout = d.pop("adv_dhcp_pt_select_timeout")

        adv_dhcp_pt_reboot = d.pop("adv_dhcp_pt_reboot")

        adv_dhcp_pt_backoff_cutoff = d.pop("adv_dhcp_pt_backoff_cutoff")

        adv_dhcp_pt_initial_interval = d.pop("adv_dhcp_pt_initial_interval")

        adv_dhcp_pt_values = d.pop("adv_dhcp_pt_values")

        adv_dhcp_config_file_override_path = d.pop("adv_dhcp_config_file_override_path")

        adv_dhcp_send_options = d.pop("adv_dhcp_send_options")

        adv_dhcp_request_options = d.pop("adv_dhcp_request_options")

        adv_dhcp_required_options = d.pop("adv_dhcp_required_options")

        adv_dhcp_option_modifiers = d.pop("adv_dhcp_option_modifiers")

        adv_dhcp6_config_advanced = d.pop("adv_dhcp6_config_advanced")

        adv_dhcp6_config_file_override = d.pop("adv_dhcp6_config_file_override")

        adv_dhcp6_prefix_selected_interface = d.pop("adv_dhcp6_prefix_selected_interface")

        adv_dhcp6_config_file_override_path = d.pop("adv_dhcp6_config_file_override_path")

        adv_dhcp6_interface_statement_information_only_enable = d.pop(
            "adv_dhcp6_interface_statement_information_only_enable"
        )

        adv_dhcp6_interface_statement_send_options = d.pop("adv_dhcp6_interface_statement_send_options")

        adv_dhcp6_interface_statement_request_options = d.pop("adv_dhcp6_interface_statement_request_options")

        adv_dhcp6_interface_statement_script = d.pop("adv_dhcp6_interface_statement_script")

        adv_dhcp6_id_assoc_statement_address_enable = d.pop("adv_dhcp6_id_assoc_statement_address_enable")

        adv_dhcp6_id_assoc_statement_address_id = d.pop("adv_dhcp6_id_assoc_statement_address_id")

        adv_dhcp6_id_assoc_statement_address = d.pop("adv_dhcp6_id_assoc_statement_address")

        adv_dhcp6_id_assoc_statement_address_pltime = d.pop("adv_dhcp6_id_assoc_statement_address_pltime")

        adv_dhcp6_id_assoc_statement_address_vltime = d.pop("adv_dhcp6_id_assoc_statement_address_vltime")

        adv_dhcp6_id_assoc_statement_prefix_enable = d.pop("adv_dhcp6_id_assoc_statement_prefix_enable")

        adv_dhcp6_id_assoc_statement_prefix_id = d.pop("adv_dhcp6_id_assoc_statement_prefix_id")

        adv_dhcp6_id_assoc_statement_prefix = d.pop("adv_dhcp6_id_assoc_statement_prefix")

        adv_dhcp6_id_assoc_statement_prefix_pltime = d.pop("adv_dhcp6_id_assoc_statement_prefix_pltime")

        adv_dhcp6_id_assoc_statement_prefix_vltime = d.pop("adv_dhcp6_id_assoc_statement_prefix_vltime")

        adv_dhcp6_prefix_interface_statement_sla_id = d.pop("adv_dhcp6_prefix_interface_statement_sla_id")

        adv_dhcp6_prefix_interface_statement_sla_len = d.pop("adv_dhcp6_prefix_interface_statement_sla_len")

        adv_dhcp6_authentication_statement_authname = d.pop("adv_dhcp6_authentication_statement_authname")

        adv_dhcp6_authentication_statement_protocol = d.pop("adv_dhcp6_authentication_statement_protocol")

        adv_dhcp6_authentication_statement_algorithm = d.pop("adv_dhcp6_authentication_statement_algorithm")

        adv_dhcp6_authentication_statement_rdm = d.pop("adv_dhcp6_authentication_statement_rdm")

        adv_dhcp6_key_info_statement_keyname = d.pop("adv_dhcp6_key_info_statement_keyname")

        adv_dhcp6_key_info_statement_realm = d.pop("adv_dhcp6_key_info_statement_realm")

        adv_dhcp6_key_info_statement_keyid = d.pop("adv_dhcp6_key_info_statement_keyid")

        adv_dhcp6_key_info_statement_secret = d.pop("adv_dhcp6_key_info_statement_secret")

        adv_dhcp6_key_info_statement_expire = d.pop("adv_dhcp6_key_info_statement_expire")

        mtu = d.pop("mtu", UNSET)

        mss = d.pop("mss", UNSET)

        pcp = d.pop("pcp", UNSET)

        media = d.pop("media", UNSET)

        tag = d.pop("tag", UNSET)

        interface = cls(
            name=name,
            if_=if_,
            assigned_name=assigned_name,
            device_name=device_name,
            identity=identity,
            enable=enable,
            blockbogons=blockbogons,
            pseudo=pseudo,
            blockpriv=blockpriv,
            slaacusev4iface=slaacusev4iface,
            descr=descr,
            type=type,
            type6=type6,
            promisc=promisc,
            ipaddr=ipaddr,
            member=member,
            mac=mac,
            mediaopt=mediaopt,
            spoofmac=spoofmac,
            gateway=gateway,
            ipaddrv6=ipaddrv6,
            ipv6usev4iface=ipv6usev4iface,
            defaultgw6=defaultgw6,
            gatewayip6=gatewayip6,
            gatewayv6=gatewayv6,
            gatewaydescr6=gatewaydescr6,
            gatewayname6=gatewayname6,
            alias_address=alias_address,
            dhcphostname=dhcphostname,
            dhcprejectfrom=dhcprejectfrom,
            dhcprejectfromarray=dhcprejectfromarray,
            dhcpvlanenable=dhcpvlanenable,
            dhcp6usev4iface=dhcp6usev4iface,
            dhcp6prefixonly=dhcp6prefixonly,
            dhcp6_ia_pd_send_hint=dhcp6_ia_pd_send_hint,
            dhcp6debug=dhcp6debug,
            dhcp6withoutra=dhcp6withoutra,
            dhcp6norelease=dhcp6norelease,
            dhcpcvpt=dhcpcvpt,
            dhcp6cvpt=dhcp6cvpt,
            prefix_6rd=prefix_6rd,
            gateway_6rd=gateway_6rd,
            track6_prefix_id_hex=track6_prefix_id_hex,
            dhcp6_ia_pd_len=dhcp6_ia_pd_len,
            prefix_6rd_v4plen=prefix_6rd_v4plen,
            track6_interface=track6_interface,
            adv_dhcp_config_advanced=adv_dhcp_config_advanced,
            adv_dhcp_config_file_override=adv_dhcp_config_file_override,
            adv_dhcp_pt_timeout=adv_dhcp_pt_timeout,
            adv_dhcp_pt_retry=adv_dhcp_pt_retry,
            adv_dhcp_pt_select_timeout=adv_dhcp_pt_select_timeout,
            adv_dhcp_pt_reboot=adv_dhcp_pt_reboot,
            adv_dhcp_pt_backoff_cutoff=adv_dhcp_pt_backoff_cutoff,
            adv_dhcp_pt_initial_interval=adv_dhcp_pt_initial_interval,
            adv_dhcp_pt_values=adv_dhcp_pt_values,
            adv_dhcp_config_file_override_path=adv_dhcp_config_file_override_path,
            adv_dhcp_send_options=adv_dhcp_send_options,
            adv_dhcp_request_options=adv_dhcp_request_options,
            adv_dhcp_required_options=adv_dhcp_required_options,
            adv_dhcp_option_modifiers=adv_dhcp_option_modifiers,
            adv_dhcp6_config_advanced=adv_dhcp6_config_advanced,
            adv_dhcp6_config_file_override=adv_dhcp6_config_file_override,
            adv_dhcp6_prefix_selected_interface=adv_dhcp6_prefix_selected_interface,
            adv_dhcp6_config_file_override_path=adv_dhcp6_config_file_override_path,
            adv_dhcp6_interface_statement_information_only_enable=adv_dhcp6_interface_statement_information_only_enable,
            adv_dhcp6_interface_statement_send_options=adv_dhcp6_interface_statement_send_options,
            adv_dhcp6_interface_statement_request_options=adv_dhcp6_interface_statement_request_options,
            adv_dhcp6_interface_statement_script=adv_dhcp6_interface_statement_script,
            adv_dhcp6_id_assoc_statement_address_enable=adv_dhcp6_id_assoc_statement_address_enable,
            adv_dhcp6_id_assoc_statement_address_id=adv_dhcp6_id_assoc_statement_address_id,
            adv_dhcp6_id_assoc_statement_address=adv_dhcp6_id_assoc_statement_address,
            adv_dhcp6_id_assoc_statement_address_pltime=adv_dhcp6_id_assoc_statement_address_pltime,
            adv_dhcp6_id_assoc_statement_address_vltime=adv_dhcp6_id_assoc_statement_address_vltime,
            adv_dhcp6_id_assoc_statement_prefix_enable=adv_dhcp6_id_assoc_statement_prefix_enable,
            adv_dhcp6_id_assoc_statement_prefix_id=adv_dhcp6_id_assoc_statement_prefix_id,
            adv_dhcp6_id_assoc_statement_prefix=adv_dhcp6_id_assoc_statement_prefix,
            adv_dhcp6_id_assoc_statement_prefix_pltime=adv_dhcp6_id_assoc_statement_prefix_pltime,
            adv_dhcp6_id_assoc_statement_prefix_vltime=adv_dhcp6_id_assoc_statement_prefix_vltime,
            adv_dhcp6_prefix_interface_statement_sla_id=adv_dhcp6_prefix_interface_statement_sla_id,
            adv_dhcp6_prefix_interface_statement_sla_len=adv_dhcp6_prefix_interface_statement_sla_len,
            adv_dhcp6_authentication_statement_authname=adv_dhcp6_authentication_statement_authname,
            adv_dhcp6_authentication_statement_protocol=adv_dhcp6_authentication_statement_protocol,
            adv_dhcp6_authentication_statement_algorithm=adv_dhcp6_authentication_statement_algorithm,
            adv_dhcp6_authentication_statement_rdm=adv_dhcp6_authentication_statement_rdm,
            adv_dhcp6_key_info_statement_keyname=adv_dhcp6_key_info_statement_keyname,
            adv_dhcp6_key_info_statement_realm=adv_dhcp6_key_info_statement_realm,
            adv_dhcp6_key_info_statement_keyid=adv_dhcp6_key_info_statement_keyid,
            adv_dhcp6_key_info_statement_secret=adv_dhcp6_key_info_statement_secret,
            adv_dhcp6_key_info_statement_expire=adv_dhcp6_key_info_statement_expire,
            mtu=mtu,
            mss=mss,
            pcp=pcp,
            media=media,
            tag=tag,
        )

        interface.additional_properties = d
        return interface

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
