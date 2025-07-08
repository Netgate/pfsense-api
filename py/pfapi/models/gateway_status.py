from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GatewayStatus")


@_attrs_define
class GatewayStatus:
    """
    Attributes:
        name (str):
        gateway (str):
        defaultgw (Union[Unset, bool]): default gateway
        monitor (Union[Unset, str]):
        descr (Union[Unset, str]):
        delay (Union[Unset, str]):
        stddev (Union[Unset, str]):
        loss (Union[Unset, str]):
        status (Union[Unset, str]):
        display (Union[Unset, str]):
    """

    name: str
    gateway: str
    defaultgw: Union[Unset, bool] = UNSET
    monitor: Union[Unset, str] = UNSET
    descr: Union[Unset, str] = UNSET
    delay: Union[Unset, str] = UNSET
    stddev: Union[Unset, str] = UNSET
    loss: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    display: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        gateway = self.gateway

        defaultgw = self.defaultgw

        monitor = self.monitor

        descr = self.descr

        delay = self.delay

        stddev = self.stddev

        loss = self.loss

        status = self.status

        display = self.display

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "gateway": gateway,
            }
        )
        if defaultgw is not UNSET:
            field_dict["defaultgw"] = defaultgw
        if monitor is not UNSET:
            field_dict["monitor"] = monitor
        if descr is not UNSET:
            field_dict["descr"] = descr
        if delay is not UNSET:
            field_dict["delay"] = delay
        if stddev is not UNSET:
            field_dict["stddev"] = stddev
        if loss is not UNSET:
            field_dict["loss"] = loss
        if status is not UNSET:
            field_dict["status"] = status
        if display is not UNSET:
            field_dict["display"] = display

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        gateway = d.pop("gateway")

        defaultgw = d.pop("defaultgw", UNSET)

        monitor = d.pop("monitor", UNSET)

        descr = d.pop("descr", UNSET)

        delay = d.pop("delay", UNSET)

        stddev = d.pop("stddev", UNSET)

        loss = d.pop("loss", UNSET)

        status = d.pop("status", UNSET)

        display = d.pop("display", UNSET)

        gateway_status = cls(
            name=name,
            gateway=gateway,
            defaultgw=defaultgw,
            monitor=monitor,
            descr=descr,
            delay=delay,
            stddev=stddev,
            loss=loss,
            status=status,
            display=display,
        )

        gateway_status.additional_properties = d
        return gateway_status

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
