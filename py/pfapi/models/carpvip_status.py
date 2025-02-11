from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CARPVIPStatus")


@_attrs_define
class CARPVIPStatus:
    """
    Attributes:
        interface (str):
        virtual_ip (str):
        mode (str):
        peer (str):
        description (str):
        status (str):
        virtual_aliases (Union[Unset, List[str]]):
    """

    interface: str
    virtual_ip: str
    mode: str
    peer: str
    description: str
    status: str
    virtual_aliases: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        interface = self.interface

        virtual_ip = self.virtual_ip

        mode = self.mode

        peer = self.peer

        description = self.description

        status = self.status

        virtual_aliases: Union[Unset, List[str]] = UNSET
        if not isinstance(self.virtual_aliases, Unset):
            virtual_aliases = self.virtual_aliases

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "interface": interface,
                "virtual_ip": virtual_ip,
                "mode": mode,
                "peer": peer,
                "description": description,
                "status": status,
            }
        )
        if virtual_aliases is not UNSET:
            field_dict["virtual_aliases"] = virtual_aliases

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        interface = d.pop("interface")

        virtual_ip = d.pop("virtual_ip")

        mode = d.pop("mode")

        peer = d.pop("peer")

        description = d.pop("description")

        status = d.pop("status")

        virtual_aliases = cast(List[str], d.pop("virtual_aliases", UNSET))

        carpvip_status = cls(
            interface=interface,
            virtual_ip=virtual_ip,
            mode=mode,
            peer=peer,
            description=description,
            status=status,
            virtual_aliases=virtual_aliases,
        )

        carpvip_status.additional_properties = d
        return carpvip_status

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
