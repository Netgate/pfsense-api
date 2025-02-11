from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

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
        name (str):
        dynamic (bool):
        disabled (bool):
        ipprotocol (str):
        gateway (str):
        gw_down_kill_states (str):
        interface (str):
        friendlyiface (str):
        friendlyifdescr (str):
        action_disable (bool):
        attribute (str):
        isdefaultgw (bool):
        monitor (str):
        monitor_disable (bool):
        descr (str):
        tiername (str):
        weight (int):
        data_payload (int):
        interval (int):
        latencylow (int):
        latencyhigh (int):
        losslow (int):
        losshigh (int):
        loss_interval (int):
        time_period (int):
        alert_interval (int):
        nonlocalgateway (bool):
        defaults (Union[Unset, GatewayDefaults]):
    """

    name: str
    dynamic: bool
    disabled: bool
    ipprotocol: str
    gateway: str
    gw_down_kill_states: str
    interface: str
    friendlyiface: str
    friendlyifdescr: str
    action_disable: bool
    attribute: str
    isdefaultgw: bool
    monitor: str
    monitor_disable: bool
    descr: str
    tiername: str
    weight: int
    data_payload: int
    interval: int
    latencylow: int
    latencyhigh: int
    losslow: int
    losshigh: int
    loss_interval: int
    time_period: int
    alert_interval: int
    nonlocalgateway: bool
    defaults: Union[Unset, "GatewayDefaults"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        dynamic = self.dynamic

        disabled = self.disabled

        ipprotocol = self.ipprotocol

        gateway = self.gateway

        gw_down_kill_states = self.gw_down_kill_states

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

        defaults: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.defaults, Unset):
            defaults = self.defaults.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "dynamic": dynamic,
                "disabled": disabled,
                "ipprotocol": ipprotocol,
                "gateway": gateway,
                "gw_down_kill_states": gw_down_kill_states,
                "interface": interface,
                "friendlyiface": friendlyiface,
                "friendlyifdescr": friendlyifdescr,
                "action_disable": action_disable,
                "attribute": attribute,
                "isdefaultgw": isdefaultgw,
                "monitor": monitor,
                "monitor_disable": monitor_disable,
                "descr": descr,
                "tiername": tiername,
                "weight": weight,
                "data_payload": data_payload,
                "interval": interval,
                "latencylow": latencylow,
                "latencyhigh": latencyhigh,
                "losslow": losslow,
                "losshigh": losshigh,
                "loss_interval": loss_interval,
                "time_period": time_period,
                "alert_interval": alert_interval,
                "nonlocalgateway": nonlocalgateway,
            }
        )
        if defaults is not UNSET:
            field_dict["defaults"] = defaults

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.gateway_defaults import GatewayDefaults

        d = src_dict.copy()
        name = d.pop("name")

        dynamic = d.pop("dynamic")

        disabled = d.pop("disabled")

        ipprotocol = d.pop("ipprotocol")

        gateway = d.pop("gateway")

        gw_down_kill_states = d.pop("gw_down_kill_states")

        interface = d.pop("interface")

        friendlyiface = d.pop("friendlyiface")

        friendlyifdescr = d.pop("friendlyifdescr")

        action_disable = d.pop("action_disable")

        attribute = d.pop("attribute")

        isdefaultgw = d.pop("isdefaultgw")

        monitor = d.pop("monitor")

        monitor_disable = d.pop("monitor_disable")

        descr = d.pop("descr")

        tiername = d.pop("tiername")

        weight = d.pop("weight")

        data_payload = d.pop("data_payload")

        interval = d.pop("interval")

        latencylow = d.pop("latencylow")

        latencyhigh = d.pop("latencyhigh")

        losslow = d.pop("losslow")

        losshigh = d.pop("losshigh")

        loss_interval = d.pop("loss_interval")

        time_period = d.pop("time_period")

        alert_interval = d.pop("alert_interval")

        nonlocalgateway = d.pop("nonlocalgateway")

        _defaults = d.pop("defaults", UNSET)
        defaults: Union[Unset, GatewayDefaults]
        if isinstance(_defaults, Unset):
            defaults = UNSET
        else:
            defaults = GatewayDefaults.from_dict(_defaults)

        gateway = cls(
            name=name,
            dynamic=dynamic,
            disabled=disabled,
            ipprotocol=ipprotocol,
            gateway=gateway,
            gw_down_kill_states=gw_down_kill_states,
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
