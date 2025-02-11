from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GatewayStatus")


@_attrs_define
class GatewayStatus:
    """
    Attributes:
        name (str):
        gateway (str):
        monitor (str):
        descr (str):
        delay (str):
        stddev (str):
        loss (str):
        status (str):
        display (str):
    """

    name: str
    gateway: str
    monitor: str
    descr: str
    delay: str
    stddev: str
    loss: str
    status: str
    display: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        gateway = self.gateway

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
                "monitor": monitor,
                "descr": descr,
                "delay": delay,
                "stddev": stddev,
                "loss": loss,
                "status": status,
                "display": display,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        gateway = d.pop("gateway")

        monitor = d.pop("monitor")

        descr = d.pop("descr")

        delay = d.pop("delay")

        stddev = d.pop("stddev")

        loss = d.pop("loss")

        status = d.pop("status")

        display = d.pop("display")

        gateway_status = cls(
            name=name,
            gateway=gateway,
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
