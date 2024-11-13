from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CARPVIPStatus")


@_attrs_define
class CARPVIPStatus:
    """
    Attributes:
        interface (Union[Unset, str]):
        virtual_ip (Union[Unset, str]):
        virtual_aliases (Union[Unset, List[str]]):
        mode (Union[Unset, str]):
        peer (Union[Unset, str]):
        description (Union[Unset, str]):
        status (Union[Unset, str]):
    """

    interface: Union[Unset, str] = UNSET
    virtual_ip: Union[Unset, str] = UNSET
    virtual_aliases: Union[Unset, List[str]] = UNSET
    mode: Union[Unset, str] = UNSET
    peer: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        interface = self.interface

        virtual_ip = self.virtual_ip

        virtual_aliases: Union[Unset, List[str]] = UNSET
        if not isinstance(self.virtual_aliases, Unset):
            virtual_aliases = self.virtual_aliases

        mode = self.mode

        peer = self.peer

        description = self.description

        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interface is not UNSET:
            field_dict["interface"] = interface
        if virtual_ip is not UNSET:
            field_dict["virtual_ip"] = virtual_ip
        if virtual_aliases is not UNSET:
            field_dict["virtual_aliases"] = virtual_aliases
        if mode is not UNSET:
            field_dict["mode"] = mode
        if peer is not UNSET:
            field_dict["peer"] = peer
        if description is not UNSET:
            field_dict["description"] = description
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        interface = d.pop("interface", UNSET)

        virtual_ip = d.pop("virtual_ip", UNSET)

        virtual_aliases = cast(List[str], d.pop("virtual_aliases", UNSET))

        mode = d.pop("mode", UNSET)

        peer = d.pop("peer", UNSET)

        description = d.pop("description", UNSET)

        status = d.pop("status", UNSET)

        carpvip_status = cls(
            interface=interface,
            virtual_ip=virtual_ip,
            virtual_aliases=virtual_aliases,
            mode=mode,
            peer=peer,
            description=description,
            status=status,
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
