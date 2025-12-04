from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Interface")


@_attrs_define
class Interface:
    """Detailed interface information

    Attributes:
        name (str | Unset): alias to assigned name
        if_ (str | Unset): alias to device_name
        assigned_name (str | Unset): user assigned name, e.g. MYLAN
        device_name (str | Unset): host device name, e.g. ix1
        identity (str | Unset): unique identity of device, e.g. opt1
        enable (bool | Unset):
        blockbogons (bool | Unset):
        pseudo (bool | Unset):
        blockpriv (bool | Unset):
        slaacusev4iface (bool | Unset):
        descr (str | Unset):
        type_ (str | Unset):
        type6 (str | Unset):
        mtu (int | Unset):
        mss (int | Unset):
        pcp (int | Unset):
        promisc (bool | Unset):
        ipaddr (str | Unset):
        member (str | Unset):
        media (str | Unset):
        mac (str | Unset):
        mediaopt (str | Unset):
        spoofmac (str | Unset):
        tag (int | Unset):
        gateway (str | Unset):
        ipaddrv6 (str | Unset):
        ipv6usev4iface (bool | Unset):
        gatewayv6 (str | Unset):
        alias_address (str | Unset):
        dhcphostname (str | Unset):
        dhcprejectfrom (str | Unset):
        dhcprejectfromarray (list[str] | Unset):
        dhcpvlanenable (bool | Unset):
        dhcp6usev4iface (bool | Unset):
        dhcp6prefixonly (bool | Unset):
        dhcp6_ia_pd_send_hint (bool | Unset):
        dhcp6debug (bool | Unset):
        dhcp6withoutra (bool | Unset):
        dhcp6norelease (bool | Unset):
        dhcpcvpt (str | Unset):
        dhcp6cvpt (str | Unset):
        prefix_6rd (str | Unset):
        gateway_6rd (str | Unset):
        dhcp6_ia_pd_len (str | Unset):
        prefix_6rd_v4plen (str | Unset):
        track6_interface (str | Unset):
        track6_prefix_id (str | Unset):
        adv_dhcp_config_advanced (bool | Unset):
        adv_dhcp_config_file_override (bool | Unset):
        adv_dhcp_pt_timeout (str | Unset):
        adv_dhcp_pt_retry (str | Unset):
        adv_dhcp_pt_select_timeout (str | Unset):
        adv_dhcp_pt_reboot (str | Unset):
        adv_dhcp_pt_backoff_cutoff (str | Unset):
        adv_dhcp_pt_initial_interval (str | Unset):
        adv_dhcp_pt_values (str | Unset):
        adv_dhcp_config_file_override_path (str | Unset):
        adv_dhcp_send_options (str | Unset):
        adv_dhcp_request_options (str | Unset):
        adv_dhcp_required_options (str | Unset):
        adv_dhcp_option_modifiers (str | Unset):
        adv_dhcp6_config_advanced (bool | Unset):
        adv_dhcp6_config_file_override (bool | Unset):
        adv_dhcp6_prefix_selected_interface (str | Unset):
        adv_dhcp6_config_file_override_path (str | Unset):
        adv_dhcp6_interface_statement_information_only_enable (bool | Unset):
        adv_dhcp6_interface_statement_send_options (str | Unset):
        adv_dhcp6_interface_statement_request_options (str | Unset):
        adv_dhcp6_interface_statement_script (str | Unset):
        adv_dhcp6_id_assoc_statement_address_enable (bool | Unset):
        adv_dhcp6_id_assoc_statement_address_id (str | Unset):
        adv_dhcp6_id_assoc_statement_address (str | Unset):
        adv_dhcp6_id_assoc_statement_address_pltime (str | Unset):
        adv_dhcp6_id_assoc_statement_address_vltime (str | Unset):
        adv_dhcp6_id_assoc_statement_prefix_enable (bool | Unset):
        adv_dhcp6_id_assoc_statement_prefix_id (str | Unset):
        adv_dhcp6_id_assoc_statement_prefix (str | Unset):
        adv_dhcp6_id_assoc_statement_prefix_pltime (str | Unset):
        adv_dhcp6_id_assoc_statement_prefix_vltime (str | Unset):
        adv_dhcp6_prefix_interface_statement_sla_id (str | Unset):
        adv_dhcp6_prefix_interface_statement_sla_len (str | Unset):
        adv_dhcp6_authentication_statement_authname (str | Unset):
        adv_dhcp6_authentication_statement_protocol (str | Unset):
        adv_dhcp6_authentication_statement_algorithm (str | Unset):
        adv_dhcp6_authentication_statement_rdm (str | Unset):
        adv_dhcp6_key_info_statement_keyname (str | Unset):
        adv_dhcp6_key_info_statement_realm (str | Unset):
        adv_dhcp6_key_info_statement_keyid (str | Unset):
        adv_dhcp6_key_info_statement_secret (str | Unset):
        adv_dhcp6_key_info_statement_expire (str | Unset):
    """

    name: str | Unset = UNSET
    if_: str | Unset = UNSET
    assigned_name: str | Unset = UNSET
    device_name: str | Unset = UNSET
    identity: str | Unset = UNSET
    enable: bool | Unset = UNSET
    blockbogons: bool | Unset = UNSET
    pseudo: bool | Unset = UNSET
    blockpriv: bool | Unset = UNSET
    slaacusev4iface: bool | Unset = UNSET
    descr: str | Unset = UNSET
    type_: str | Unset = UNSET
    type6: str | Unset = UNSET
    mtu: int | Unset = UNSET
    mss: int | Unset = UNSET
    pcp: int | Unset = UNSET
    promisc: bool | Unset = UNSET
    ipaddr: str | Unset = UNSET
    member: str | Unset = UNSET
    media: str | Unset = UNSET
    mac: str | Unset = UNSET
    mediaopt: str | Unset = UNSET
    spoofmac: str | Unset = UNSET
    tag: int | Unset = UNSET
    gateway: str | Unset = UNSET
    ipaddrv6: str | Unset = UNSET
    ipv6usev4iface: bool | Unset = UNSET
    gatewayv6: str | Unset = UNSET
    alias_address: str | Unset = UNSET
    dhcphostname: str | Unset = UNSET
    dhcprejectfrom: str | Unset = UNSET
    dhcprejectfromarray: list[str] | Unset = UNSET
    dhcpvlanenable: bool | Unset = UNSET
    dhcp6usev4iface: bool | Unset = UNSET
    dhcp6prefixonly: bool | Unset = UNSET
    dhcp6_ia_pd_send_hint: bool | Unset = UNSET
    dhcp6debug: bool | Unset = UNSET
    dhcp6withoutra: bool | Unset = UNSET
    dhcp6norelease: bool | Unset = UNSET
    dhcpcvpt: str | Unset = UNSET
    dhcp6cvpt: str | Unset = UNSET
    prefix_6rd: str | Unset = UNSET
    gateway_6rd: str | Unset = UNSET
    dhcp6_ia_pd_len: str | Unset = UNSET
    prefix_6rd_v4plen: str | Unset = UNSET
    track6_interface: str | Unset = UNSET
    track6_prefix_id: str | Unset = UNSET
    adv_dhcp_config_advanced: bool | Unset = UNSET
    adv_dhcp_config_file_override: bool | Unset = UNSET
    adv_dhcp_pt_timeout: str | Unset = UNSET
    adv_dhcp_pt_retry: str | Unset = UNSET
    adv_dhcp_pt_select_timeout: str | Unset = UNSET
    adv_dhcp_pt_reboot: str | Unset = UNSET
    adv_dhcp_pt_backoff_cutoff: str | Unset = UNSET
    adv_dhcp_pt_initial_interval: str | Unset = UNSET
    adv_dhcp_pt_values: str | Unset = UNSET
    adv_dhcp_config_file_override_path: str | Unset = UNSET
    adv_dhcp_send_options: str | Unset = UNSET
    adv_dhcp_request_options: str | Unset = UNSET
    adv_dhcp_required_options: str | Unset = UNSET
    adv_dhcp_option_modifiers: str | Unset = UNSET
    adv_dhcp6_config_advanced: bool | Unset = UNSET
    adv_dhcp6_config_file_override: bool | Unset = UNSET
    adv_dhcp6_prefix_selected_interface: str | Unset = UNSET
    adv_dhcp6_config_file_override_path: str | Unset = UNSET
    adv_dhcp6_interface_statement_information_only_enable: bool | Unset = UNSET
    adv_dhcp6_interface_statement_send_options: str | Unset = UNSET
    adv_dhcp6_interface_statement_request_options: str | Unset = UNSET
    adv_dhcp6_interface_statement_script: str | Unset = UNSET
    adv_dhcp6_id_assoc_statement_address_enable: bool | Unset = UNSET
    adv_dhcp6_id_assoc_statement_address_id: str | Unset = UNSET
    adv_dhcp6_id_assoc_statement_address: str | Unset = UNSET
    adv_dhcp6_id_assoc_statement_address_pltime: str | Unset = UNSET
    adv_dhcp6_id_assoc_statement_address_vltime: str | Unset = UNSET
    adv_dhcp6_id_assoc_statement_prefix_enable: bool | Unset = UNSET
    adv_dhcp6_id_assoc_statement_prefix_id: str | Unset = UNSET
    adv_dhcp6_id_assoc_statement_prefix: str | Unset = UNSET
    adv_dhcp6_id_assoc_statement_prefix_pltime: str | Unset = UNSET
    adv_dhcp6_id_assoc_statement_prefix_vltime: str | Unset = UNSET
    adv_dhcp6_prefix_interface_statement_sla_id: str | Unset = UNSET
    adv_dhcp6_prefix_interface_statement_sla_len: str | Unset = UNSET
    adv_dhcp6_authentication_statement_authname: str | Unset = UNSET
    adv_dhcp6_authentication_statement_protocol: str | Unset = UNSET
    adv_dhcp6_authentication_statement_algorithm: str | Unset = UNSET
    adv_dhcp6_authentication_statement_rdm: str | Unset = UNSET
    adv_dhcp6_key_info_statement_keyname: str | Unset = UNSET
    adv_dhcp6_key_info_statement_realm: str | Unset = UNSET
    adv_dhcp6_key_info_statement_keyid: str | Unset = UNSET
    adv_dhcp6_key_info_statement_secret: str | Unset = UNSET
    adv_dhcp6_key_info_statement_expire: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        type_ = self.type_

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

        gatewayv6 = self.gatewayv6

        alias_address = self.alias_address

        dhcphostname = self.dhcphostname

        dhcprejectfrom = self.dhcprejectfrom

        dhcprejectfromarray: list[str] | Unset = UNSET
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

        dhcp6_ia_pd_len = self.dhcp6_ia_pd_len

        prefix_6rd_v4plen = self.prefix_6rd_v4plen

        track6_interface = self.track6_interface

        track6_prefix_id = self.track6_prefix_id

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if if_ is not UNSET:
            field_dict["if"] = if_
        if assigned_name is not UNSET:
            field_dict["assigned_name"] = assigned_name
        if device_name is not UNSET:
            field_dict["device_name"] = device_name
        if identity is not UNSET:
            field_dict["identity"] = identity
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
        if descr is not UNSET:
            field_dict["descr"] = descr
        if type_ is not UNSET:
            field_dict["type"] = type_
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
        if gatewayv6 is not UNSET:
            field_dict["gatewayv6"] = gatewayv6
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
        if dhcp6_ia_pd_len is not UNSET:
            field_dict["dhcp6_ia_pd_len"] = dhcp6_ia_pd_len
        if prefix_6rd_v4plen is not UNSET:
            field_dict["prefix_6rd_v4plen"] = prefix_6rd_v4plen
        if track6_interface is not UNSET:
            field_dict["track6_interface"] = track6_interface
        if track6_prefix_id is not UNSET:
            field_dict["track6_prefix_id"] = track6_prefix_id
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
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        if_ = d.pop("if", UNSET)

        assigned_name = d.pop("assigned_name", UNSET)

        device_name = d.pop("device_name", UNSET)

        identity = d.pop("identity", UNSET)

        enable = d.pop("enable", UNSET)

        blockbogons = d.pop("blockbogons", UNSET)

        pseudo = d.pop("pseudo", UNSET)

        blockpriv = d.pop("blockpriv", UNSET)

        slaacusev4iface = d.pop("slaacusev4iface", UNSET)

        descr = d.pop("descr", UNSET)

        type_ = d.pop("type", UNSET)

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

        gatewayv6 = d.pop("gatewayv6", UNSET)

        alias_address = d.pop("alias_address", UNSET)

        dhcphostname = d.pop("dhcphostname", UNSET)

        dhcprejectfrom = d.pop("dhcprejectfrom", UNSET)

        dhcprejectfromarray = cast(list[str], d.pop("dhcprejectfromarray", UNSET))

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

        dhcp6_ia_pd_len = d.pop("dhcp6_ia_pd_len", UNSET)

        prefix_6rd_v4plen = d.pop("prefix_6rd_v4plen", UNSET)

        track6_interface = d.pop("track6_interface", UNSET)

        track6_prefix_id = d.pop("track6_prefix_id", UNSET)

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
            type_=type_,
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
            gatewayv6=gatewayv6,
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
            dhcp6_ia_pd_len=dhcp6_ia_pd_len,
            prefix_6rd_v4plen=prefix_6rd_v4plen,
            track6_interface=track6_interface,
            track6_prefix_id=track6_prefix_id,
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
