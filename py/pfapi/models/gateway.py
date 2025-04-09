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
        gateway (str):
        name (Union[Unset, str]):
        dynamic (Union[Unset, bool]):
        disabled (Union[Unset, bool]):
        ipprotocol (Union[Unset, str]):
        gw_down_kill_states (Union[Unset, str]):
        interface_device (Union[Unset, str]):
        interface_identity (Union[Unset, str]):
        interface_assigned (Union[Unset, str]):
        interface (Union[Unset, str]): obsolete - use interface_device
        friendlyiface (Union[Unset, str]): obsolete - use interface_identity
        friendlyifdescr (Union[Unset, str]): obsolete - use interface_assigned
        action_disable (Union[Unset, bool]):
        attribute (Union[Unset, str]):
        isdefaultgw (Union[Unset, bool]):
        monitor (Union[Unset, str]):
        monitor_disable (Union[Unset, bool]):
        descr (Union[Unset, str]):
        tiername (Union[Unset, str]):
        weight (Union[Unset, int]):
        data_payload (Union[Unset, int]):
        interval (Union[Unset, int]):
        latencylow (Union[Unset, int]):
        latencyhigh (Union[Unset, int]):
        losslow (Union[Unset, int]):
        losshigh (Union[Unset, int]):
        loss_interval (Union[Unset, int]):
        time_period (Union[Unset, int]):
        alert_interval (Union[Unset, int]):
        nonlocalgateway (Union[Unset, bool]):
        defaults (Union[Unset, GatewayDefaults]):
    """

    gateway: str
    name: Union[Unset, str] = UNSET
    dynamic: Union[Unset, bool] = UNSET
    disabled: Union[Unset, bool] = UNSET
    ipprotocol: Union[Unset, str] = UNSET
    gw_down_kill_states: Union[Unset, str] = UNSET
    interface_device: Union[Unset, str] = UNSET
    interface_identity: Union[Unset, str] = UNSET
    interface_assigned: Union[Unset, str] = UNSET
    interface: Union[Unset, str] = UNSET
    friendlyiface: Union[Unset, str] = UNSET
    friendlyifdescr: Union[Unset, str] = UNSET
    action_disable: Union[Unset, bool] = UNSET
    attribute: Union[Unset, str] = UNSET
    isdefaultgw: Union[Unset, bool] = UNSET
    monitor: Union[Unset, str] = UNSET
    monitor_disable: Union[Unset, bool] = UNSET
    descr: Union[Unset, str] = UNSET
    tiername: Union[Unset, str] = UNSET
    weight: Union[Unset, int] = UNSET
    data_payload: Union[Unset, int] = UNSET
    interval: Union[Unset, int] = UNSET
    latencylow: Union[Unset, int] = UNSET
    latencyhigh: Union[Unset, int] = UNSET
    losslow: Union[Unset, int] = UNSET
    losshigh: Union[Unset, int] = UNSET
    loss_interval: Union[Unset, int] = UNSET
    time_period: Union[Unset, int] = UNSET
    alert_interval: Union[Unset, int] = UNSET
    nonlocalgateway: Union[Unset, bool] = UNSET
    defaults: Union[Unset, "GatewayDefaults"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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

        defaults: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.defaults, Unset):
            defaults = self.defaults.to_dict()

        field_dict: Dict[str, Any] = {}
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.gateway_defaults import GatewayDefaults

        d = src_dict.copy()
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
        defaults: Union[Unset, GatewayDefaults]
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
