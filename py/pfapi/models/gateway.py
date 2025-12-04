from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gateway_defaults import GatewayDefaults


T = TypeVar("T", bound="Gateway")


@_attrs_define
class Gateway:
    """
    Attributes:
        gateway (str):
        name (str | Unset):
        dynamic (bool | Unset):
        disabled (bool | Unset):
        ipprotocol (str | Unset):
        gw_down_kill_states (str | Unset):
        interface_device (str | Unset):
        interface_identity (str | Unset):
        interface_assigned (str | Unset):
        interface (str | Unset): obsolete - use interface_device
        friendlyiface (str | Unset): obsolete - use interface_identity
        friendlyifdescr (str | Unset): obsolete - use interface_assigned
        action_disable (bool | Unset):
        attribute (str | Unset):
        isdefaultgw (bool | Unset):
        monitor (str | Unset):
        monitor_disable (bool | Unset):
        descr (str | Unset):
        tiername (str | Unset):
        weight (int | Unset):
        data_payload (int | Unset):
        interval (int | Unset):
        latencylow (int | Unset):
        latencyhigh (int | Unset):
        losslow (int | Unset):
        losshigh (int | Unset):
        loss_interval (int | Unset):
        time_period (int | Unset):
        alert_interval (int | Unset):
        nonlocalgateway (bool | Unset):
        defaults (GatewayDefaults | Unset):
    """

    gateway: str
    name: str | Unset = UNSET
    dynamic: bool | Unset = UNSET
    disabled: bool | Unset = UNSET
    ipprotocol: str | Unset = UNSET
    gw_down_kill_states: str | Unset = UNSET
    interface_device: str | Unset = UNSET
    interface_identity: str | Unset = UNSET
    interface_assigned: str | Unset = UNSET
    interface: str | Unset = UNSET
    friendlyiface: str | Unset = UNSET
    friendlyifdescr: str | Unset = UNSET
    action_disable: bool | Unset = UNSET
    attribute: str | Unset = UNSET
    isdefaultgw: bool | Unset = UNSET
    monitor: str | Unset = UNSET
    monitor_disable: bool | Unset = UNSET
    descr: str | Unset = UNSET
    tiername: str | Unset = UNSET
    weight: int | Unset = UNSET
    data_payload: int | Unset = UNSET
    interval: int | Unset = UNSET
    latencylow: int | Unset = UNSET
    latencyhigh: int | Unset = UNSET
    losslow: int | Unset = UNSET
    losshigh: int | Unset = UNSET
    loss_interval: int | Unset = UNSET
    time_period: int | Unset = UNSET
    alert_interval: int | Unset = UNSET
    nonlocalgateway: bool | Unset = UNSET
    defaults: GatewayDefaults | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gateway = self.gateway

        name = self.name

        dynamic = self.dynamic

        disabled = self.disabled

        ipprotocol = self.ipprotocol

        gw_down_kill_states = self.gw_down_kill_states

        interface_device = self.interface_device

        interface_identity = self.interface_identity

        interface_assigned = self.interface_assigned

        interface = self.interface

        friendlyiface = self.friendlyiface

        friendlyifdescr = self.friendlyifdescr

        action_disable = self.action_disable

        attribute = self.attribute

        isdefaultgw = self.isdefaultgw

        monitor = self.monitor

        monitor_disable = self.monitor_disable

        descr = self.descr

        tiername = self.tiername

        weight = self.weight

        data_payload = self.data_payload

        interval = self.interval

        latencylow = self.latencylow

        latencyhigh = self.latencyhigh

        losslow = self.losslow

        losshigh = self.losshigh

        loss_interval = self.loss_interval

        time_period = self.time_period

        alert_interval = self.alert_interval

        nonlocalgateway = self.nonlocalgateway

        defaults: dict[str, Any] | Unset = UNSET
        if not isinstance(self.defaults, Unset):
            defaults = self.defaults.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gateway": gateway,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if dynamic is not UNSET:
            field_dict["dynamic"] = dynamic
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if ipprotocol is not UNSET:
            field_dict["ipprotocol"] = ipprotocol
        if gw_down_kill_states is not UNSET:
            field_dict["gw_down_kill_states"] = gw_down_kill_states
        if interface_device is not UNSET:
            field_dict["interface_device"] = interface_device
        if interface_identity is not UNSET:
            field_dict["interface_identity"] = interface_identity
        if interface_assigned is not UNSET:
            field_dict["interface_assigned"] = interface_assigned
        if interface is not UNSET:
            field_dict["interface"] = interface
        if friendlyiface is not UNSET:
            field_dict["friendlyiface"] = friendlyiface
        if friendlyifdescr is not UNSET:
            field_dict["friendlyifdescr"] = friendlyifdescr
        if action_disable is not UNSET:
            field_dict["action_disable"] = action_disable
        if attribute is not UNSET:
            field_dict["attribute"] = attribute
        if isdefaultgw is not UNSET:
            field_dict["isdefaultgw"] = isdefaultgw
        if monitor is not UNSET:
            field_dict["monitor"] = monitor
        if monitor_disable is not UNSET:
            field_dict["monitor_disable"] = monitor_disable
        if descr is not UNSET:
            field_dict["descr"] = descr
        if tiername is not UNSET:
            field_dict["tiername"] = tiername
        if weight is not UNSET:
            field_dict["weight"] = weight
        if data_payload is not UNSET:
            field_dict["data_payload"] = data_payload
        if interval is not UNSET:
            field_dict["interval"] = interval
        if latencylow is not UNSET:
            field_dict["latencylow"] = latencylow
        if latencyhigh is not UNSET:
            field_dict["latencyhigh"] = latencyhigh
        if losslow is not UNSET:
            field_dict["losslow"] = losslow
        if losshigh is not UNSET:
            field_dict["losshigh"] = losshigh
        if loss_interval is not UNSET:
            field_dict["loss_interval"] = loss_interval
        if time_period is not UNSET:
            field_dict["time_period"] = time_period
        if alert_interval is not UNSET:
            field_dict["alert_interval"] = alert_interval
        if nonlocalgateway is not UNSET:
            field_dict["nonlocalgateway"] = nonlocalgateway
        if defaults is not UNSET:
            field_dict["defaults"] = defaults

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gateway_defaults import GatewayDefaults

        d = dict(src_dict)
        gateway = d.pop("gateway")

        name = d.pop("name", UNSET)

        dynamic = d.pop("dynamic", UNSET)

        disabled = d.pop("disabled", UNSET)

        ipprotocol = d.pop("ipprotocol", UNSET)

        gw_down_kill_states = d.pop("gw_down_kill_states", UNSET)

        interface_device = d.pop("interface_device", UNSET)

        interface_identity = d.pop("interface_identity", UNSET)

        interface_assigned = d.pop("interface_assigned", UNSET)

        interface = d.pop("interface", UNSET)

        friendlyiface = d.pop("friendlyiface", UNSET)

        friendlyifdescr = d.pop("friendlyifdescr", UNSET)

        action_disable = d.pop("action_disable", UNSET)

        attribute = d.pop("attribute", UNSET)

        isdefaultgw = d.pop("isdefaultgw", UNSET)

        monitor = d.pop("monitor", UNSET)

        monitor_disable = d.pop("monitor_disable", UNSET)

        descr = d.pop("descr", UNSET)

        tiername = d.pop("tiername", UNSET)

        weight = d.pop("weight", UNSET)

        data_payload = d.pop("data_payload", UNSET)

        interval = d.pop("interval", UNSET)

        latencylow = d.pop("latencylow", UNSET)

        latencyhigh = d.pop("latencyhigh", UNSET)

        losslow = d.pop("losslow", UNSET)

        losshigh = d.pop("losshigh", UNSET)

        loss_interval = d.pop("loss_interval", UNSET)

        time_period = d.pop("time_period", UNSET)

        alert_interval = d.pop("alert_interval", UNSET)

        nonlocalgateway = d.pop("nonlocalgateway", UNSET)

        _defaults = d.pop("defaults", UNSET)
        defaults: GatewayDefaults | Unset
        if isinstance(_defaults, Unset):
            defaults = UNSET
        else:
            defaults = GatewayDefaults.from_dict(_defaults)

        gateway = cls(
            gateway=gateway,
            name=name,
            dynamic=dynamic,
            disabled=disabled,
            ipprotocol=ipprotocol,
            gw_down_kill_states=gw_down_kill_states,
            interface_device=interface_device,
            interface_identity=interface_identity,
            interface_assigned=interface_assigned,
            interface=interface,
            friendlyiface=friendlyiface,
            friendlyifdescr=friendlyifdescr,
            action_disable=action_disable,
            attribute=attribute,
            isdefaultgw=isdefaultgw,
            monitor=monitor,
            monitor_disable=monitor_disable,
            descr=descr,
            tiername=tiername,
            weight=weight,
            data_payload=data_payload,
            interval=interval,
            latencylow=latencylow,
            latencyhigh=latencyhigh,
            losslow=losslow,
            losshigh=losshigh,
            loss_interval=loss_interval,
            time_period=time_period,
            alert_interval=alert_interval,
            nonlocalgateway=nonlocalgateway,
            defaults=defaults,
        )

        gateway.additional_properties = d
        return gateway

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
