from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Interface")


@_attrs_define
class Interface:
    """Detailed interface information

    Attributes:
        name (Union[Unset, str]):
        enable (Union[Unset, bool]):
        blockbogons (Union[Unset, bool]):
        pseudo (Union[Unset, bool]):
        blockpriv (Union[Unset, bool]):
        slaacusev4iface (Union[Unset, bool]):
        if_ (Union[Unset, str]):
        descr (Union[Unset, str]):
        type (Union[Unset, str]):
        type6 (Union[Unset, str]):
        mtu (Union[Unset, int]):
        mss (Union[Unset, int]):
        pcp (Union[Unset, int]):
        promisc (Union[Unset, bool]):
        ipaddr (Union[Unset, str]):
        member (Union[Unset, str]):
        media (Union[Unset, str]):
        mac (Union[Unset, str]):
        mediaopt (Union[Unset, str]):
        spoofmac (Union[Unset, str]):
        tag (Union[Unset, int]):
        gateway (Union[Unset, str]):
        ipaddrv6 (Union[Unset, str]):
        ipv6usev4iface (Union[Unset, bool]):
        defaultgw6 (Union[Unset, bool]):
        gatewayip6 (Union[Unset, str]):
        gatewayv6 (Union[Unset, str]):
        gatewaydescr6 (Union[Unset, str]):
        gatewayname6 (Union[Unset, str]):
        alias_address (Union[Unset, str]):
        dhcphostname (Union[Unset, str]):
        dhcprejectfrom (Union[Unset, str]):
        dhcprejectfromarray (Union[Unset, List[str]]):
        dhcpvlanenable (Union[Unset, bool]):
        dhcp6usev4iface (Union[Unset, bool]):
        dhcp6prefixonly (Union[Unset, bool]):
        dhcp6_ia_pd_send_hint (Union[Unset, bool]):
        dhcp6debug (Union[Unset, bool]):
        dhcp6withoutra (Union[Unset, bool]):
        dhcp6norelease (Union[Unset, bool]):
        dhcpcvpt (Union[Unset, str]):
        dhcp6cvpt (Union[Unset, str]):
        prefix_6rd (Union[Unset, str]):
        gateway_6rd (Union[Unset, str]):
        track6_prefix_id_hex (Union[Unset, str]):
        dhcp6_ia_pd_len (Union[Unset, str]):
        prefix_6rd_v4plen (Union[Unset, str]):
        track6_interface (Union[Unset, str]):
        adv_dhcp_config_advanced (Union[Unset, bool]):
        adv_dhcp_config_file_override (Union[Unset, bool]):
        adv_dhcp_pt_timeout (Union[Unset, str]):
        adv_dhcp_pt_retry (Union[Unset, str]):
        adv_dhcp_pt_select_timeout (Union[Unset, str]):
        adv_dhcp_pt_reboot (Union[Unset, str]):
        adv_dhcp_pt_backoff_cutoff (Union[Unset, str]):
        adv_dhcp_pt_initial_interval (Union[Unset, str]):
        adv_dhcp_pt_values (Union[Unset, str]):
        adv_dhcp_config_file_override_path (Union[Unset, str]):
        adv_dhcp_send_options (Union[Unset, str]):
        adv_dhcp_request_options (Union[Unset, str]):
        adv_dhcp_required_options (Union[Unset, str]):
        adv_dhcp_option_modifiers (Union[Unset, str]):
        adv_dhcp6_config_advanced (Union[Unset, bool]):
        adv_dhcp6_config_file_override (Union[Unset, bool]):
        adv_dhcp6_prefix_selected_interface (Union[Unset, str]):
        adv_dhcp6_config_file_override_path (Union[Unset, str]):
        adv_dhcp6_interface_statement_information_only_enable (Union[Unset, bool]):
        adv_dhcp6_interface_statement_send_options (Union[Unset, str]):
        adv_dhcp6_interface_statement_request_options (Union[Unset, str]):
        adv_dhcp6_interface_statement_script (Union[Unset, str]):
        adv_dhcp6_id_assoc_statement_address_enable (Union[Unset, bool]):
        adv_dhcp6_id_assoc_statement_address_id (Union[Unset, str]):
        adv_dhcp6_id_assoc_statement_address (Union[Unset, str]):
        adv_dhcp6_id_assoc_statement_address_pltime (Union[Unset, str]):
        adv_dhcp6_id_assoc_statement_address_vltime (Union[Unset, str]):
        adv_dhcp6_id_assoc_statement_prefix_enable (Union[Unset, bool]):
        adv_dhcp6_id_assoc_statement_prefix_id (Union[Unset, str]):
        adv_dhcp6_id_assoc_statement_prefix (Union[Unset, str]):
        adv_dhcp6_id_assoc_statement_prefix_pltime (Union[Unset, str]):
        adv_dhcp6_id_assoc_statement_prefix_vltime (Union[Unset, str]):
        adv_dhcp6_prefix_interface_statement_sla_id (Union[Unset, str]):
        adv_dhcp6_prefix_interface_statement_sla_len (Union[Unset, str]):
        adv_dhcp6_authentication_statement_authname (Union[Unset, str]):
        adv_dhcp6_authentication_statement_protocol (Union[Unset, str]):
        adv_dhcp6_authentication_statement_algorithm (Union[Unset, str]):
        adv_dhcp6_authentication_statement_rdm (Union[Unset, str]):
        adv_dhcp6_key_info_statement_keyname (Union[Unset, str]):
        adv_dhcp6_key_info_statement_realm (Union[Unset, str]):
        adv_dhcp6_key_info_statement_keyid (Union[Unset, str]):
        adv_dhcp6_key_info_statement_secret (Union[Unset, str]):
        adv_dhcp6_key_info_statement_expire (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    enable: Union[Unset, bool] = UNSET
    blockbogons: Union[Unset, bool] = UNSET
    pseudo: Union[Unset, bool] = UNSET
    blockpriv: Union[Unset, bool] = UNSET
    slaacusev4iface: Union[Unset, bool] = UNSET
    if_: Union[Unset, str] = UNSET
    descr: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    type6: Union[Unset, str] = UNSET
    mtu: Union[Unset, int] = UNSET
    mss: Union[Unset, int] = UNSET
    pcp: Union[Unset, int] = UNSET
    promisc: Union[Unset, bool] = UNSET
    ipaddr: Union[Unset, str] = UNSET
    member: Union[Unset, str] = UNSET
    media: Union[Unset, str] = UNSET
    mac: Union[Unset, str] = UNSET
    mediaopt: Union[Unset, str] = UNSET
    spoofmac: Union[Unset, str] = UNSET
    tag: Union[Unset, int] = UNSET
    gateway: Union[Unset, str] = UNSET
    ipaddrv6: Union[Unset, str] = UNSET
    ipv6usev4iface: Union[Unset, bool] = UNSET
    defaultgw6: Union[Unset, bool] = UNSET
    gatewayip6: Union[Unset, str] = UNSET
    gatewayv6: Union[Unset, str] = UNSET
    gatewaydescr6: Union[Unset, str] = UNSET
    gatewayname6: Union[Unset, str] = UNSET
    alias_address: Union[Unset, str] = UNSET
    dhcphostname: Union[Unset, str] = UNSET
    dhcprejectfrom: Union[Unset, str] = UNSET
    dhcprejectfromarray: Union[Unset, List[str]] = UNSET
    dhcpvlanenable: Union[Unset, bool] = UNSET
    dhcp6usev4iface: Union[Unset, bool] = UNSET
    dhcp6prefixonly: Union[Unset, bool] = UNSET
    dhcp6_ia_pd_send_hint: Union[Unset, bool] = UNSET
    dhcp6debug: Union[Unset, bool] = UNSET
    dhcp6withoutra: Union[Unset, bool] = UNSET
    dhcp6norelease: Union[Unset, bool] = UNSET
    dhcpcvpt: Union[Unset, str] = UNSET
    dhcp6cvpt: Union[Unset, str] = UNSET
    prefix_6rd: Union[Unset, str] = UNSET
    gateway_6rd: Union[Unset, str] = UNSET
    track6_prefix_id_hex: Union[Unset, str] = UNSET
    dhcp6_ia_pd_len: Union[Unset, str] = UNSET
    prefix_6rd_v4plen: Union[Unset, str] = UNSET
    track6_interface: Union[Unset, str] = UNSET
    adv_dhcp_config_advanced: Union[Unset, bool] = UNSET
    adv_dhcp_config_file_override: Union[Unset, bool] = UNSET
    adv_dhcp_pt_timeout: Union[Unset, str] = UNSET
    adv_dhcp_pt_retry: Union[Unset, str] = UNSET
    adv_dhcp_pt_select_timeout: Union[Unset, str] = UNSET
    adv_dhcp_pt_reboot: Union[Unset, str] = UNSET
    adv_dhcp_pt_backoff_cutoff: Union[Unset, str] = UNSET
    adv_dhcp_pt_initial_interval: Union[Unset, str] = UNSET
    adv_dhcp_pt_values: Union[Unset, str] = UNSET
    adv_dhcp_config_file_override_path: Union[Unset, str] = UNSET
    adv_dhcp_send_options: Union[Unset, str] = UNSET
    adv_dhcp_request_options: Union[Unset, str] = UNSET
    adv_dhcp_required_options: Union[Unset, str] = UNSET
    adv_dhcp_option_modifiers: Union[Unset, str] = UNSET
    adv_dhcp6_config_advanced: Union[Unset, bool] = UNSET
    adv_dhcp6_config_file_override: Union[Unset, bool] = UNSET
    adv_dhcp6_prefix_selected_interface: Union[Unset, str] = UNSET
    adv_dhcp6_config_file_override_path: Union[Unset, str] = UNSET
    adv_dhcp6_interface_statement_information_only_enable: Union[Unset, bool] = UNSET
    adv_dhcp6_interface_statement_send_options: Union[Unset, str] = UNSET
    adv_dhcp6_interface_statement_request_options: Union[Unset, str] = UNSET
    adv_dhcp6_interface_statement_script: Union[Unset, str] = UNSET
    adv_dhcp6_id_assoc_statement_address_enable: Union[Unset, bool] = UNSET
    adv_dhcp6_id_assoc_statement_address_id: Union[Unset, str] = UNSET
    adv_dhcp6_id_assoc_statement_address: Union[Unset, str] = UNSET
    adv_dhcp6_id_assoc_statement_address_pltime: Union[Unset, str] = UNSET
    adv_dhcp6_id_assoc_statement_address_vltime: Union[Unset, str] = UNSET
    adv_dhcp6_id_assoc_statement_prefix_enable: Union[Unset, bool] = UNSET
    adv_dhcp6_id_assoc_statement_prefix_id: Union[Unset, str] = UNSET
    adv_dhcp6_id_assoc_statement_prefix: Union[Unset, str] = UNSET
    adv_dhcp6_id_assoc_statement_prefix_pltime: Union[Unset, str] = UNSET
    adv_dhcp6_id_assoc_statement_prefix_vltime: Union[Unset, str] = UNSET
    adv_dhcp6_prefix_interface_statement_sla_id: Union[Unset, str] = UNSET
    adv_dhcp6_prefix_interface_statement_sla_len: Union[Unset, str] = UNSET
    adv_dhcp6_authentication_statement_authname: Union[Unset, str] = UNSET
    adv_dhcp6_authentication_statement_protocol: Union[Unset, str] = UNSET
    adv_dhcp6_authentication_statement_algorithm: Union[Unset, str] = UNSET
    adv_dhcp6_authentication_statement_rdm: Union[Unset, str] = UNSET
    adv_dhcp6_key_info_statement_keyname: Union[Unset, str] = UNSET
    adv_dhcp6_key_info_statement_realm: Union[Unset, str] = UNSET
    adv_dhcp6_key_info_statement_keyid: Union[Unset, str] = UNSET
    adv_dhcp6_key_info_statement_secret: Union[Unset, str] = UNSET
    adv_dhcp6_key_info_statement_expire: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        enable = self.enable

        blockbogons = self.blockbogons

        pseudo = self.pseudo

        blockpriv = self.blockpriv

        slaacusev4iface = self.slaacusev4iface

        if_ = self.if_

        descr = self.descr

        type = self.type

        type6 = self.type6

        mtu = self.mtu

        mss = self.mss

        pcp = self.pcp

        promisc = self.promisc

        ipaddr = self.ipaddr

        member = self.member

        media = self.media

        mac = self.mac

        mediaopt = self.mediaopt

        spoofmac = self.spoofmac

        tag = self.tag

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

        dhcprejectfromarray: Union[Unset, List[str]] = UNSET
        if not isinstance(self.dhcprejectfromarray, Unset):
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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if enable is not UNSET:
            field_dict["enable"] = enable
        if blockbogons is not UNSET:
            field_dict["blockbogons"] = blockbogons
        if pseudo is not UNSET:
            field_dict["pseudo"] = pseudo
        if blockpriv is not UNSET:
            field_dict["blockpriv"] = blockpriv
        if slaacusev4iface is not UNSET:
            field_dict["slaacusev4iface"] = slaacusev4iface
        if if_ is not UNSET:
            field_dict["if"] = if_
        if descr is not UNSET:
            field_dict["descr"] = descr
        if type is not UNSET:
            field_dict["type"] = type
        if type6 is not UNSET:
            field_dict["type6"] = type6
        if mtu is not UNSET:
            field_dict["mtu"] = mtu
        if mss is not UNSET:
            field_dict["mss"] = mss
        if pcp is not UNSET:
            field_dict["pcp"] = pcp
        if promisc is not UNSET:
            field_dict["promisc"] = promisc
        if ipaddr is not UNSET:
            field_dict["ipaddr"] = ipaddr
        if member is not UNSET:
            field_dict["member"] = member
        if media is not UNSET:
            field_dict["media"] = media
        if mac is not UNSET:
            field_dict["mac"] = mac
        if mediaopt is not UNSET:
            field_dict["mediaopt"] = mediaopt
        if spoofmac is not UNSET:
            field_dict["spoofmac"] = spoofmac
        if tag is not UNSET:
            field_dict["tag"] = tag
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if ipaddrv6 is not UNSET:
            field_dict["ipaddrv6"] = ipaddrv6
        if ipv6usev4iface is not UNSET:
            field_dict["ipv6usev4iface"] = ipv6usev4iface
        if defaultgw6 is not UNSET:
            field_dict["defaultgw6"] = defaultgw6
        if gatewayip6 is not UNSET:
            field_dict["gatewayip6"] = gatewayip6
        if gatewayv6 is not UNSET:
            field_dict["gatewayv6"] = gatewayv6
        if gatewaydescr6 is not UNSET:
            field_dict["gatewaydescr6"] = gatewaydescr6
        if gatewayname6 is not UNSET:
            field_dict["gatewayname6"] = gatewayname6
        if alias_address is not UNSET:
            field_dict["alias_address"] = alias_address
        if dhcphostname is not UNSET:
            field_dict["dhcphostname"] = dhcphostname
        if dhcprejectfrom is not UNSET:
            field_dict["dhcprejectfrom"] = dhcprejectfrom
        if dhcprejectfromarray is not UNSET:
            field_dict["dhcprejectfromarray"] = dhcprejectfromarray
        if dhcpvlanenable is not UNSET:
            field_dict["dhcpvlanenable"] = dhcpvlanenable
        if dhcp6usev4iface is not UNSET:
            field_dict["dhcp6usev4iface"] = dhcp6usev4iface
        if dhcp6prefixonly is not UNSET:
            field_dict["dhcp6prefixonly"] = dhcp6prefixonly
        if dhcp6_ia_pd_send_hint is not UNSET:
            field_dict["dhcp6_ia_pd_send_hint"] = dhcp6_ia_pd_send_hint
        if dhcp6debug is not UNSET:
            field_dict["dhcp6debug"] = dhcp6debug
        if dhcp6withoutra is not UNSET:
            field_dict["dhcp6withoutra"] = dhcp6withoutra
        if dhcp6norelease is not UNSET:
            field_dict["dhcp6norelease"] = dhcp6norelease
        if dhcpcvpt is not UNSET:
            field_dict["dhcpcvpt"] = dhcpcvpt
        if dhcp6cvpt is not UNSET:
            field_dict["dhcp6cvpt"] = dhcp6cvpt
        if prefix_6rd is not UNSET:
            field_dict["prefix_6rd"] = prefix_6rd
        if gateway_6rd is not UNSET:
            field_dict["gateway_6rd"] = gateway_6rd
        if track6_prefix_id_hex is not UNSET:
            field_dict["track6_prefix_id__hex"] = track6_prefix_id_hex
        if dhcp6_ia_pd_len is not UNSET:
            field_dict["dhcp6_ia_pd_len"] = dhcp6_ia_pd_len
        if prefix_6rd_v4plen is not UNSET:
            field_dict["prefix_6rd_v4plen"] = prefix_6rd_v4plen
        if track6_interface is not UNSET:
            field_dict["track6_interface"] = track6_interface
        if adv_dhcp_config_advanced is not UNSET:
            field_dict["adv_dhcp_config_advanced"] = adv_dhcp_config_advanced
        if adv_dhcp_config_file_override is not UNSET:
            field_dict["adv_dhcp_config_file_override"] = adv_dhcp_config_file_override
        if adv_dhcp_pt_timeout is not UNSET:
            field_dict["adv_dhcp_pt_timeout"] = adv_dhcp_pt_timeout
        if adv_dhcp_pt_retry is not UNSET:
            field_dict["adv_dhcp_pt_retry"] = adv_dhcp_pt_retry
        if adv_dhcp_pt_select_timeout is not UNSET:
            field_dict["adv_dhcp_pt_select_timeout"] = adv_dhcp_pt_select_timeout
        if adv_dhcp_pt_reboot is not UNSET:
            field_dict["adv_dhcp_pt_reboot"] = adv_dhcp_pt_reboot
        if adv_dhcp_pt_backoff_cutoff is not UNSET:
            field_dict["adv_dhcp_pt_backoff_cutoff"] = adv_dhcp_pt_backoff_cutoff
        if adv_dhcp_pt_initial_interval is not UNSET:
            field_dict["adv_dhcp_pt_initial_interval"] = adv_dhcp_pt_initial_interval
        if adv_dhcp_pt_values is not UNSET:
            field_dict["adv_dhcp_pt_values"] = adv_dhcp_pt_values
        if adv_dhcp_config_file_override_path is not UNSET:
            field_dict["adv_dhcp_config_file_override_path"] = adv_dhcp_config_file_override_path
        if adv_dhcp_send_options is not UNSET:
            field_dict["adv_dhcp_send_options"] = adv_dhcp_send_options
        if adv_dhcp_request_options is not UNSET:
            field_dict["adv_dhcp_request_options"] = adv_dhcp_request_options
        if adv_dhcp_required_options is not UNSET:
            field_dict["adv_dhcp_required_options"] = adv_dhcp_required_options
        if adv_dhcp_option_modifiers is not UNSET:
            field_dict["adv_dhcp_option_modifiers"] = adv_dhcp_option_modifiers
        if adv_dhcp6_config_advanced is not UNSET:
            field_dict["adv_dhcp6_config_advanced"] = adv_dhcp6_config_advanced
        if adv_dhcp6_config_file_override is not UNSET:
            field_dict["adv_dhcp6_config_file_override"] = adv_dhcp6_config_file_override
        if adv_dhcp6_prefix_selected_interface is not UNSET:
            field_dict["adv_dhcp6_prefix_selected_interface"] = adv_dhcp6_prefix_selected_interface
        if adv_dhcp6_config_file_override_path is not UNSET:
            field_dict["adv_dhcp6_config_file_override_path"] = adv_dhcp6_config_file_override_path
        if adv_dhcp6_interface_statement_information_only_enable is not UNSET:
            field_dict["adv_dhcp6_interface_statement_information_only_enable"] = (
                adv_dhcp6_interface_statement_information_only_enable
            )
        if adv_dhcp6_interface_statement_send_options is not UNSET:
            field_dict["adv_dhcp6_interface_statement_send_options"] = adv_dhcp6_interface_statement_send_options
        if adv_dhcp6_interface_statement_request_options is not UNSET:
            field_dict["adv_dhcp6_interface_statement_request_options"] = adv_dhcp6_interface_statement_request_options
        if adv_dhcp6_interface_statement_script is not UNSET:
            field_dict["adv_dhcp6_interface_statement_script"] = adv_dhcp6_interface_statement_script
        if adv_dhcp6_id_assoc_statement_address_enable is not UNSET:
            field_dict["adv_dhcp6_id_assoc_statement_address_enable"] = adv_dhcp6_id_assoc_statement_address_enable
        if adv_dhcp6_id_assoc_statement_address_id is not UNSET:
            field_dict["adv_dhcp6_id_assoc_statement_address_id"] = adv_dhcp6_id_assoc_statement_address_id
        if adv_dhcp6_id_assoc_statement_address is not UNSET:
            field_dict["adv_dhcp6_id_assoc_statement_address"] = adv_dhcp6_id_assoc_statement_address
        if adv_dhcp6_id_assoc_statement_address_pltime is not UNSET:
            field_dict["adv_dhcp6_id_assoc_statement_address_pltime"] = adv_dhcp6_id_assoc_statement_address_pltime
        if adv_dhcp6_id_assoc_statement_address_vltime is not UNSET:
            field_dict["adv_dhcp6_id_assoc_statement_address_vltime"] = adv_dhcp6_id_assoc_statement_address_vltime
        if adv_dhcp6_id_assoc_statement_prefix_enable is not UNSET:
            field_dict["adv_dhcp6_id_assoc_statement_prefix_enable"] = adv_dhcp6_id_assoc_statement_prefix_enable
        if adv_dhcp6_id_assoc_statement_prefix_id is not UNSET:
            field_dict["adv_dhcp6_id_assoc_statement_prefix_id"] = adv_dhcp6_id_assoc_statement_prefix_id
        if adv_dhcp6_id_assoc_statement_prefix is not UNSET:
            field_dict["adv_dhcp6_id_assoc_statement_prefix"] = adv_dhcp6_id_assoc_statement_prefix
        if adv_dhcp6_id_assoc_statement_prefix_pltime is not UNSET:
            field_dict["adv_dhcp6_id_assoc_statement_prefix_pltime"] = adv_dhcp6_id_assoc_statement_prefix_pltime
        if adv_dhcp6_id_assoc_statement_prefix_vltime is not UNSET:
            field_dict["adv_dhcp6_id_assoc_statement_prefix_vltime"] = adv_dhcp6_id_assoc_statement_prefix_vltime
        if adv_dhcp6_prefix_interface_statement_sla_id is not UNSET:
            field_dict["adv_dhcp6_prefix_interface_statement_sla_id"] = adv_dhcp6_prefix_interface_statement_sla_id
        if adv_dhcp6_prefix_interface_statement_sla_len is not UNSET:
            field_dict["adv_dhcp6_prefix_interface_statement_sla_len"] = adv_dhcp6_prefix_interface_statement_sla_len
        if adv_dhcp6_authentication_statement_authname is not UNSET:
            field_dict["adv_dhcp6_authentication_statement_authname"] = adv_dhcp6_authentication_statement_authname
        if adv_dhcp6_authentication_statement_protocol is not UNSET:
            field_dict["adv_dhcp6_authentication_statement_protocol"] = adv_dhcp6_authentication_statement_protocol
        if adv_dhcp6_authentication_statement_algorithm is not UNSET:
            field_dict["adv_dhcp6_authentication_statement_algorithm"] = adv_dhcp6_authentication_statement_algorithm
        if adv_dhcp6_authentication_statement_rdm is not UNSET:
            field_dict["adv_dhcp6_authentication_statement_rdm"] = adv_dhcp6_authentication_statement_rdm
        if adv_dhcp6_key_info_statement_keyname is not UNSET:
            field_dict["adv_dhcp6_key_info_statement_keyname"] = adv_dhcp6_key_info_statement_keyname
        if adv_dhcp6_key_info_statement_realm is not UNSET:
            field_dict["adv_dhcp6_key_info_statement_realm"] = adv_dhcp6_key_info_statement_realm
        if adv_dhcp6_key_info_statement_keyid is not UNSET:
            field_dict["adv_dhcp6_key_info_statement_keyid"] = adv_dhcp6_key_info_statement_keyid
        if adv_dhcp6_key_info_statement_secret is not UNSET:
            field_dict["adv_dhcp6_key_info_statement_secret"] = adv_dhcp6_key_info_statement_secret
        if adv_dhcp6_key_info_statement_expire is not UNSET:
            field_dict["adv_dhcp6_key_info_statement_expire"] = adv_dhcp6_key_info_statement_expire

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        enable = d.pop("enable", UNSET)

        blockbogons = d.pop("blockbogons", UNSET)

        pseudo = d.pop("pseudo", UNSET)

        blockpriv = d.pop("blockpriv", UNSET)

        slaacusev4iface = d.pop("slaacusev4iface", UNSET)

        if_ = d.pop("if", UNSET)

        descr = d.pop("descr", UNSET)

        type = d.pop("type", UNSET)

        type6 = d.pop("type6", UNSET)

        mtu = d.pop("mtu", UNSET)

        mss = d.pop("mss", UNSET)

        pcp = d.pop("pcp", UNSET)

        promisc = d.pop("promisc", UNSET)

        ipaddr = d.pop("ipaddr", UNSET)

        member = d.pop("member", UNSET)

        media = d.pop("media", UNSET)

        mac = d.pop("mac", UNSET)

        mediaopt = d.pop("mediaopt", UNSET)

        spoofmac = d.pop("spoofmac", UNSET)

        tag = d.pop("tag", UNSET)

        gateway = d.pop("gateway", UNSET)

        ipaddrv6 = d.pop("ipaddrv6", UNSET)

        ipv6usev4iface = d.pop("ipv6usev4iface", UNSET)

        defaultgw6 = d.pop("defaultgw6", UNSET)

        gatewayip6 = d.pop("gatewayip6", UNSET)

        gatewayv6 = d.pop("gatewayv6", UNSET)

        gatewaydescr6 = d.pop("gatewaydescr6", UNSET)

        gatewayname6 = d.pop("gatewayname6", UNSET)

        alias_address = d.pop("alias_address", UNSET)

        dhcphostname = d.pop("dhcphostname", UNSET)

        dhcprejectfrom = d.pop("dhcprejectfrom", UNSET)

        dhcprejectfromarray = cast(List[str], d.pop("dhcprejectfromarray", UNSET))

        dhcpvlanenable = d.pop("dhcpvlanenable", UNSET)

        dhcp6usev4iface = d.pop("dhcp6usev4iface", UNSET)

        dhcp6prefixonly = d.pop("dhcp6prefixonly", UNSET)

        dhcp6_ia_pd_send_hint = d.pop("dhcp6_ia_pd_send_hint", UNSET)

        dhcp6debug = d.pop("dhcp6debug", UNSET)

        dhcp6withoutra = d.pop("dhcp6withoutra", UNSET)

        dhcp6norelease = d.pop("dhcp6norelease", UNSET)

        dhcpcvpt = d.pop("dhcpcvpt", UNSET)

        dhcp6cvpt = d.pop("dhcp6cvpt", UNSET)

        prefix_6rd = d.pop("prefix_6rd", UNSET)

        gateway_6rd = d.pop("gateway_6rd", UNSET)

        track6_prefix_id_hex = d.pop("track6_prefix_id__hex", UNSET)

        dhcp6_ia_pd_len = d.pop("dhcp6_ia_pd_len", UNSET)

        prefix_6rd_v4plen = d.pop("prefix_6rd_v4plen", UNSET)

        track6_interface = d.pop("track6_interface", UNSET)

        adv_dhcp_config_advanced = d.pop("adv_dhcp_config_advanced", UNSET)

        adv_dhcp_config_file_override = d.pop("adv_dhcp_config_file_override", UNSET)

        adv_dhcp_pt_timeout = d.pop("adv_dhcp_pt_timeout", UNSET)

        adv_dhcp_pt_retry = d.pop("adv_dhcp_pt_retry", UNSET)

        adv_dhcp_pt_select_timeout = d.pop("adv_dhcp_pt_select_timeout", UNSET)

        adv_dhcp_pt_reboot = d.pop("adv_dhcp_pt_reboot", UNSET)

        adv_dhcp_pt_backoff_cutoff = d.pop("adv_dhcp_pt_backoff_cutoff", UNSET)

        adv_dhcp_pt_initial_interval = d.pop("adv_dhcp_pt_initial_interval", UNSET)

        adv_dhcp_pt_values = d.pop("adv_dhcp_pt_values", UNSET)

        adv_dhcp_config_file_override_path = d.pop("adv_dhcp_config_file_override_path", UNSET)

        adv_dhcp_send_options = d.pop("adv_dhcp_send_options", UNSET)

        adv_dhcp_request_options = d.pop("adv_dhcp_request_options", UNSET)

        adv_dhcp_required_options = d.pop("adv_dhcp_required_options", UNSET)

        adv_dhcp_option_modifiers = d.pop("adv_dhcp_option_modifiers", UNSET)

        adv_dhcp6_config_advanced = d.pop("adv_dhcp6_config_advanced", UNSET)

        adv_dhcp6_config_file_override = d.pop("adv_dhcp6_config_file_override", UNSET)

        adv_dhcp6_prefix_selected_interface = d.pop("adv_dhcp6_prefix_selected_interface", UNSET)

        adv_dhcp6_config_file_override_path = d.pop("adv_dhcp6_config_file_override_path", UNSET)

        adv_dhcp6_interface_statement_information_only_enable = d.pop(
            "adv_dhcp6_interface_statement_information_only_enable", UNSET
        )

        adv_dhcp6_interface_statement_send_options = d.pop("adv_dhcp6_interface_statement_send_options", UNSET)

        adv_dhcp6_interface_statement_request_options = d.pop("adv_dhcp6_interface_statement_request_options", UNSET)

        adv_dhcp6_interface_statement_script = d.pop("adv_dhcp6_interface_statement_script", UNSET)

        adv_dhcp6_id_assoc_statement_address_enable = d.pop("adv_dhcp6_id_assoc_statement_address_enable", UNSET)

        adv_dhcp6_id_assoc_statement_address_id = d.pop("adv_dhcp6_id_assoc_statement_address_id", UNSET)

        adv_dhcp6_id_assoc_statement_address = d.pop("adv_dhcp6_id_assoc_statement_address", UNSET)

        adv_dhcp6_id_assoc_statement_address_pltime = d.pop("adv_dhcp6_id_assoc_statement_address_pltime", UNSET)

        adv_dhcp6_id_assoc_statement_address_vltime = d.pop("adv_dhcp6_id_assoc_statement_address_vltime", UNSET)

        adv_dhcp6_id_assoc_statement_prefix_enable = d.pop("adv_dhcp6_id_assoc_statement_prefix_enable", UNSET)

        adv_dhcp6_id_assoc_statement_prefix_id = d.pop("adv_dhcp6_id_assoc_statement_prefix_id", UNSET)

        adv_dhcp6_id_assoc_statement_prefix = d.pop("adv_dhcp6_id_assoc_statement_prefix", UNSET)

        adv_dhcp6_id_assoc_statement_prefix_pltime = d.pop("adv_dhcp6_id_assoc_statement_prefix_pltime", UNSET)

        adv_dhcp6_id_assoc_statement_prefix_vltime = d.pop("adv_dhcp6_id_assoc_statement_prefix_vltime", UNSET)

        adv_dhcp6_prefix_interface_statement_sla_id = d.pop("adv_dhcp6_prefix_interface_statement_sla_id", UNSET)

        adv_dhcp6_prefix_interface_statement_sla_len = d.pop("adv_dhcp6_prefix_interface_statement_sla_len", UNSET)

        adv_dhcp6_authentication_statement_authname = d.pop("adv_dhcp6_authentication_statement_authname", UNSET)

        adv_dhcp6_authentication_statement_protocol = d.pop("adv_dhcp6_authentication_statement_protocol", UNSET)

        adv_dhcp6_authentication_statement_algorithm = d.pop("adv_dhcp6_authentication_statement_algorithm", UNSET)

        adv_dhcp6_authentication_statement_rdm = d.pop("adv_dhcp6_authentication_statement_rdm", UNSET)

        adv_dhcp6_key_info_statement_keyname = d.pop("adv_dhcp6_key_info_statement_keyname", UNSET)

        adv_dhcp6_key_info_statement_realm = d.pop("adv_dhcp6_key_info_statement_realm", UNSET)

        adv_dhcp6_key_info_statement_keyid = d.pop("adv_dhcp6_key_info_statement_keyid", UNSET)

        adv_dhcp6_key_info_statement_secret = d.pop("adv_dhcp6_key_info_statement_secret", UNSET)

        adv_dhcp6_key_info_statement_expire = d.pop("adv_dhcp6_key_info_statement_expire", UNSET)

        interface = cls(
            name=name,
            enable=enable,
            blockbogons=blockbogons,
            pseudo=pseudo,
            blockpriv=blockpriv,
            slaacusev4iface=slaacusev4iface,
            if_=if_,
            descr=descr,
            type=type,
            type6=type6,
            mtu=mtu,
            mss=mss,
            pcp=pcp,
            promisc=promisc,
            ipaddr=ipaddr,
            member=member,
            media=media,
            mac=mac,
            mediaopt=mediaopt,
            spoofmac=spoofmac,
            tag=tag,
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
