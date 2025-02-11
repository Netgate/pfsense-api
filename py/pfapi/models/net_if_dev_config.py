from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="NetIfDevConfig")


@_attrs_define
class NetIfDevConfig:
    """
    Attributes:
        device (str): original name of the device
        bus_path (str): BUS path of the device
        mac (str): original MAC address
        parent_device (str): parent device
        parent_path (str): parent device bus path
        iftype (str): interface type
        members (List[str]):
    """

    device: str
    bus_path: str
    mac: str
    parent_device: str
    parent_path: str
    iftype: str
    members: List[str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        device = self.device

        bus_path = self.bus_path

        mac = self.mac

        parent_device = self.parent_device

        parent_path = self.parent_path

        iftype = self.iftype

        members = self.members

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "device": device,
                "bus_path": bus_path,
                "mac": mac,
                "parent_device": parent_device,
                "parent_path": parent_path,
                "iftype": iftype,
                "members": members,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        device = d.pop("device")

        bus_path = d.pop("bus_path")

        mac = d.pop("mac")

        parent_device = d.pop("parent_device")

        parent_path = d.pop("parent_path")

        iftype = d.pop("iftype")

        members = cast(List[str], d.pop("members"))

        net_if_dev_config = cls(
            device=device,
            bus_path=bus_path,
            mac=mac,
            parent_device=parent_device,
            parent_path=parent_path,
            iftype=iftype,
            members=members,
        )

        net_if_dev_config.additional_properties = d
        return net_if_dev_config

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
