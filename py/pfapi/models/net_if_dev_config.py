from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NetIfDevConfig")


@_attrs_define
class NetIfDevConfig:
    """
    Attributes:
        device (Union[Unset, str]): original name of the device
        bus_path (Union[Unset, str]): BUS path of the device
        mac (Union[Unset, str]): original MAC address
        parent_device (Union[Unset, str]): parent device
        parent_path (Union[Unset, str]): parent device bus path
        iftype (Union[Unset, str]): interface type
        members (Union[Unset, List[str]]):
    """

    device: Union[Unset, str] = UNSET
    bus_path: Union[Unset, str] = UNSET
    mac: Union[Unset, str] = UNSET
    parent_device: Union[Unset, str] = UNSET
    parent_path: Union[Unset, str] = UNSET
    iftype: Union[Unset, str] = UNSET
    members: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        device = self.device

        bus_path = self.bus_path

        mac = self.mac

        parent_device = self.parent_device

        parent_path = self.parent_path

        iftype = self.iftype

        members: Union[Unset, List[str]] = UNSET
        if not isinstance(self.members, Unset):
            members = self.members

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device is not UNSET:
            field_dict["device"] = device
        if bus_path is not UNSET:
            field_dict["bus_path"] = bus_path
        if mac is not UNSET:
            field_dict["mac"] = mac
        if parent_device is not UNSET:
            field_dict["parent_device"] = parent_device
        if parent_path is not UNSET:
            field_dict["parent_path"] = parent_path
        if iftype is not UNSET:
            field_dict["iftype"] = iftype
        if members is not UNSET:
            field_dict["members"] = members

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        device = d.pop("device", UNSET)

        bus_path = d.pop("bus_path", UNSET)

        mac = d.pop("mac", UNSET)

        parent_device = d.pop("parent_device", UNSET)

        parent_path = d.pop("parent_path", UNSET)

        iftype = d.pop("iftype", UNSET)

        members = cast(List[str], d.pop("members", UNSET))

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
