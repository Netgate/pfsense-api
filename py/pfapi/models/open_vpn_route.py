from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OpenVPNRoute")


@_attrs_define
class OpenVPNRoute:
    """
    Attributes:
        virtual_addr (str):
        common_name (str):
        remote_host (str):
        last_time (str):
    """

    virtual_addr: str
    common_name: str
    remote_host: str
    last_time: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        virtual_addr = self.virtual_addr

        common_name = self.common_name

        remote_host = self.remote_host

        last_time = self.last_time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "virtual_addr": virtual_addr,
                "common_name": common_name,
                "remote_host": remote_host,
                "last_time": last_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        virtual_addr = d.pop("virtual_addr")

        common_name = d.pop("common_name")

        remote_host = d.pop("remote_host")

        last_time = d.pop("last_time")

        open_vpn_route = cls(
            virtual_addr=virtual_addr,
            common_name=common_name,
            remote_host=remote_host,
            last_time=last_time,
        )

        open_vpn_route.additional_properties = d
        return open_vpn_route

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
