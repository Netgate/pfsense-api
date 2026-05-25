from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_value import TextValue


T = TypeVar("T", bound="Pimd")


@_attrs_define
class Pimd:
    """
    Attributes:
        enable (bool | Unset): (Service Control) Enable
        interfacemode (str | Unset): (Service Control) Default Bind (none, all)

            Default interface binding behavior. Per-interface behavior can be set on the Interfaces tab.
        loglevel (str | Unset): (Service Control) Log Level (none, error, warning, notice, info, debug)

            Default Logging Level
        carpstatusvip (str | Unset): (Service Control) CARP Status VIP

            Used to determine the CARP status. When the CARP vhid is in BACKUP status, pimd will not be started.
        default_route_distance (str | Unset): (General Settings) Default Route Distance

            Default value for unicast routing protocol administrative distance. It is used
            in PIM Assert elections to determine upstream routers.  The router advertising
            the lowest assert preference will be selected as the forwarder and upstream
            router for the LAN.
            (1-255, Default: 101)
        default_route_metric (str | Unset): (General Settings) Default Route Metric

            The default cost for sending data through this router. Only PIM-SM data should
            to go to this daemon; so a high value is recommended to prevent accidental
            usage.
            (1-1024, Default: 1024)
        igmp_query_interval (str | Unset): (General Settings) IGMP Query Interval

            The interval, in seconds, between IGMP queries when elected as querier.
            (1-65535, Default: 12)
        igmp_querier_timeout (str | Unset): (General Settings) IGMP Querier Timeout

            The timeout, in seconds, after which PIMD will take over for a failed elected
            querier.
            (8-65535, Default: 42)
        hello_interval (str | Unset): (General Settings) Hello Interval

            The interval, in seconds, between PIM Hello messages sent by pimd. This value
            also affects the Hold Time, which is 3.5x this value.
            (30-18724, Default: 30)
        spt_type (str | Unset): (Tree Switch Threshold) Threshold Type (default, rate, packets, infinity)

            Type of check to perform when making SPT decisions.
        spt_value (str | Unset): (Tree Switch Threshold) Threshold Value

            When Threshold Type is set to Rate, this value is a rate in Kbit/s.
            When set to Packets, this value is a specific number of packets.
            When set to Default or Infinity, this value is ignored.
        spt_interval (str | Unset): (Tree Switch Threshold) SPT Interval

            The interval, in seconds, after which PIMD will switch from the shared tree to
            the shortest-path source tree.
            (Default: 100)
        carp_vip_options (list[TextValue] | Unset):
    """

    enable: bool | Unset = UNSET
    interfacemode: str | Unset = UNSET
    loglevel: str | Unset = UNSET
    carpstatusvip: str | Unset = UNSET
    default_route_distance: str | Unset = UNSET
    default_route_metric: str | Unset = UNSET
    igmp_query_interval: str | Unset = UNSET
    igmp_querier_timeout: str | Unset = UNSET
    hello_interval: str | Unset = UNSET
    spt_type: str | Unset = UNSET
    spt_value: str | Unset = UNSET
    spt_interval: str | Unset = UNSET
    carp_vip_options: list[TextValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        interfacemode = self.interfacemode

        loglevel = self.loglevel

        carpstatusvip = self.carpstatusvip

        default_route_distance = self.default_route_distance

        default_route_metric = self.default_route_metric

        igmp_query_interval = self.igmp_query_interval

        igmp_querier_timeout = self.igmp_querier_timeout

        hello_interval = self.hello_interval

        spt_type = self.spt_type

        spt_value = self.spt_value

        spt_interval = self.spt_interval

        carp_vip_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.carp_vip_options, Unset):
            carp_vip_options = []
            for carp_vip_options_item_data in self.carp_vip_options:
                carp_vip_options_item = carp_vip_options_item_data.to_dict()
                carp_vip_options.append(carp_vip_options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if interfacemode is not UNSET:
            field_dict["interfacemode"] = interfacemode
        if loglevel is not UNSET:
            field_dict["loglevel"] = loglevel
        if carpstatusvip is not UNSET:
            field_dict["carpstatusvip"] = carpstatusvip
        if default_route_distance is not UNSET:
            field_dict["default_route_distance"] = default_route_distance
        if default_route_metric is not UNSET:
            field_dict["default_route_metric"] = default_route_metric
        if igmp_query_interval is not UNSET:
            field_dict["igmp_query_interval"] = igmp_query_interval
        if igmp_querier_timeout is not UNSET:
            field_dict["igmp_querier_timeout"] = igmp_querier_timeout
        if hello_interval is not UNSET:
            field_dict["hello_interval"] = hello_interval
        if spt_type is not UNSET:
            field_dict["spt_type"] = spt_type
        if spt_value is not UNSET:
            field_dict["spt_value"] = spt_value
        if spt_interval is not UNSET:
            field_dict["spt_interval"] = spt_interval
        if carp_vip_options is not UNSET:
            field_dict["carp_vip_options"] = carp_vip_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_value import TextValue

        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        interfacemode = d.pop("interfacemode", UNSET)

        loglevel = d.pop("loglevel", UNSET)

        carpstatusvip = d.pop("carpstatusvip", UNSET)

        default_route_distance = d.pop("default_route_distance", UNSET)

        default_route_metric = d.pop("default_route_metric", UNSET)

        igmp_query_interval = d.pop("igmp_query_interval", UNSET)

        igmp_querier_timeout = d.pop("igmp_querier_timeout", UNSET)

        hello_interval = d.pop("hello_interval", UNSET)

        spt_type = d.pop("spt_type", UNSET)

        spt_value = d.pop("spt_value", UNSET)

        spt_interval = d.pop("spt_interval", UNSET)

        _carp_vip_options = d.pop("carp_vip_options", UNSET)
        carp_vip_options: list[TextValue] | Unset = UNSET
        if _carp_vip_options is not UNSET:
            carp_vip_options = []
            for carp_vip_options_item_data in _carp_vip_options:
                carp_vip_options_item = TextValue.from_dict(carp_vip_options_item_data)

                carp_vip_options.append(carp_vip_options_item)

        pimd = cls(
            enable=enable,
            interfacemode=interfacemode,
            loglevel=loglevel,
            carpstatusvip=carpstatusvip,
            default_route_distance=default_route_distance,
            default_route_metric=default_route_metric,
            igmp_query_interval=igmp_query_interval,
            igmp_querier_timeout=igmp_querier_timeout,
            hello_interval=hello_interval,
            spt_type=spt_type,
            spt_value=spt_value,
            spt_interval=spt_interval,
            carp_vip_options=carp_vip_options,
        )

        pimd.additional_properties = d
        return pimd

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
