from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ntopng_localnet import NtopngLocalnet
    from ..models.text_value import TextValue


T = TypeVar("T", bound="Ntopng")


@_attrs_define
class Ntopng:
    """
    Attributes:
        enable (bool | Unset): Enable ntopng

            Check this to enable ntopng.
        keepdata (bool | Unset): Keep Data/Settings
            Note: If disabled, all settings and data will be wiped on package uninstall/reinstall/upgrade!

            Keep ntopng settings, graphs and traffic data.
        redis_password (str | Unset): ntopng Admin Password

            Enter the password for the ntopng admin user. Minimum 5 characters.
        redis_passwordagain (str | Unset): Confirm ntopng Admin Password
        server_interface (str | Unset): (HTTP(S) Server Options) Server Interface

            Interface for the ntopng http(s) server to listen on.
        server_ipv4 (bool | Unset): (HTTP(S) Server Options) Server IPv4

            Enable listening on IPv4. Note that ntopng currently allows IPv4 or IPv6, but not both.
        server_ipv6 (bool | Unset): (HTTP(S) Server Options) Server IPv6

            Enable listening on IPv6. This setting is currently ignored if IPv4 is enabled.
        interface_array (list[str] | Unset):
        promiscuous (bool | Unset): (Monitoring Options) Promiscuous Mode

            Enable promiscuous mode on all monitored interfaces.
        dns_mode (str | Unset): (Monitoring Options) DNS Mode (0, 1, 2, 3)

            Configures how name resolution is handled.
        local_nets (list[NtopngLocalnet] | Unset):
        custom_config (str | Unset): (Advanced configuration) Additional configuration for ntopng.conf

            Additional configuration lines to be added directly to the ntopng configuration file.
            Each option must be on a separate line and in the form of `--key=value`
            See https://www.ntop.org/guides/ntopng/cli_options/cli_options_example.html "Configruation File Example" in the
            ntopng guide for configuration file syntax.
            See https://www.ntop.org/guides/ntopng/cli_options/cli_options.html "Command Line Options" in the guide for all
            available options.
        maxmind_account (str | Unset): (Geolocation support) GeoLite2 Account ID
        maxmind_key (str | Unset): (Geolocation support) GeoLite2 License Key

            GeoLite2 provides location information about IP addresses.
            To utilize the free MaxMind GeoLite2 GeoIP functionality, you must register for a free MaxMind user account
        delete_data (bool | Unset): Delete ntopng traffic data and alerts (useful if you are running out of disk space).
        reset_ntopng (bool | Unset): Delete all ntopng data and perform a complete reset of ntopng configuration.
        update_geodb (bool | Unset): Update the Geolocation database from the maxmind account
        server_interface_options (list[TextValue] | Unset):
        interface_array_options (list[TextValue] | Unset):
    """

    enable: bool | Unset = UNSET
    keepdata: bool | Unset = UNSET
    redis_password: str | Unset = UNSET
    redis_passwordagain: str | Unset = UNSET
    server_interface: str | Unset = UNSET
    server_ipv4: bool | Unset = UNSET
    server_ipv6: bool | Unset = UNSET
    interface_array: list[str] | Unset = UNSET
    promiscuous: bool | Unset = UNSET
    dns_mode: str | Unset = UNSET
    local_nets: list[NtopngLocalnet] | Unset = UNSET
    custom_config: str | Unset = UNSET
    maxmind_account: str | Unset = UNSET
    maxmind_key: str | Unset = UNSET
    delete_data: bool | Unset = UNSET
    reset_ntopng: bool | Unset = UNSET
    update_geodb: bool | Unset = UNSET
    server_interface_options: list[TextValue] | Unset = UNSET
    interface_array_options: list[TextValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        keepdata = self.keepdata

        redis_password = self.redis_password

        redis_passwordagain = self.redis_passwordagain

        server_interface = self.server_interface

        server_ipv4 = self.server_ipv4

        server_ipv6 = self.server_ipv6

        interface_array: list[str] | Unset = UNSET
        if not isinstance(self.interface_array, Unset):
            interface_array = self.interface_array

        promiscuous = self.promiscuous

        dns_mode = self.dns_mode

        local_nets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.local_nets, Unset):
            local_nets = []
            for local_nets_item_data in self.local_nets:
                local_nets_item = local_nets_item_data.to_dict()
                local_nets.append(local_nets_item)

        custom_config = self.custom_config

        maxmind_account = self.maxmind_account

        maxmind_key = self.maxmind_key

        delete_data = self.delete_data

        reset_ntopng = self.reset_ntopng

        update_geodb = self.update_geodb

        server_interface_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.server_interface_options, Unset):
            server_interface_options = []
            for server_interface_options_item_data in self.server_interface_options:
                server_interface_options_item = server_interface_options_item_data.to_dict()
                server_interface_options.append(server_interface_options_item)

        interface_array_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.interface_array_options, Unset):
            interface_array_options = []
            for interface_array_options_item_data in self.interface_array_options:
                interface_array_options_item = interface_array_options_item_data.to_dict()
                interface_array_options.append(interface_array_options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if keepdata is not UNSET:
            field_dict["keepdata"] = keepdata
        if redis_password is not UNSET:
            field_dict["redis_password"] = redis_password
        if redis_passwordagain is not UNSET:
            field_dict["redis_passwordagain"] = redis_passwordagain
        if server_interface is not UNSET:
            field_dict["server_interface"] = server_interface
        if server_ipv4 is not UNSET:
            field_dict["server_ipv4"] = server_ipv4
        if server_ipv6 is not UNSET:
            field_dict["server_ipv6"] = server_ipv6
        if interface_array is not UNSET:
            field_dict["interface_array"] = interface_array
        if promiscuous is not UNSET:
            field_dict["promiscuous"] = promiscuous
        if dns_mode is not UNSET:
            field_dict["dns_mode"] = dns_mode
        if local_nets is not UNSET:
            field_dict["local_nets"] = local_nets
        if custom_config is not UNSET:
            field_dict["custom_config"] = custom_config
        if maxmind_account is not UNSET:
            field_dict["maxmind_account"] = maxmind_account
        if maxmind_key is not UNSET:
            field_dict["maxmind_key"] = maxmind_key
        if delete_data is not UNSET:
            field_dict["delete_data"] = delete_data
        if reset_ntopng is not UNSET:
            field_dict["reset_ntopng"] = reset_ntopng
        if update_geodb is not UNSET:
            field_dict["update_geodb"] = update_geodb
        if server_interface_options is not UNSET:
            field_dict["server_interface_options"] = server_interface_options
        if interface_array_options is not UNSET:
            field_dict["interface_array_options"] = interface_array_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ntopng_localnet import NtopngLocalnet
        from ..models.text_value import TextValue

        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        keepdata = d.pop("keepdata", UNSET)

        redis_password = d.pop("redis_password", UNSET)

        redis_passwordagain = d.pop("redis_passwordagain", UNSET)

        server_interface = d.pop("server_interface", UNSET)

        server_ipv4 = d.pop("server_ipv4", UNSET)

        server_ipv6 = d.pop("server_ipv6", UNSET)

        interface_array = cast(list[str], d.pop("interface_array", UNSET))

        promiscuous = d.pop("promiscuous", UNSET)

        dns_mode = d.pop("dns_mode", UNSET)

        _local_nets = d.pop("local_nets", UNSET)
        local_nets: list[NtopngLocalnet] | Unset = UNSET
        if _local_nets is not UNSET:
            local_nets = []
            for local_nets_item_data in _local_nets:
                local_nets_item = NtopngLocalnet.from_dict(local_nets_item_data)

                local_nets.append(local_nets_item)

        custom_config = d.pop("custom_config", UNSET)

        maxmind_account = d.pop("maxmind_account", UNSET)

        maxmind_key = d.pop("maxmind_key", UNSET)

        delete_data = d.pop("delete_data", UNSET)

        reset_ntopng = d.pop("reset_ntopng", UNSET)

        update_geodb = d.pop("update_geodb", UNSET)

        _server_interface_options = d.pop("server_interface_options", UNSET)
        server_interface_options: list[TextValue] | Unset = UNSET
        if _server_interface_options is not UNSET:
            server_interface_options = []
            for server_interface_options_item_data in _server_interface_options:
                server_interface_options_item = TextValue.from_dict(server_interface_options_item_data)

                server_interface_options.append(server_interface_options_item)

        _interface_array_options = d.pop("interface_array_options", UNSET)
        interface_array_options: list[TextValue] | Unset = UNSET
        if _interface_array_options is not UNSET:
            interface_array_options = []
            for interface_array_options_item_data in _interface_array_options:
                interface_array_options_item = TextValue.from_dict(interface_array_options_item_data)

                interface_array_options.append(interface_array_options_item)

        ntopng = cls(
            enable=enable,
            keepdata=keepdata,
            redis_password=redis_password,
            redis_passwordagain=redis_passwordagain,
            server_interface=server_interface,
            server_ipv4=server_ipv4,
            server_ipv6=server_ipv6,
            interface_array=interface_array,
            promiscuous=promiscuous,
            dns_mode=dns_mode,
            local_nets=local_nets,
            custom_config=custom_config,
            maxmind_account=maxmind_account,
            maxmind_key=maxmind_key,
            delete_data=delete_data,
            reset_ntopng=reset_ntopng,
            update_geodb=update_geodb,
            server_interface_options=server_interface_options,
            interface_array_options=interface_array_options,
        )

        ntopng.additional_properties = d
        return ntopng

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
