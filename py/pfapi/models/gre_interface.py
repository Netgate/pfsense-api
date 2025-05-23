from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GREInterface")


@_attrs_define
class GREInterface:
    """
    Attributes:
        if_identity (str): identity name of the parent interface
        tunnel_local_addr (Union[Unset, str]): local ipv4 tunnel address
        tunnel_remote_addr (Union[Unset, str]): remote ipv4 tunnel address
        tunnel_local_addr6 (Union[Unset, str]): local ipv6 tunnel address
        tunnel_remote_addr6 (Union[Unset, str]): remote ipv6 tunnel address
        tunnel_remote_net (Union[Unset, int]): remote ipv4 tunnel address subnet
        tunnel_remote_net6 (Union[Unset, int]): remote ipv6 tunnel address subnet
        remote_addr (Union[Unset, str]): address of the remote peer
        descr (Union[Unset, str]): description
        link1 (Union[Unset, bool]): add an explicit static route for the remote inner tunnel
        greif (Union[Unset, str]): generated by system when create gre
    """

    if_identity: str
    tunnel_local_addr: Union[Unset, str] = UNSET
    tunnel_remote_addr: Union[Unset, str] = UNSET
    tunnel_local_addr6: Union[Unset, str] = UNSET
    tunnel_remote_addr6: Union[Unset, str] = UNSET
    tunnel_remote_net: Union[Unset, int] = UNSET
    tunnel_remote_net6: Union[Unset, int] = UNSET
    remote_addr: Union[Unset, str] = UNSET
    descr: Union[Unset, str] = UNSET
    link1: Union[Unset, bool] = UNSET
    greif: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if_identity = self.if_identity

        tunnel_local_addr = self.tunnel_local_addr

        tunnel_remote_addr = self.tunnel_remote_addr

        tunnel_local_addr6 = self.tunnel_local_addr6

        tunnel_remote_addr6 = self.tunnel_remote_addr6

        tunnel_remote_net = self.tunnel_remote_net

        tunnel_remote_net6 = self.tunnel_remote_net6

        remote_addr = self.remote_addr

        descr = self.descr

        link1 = self.link1

        greif = self.greif

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "if_identity": if_identity,
            }
        )
        if tunnel_local_addr is not UNSET:
            field_dict["tunnel_local_addr"] = tunnel_local_addr
        if tunnel_remote_addr is not UNSET:
            field_dict["tunnel_remote_addr"] = tunnel_remote_addr
        if tunnel_local_addr6 is not UNSET:
            field_dict["tunnel_local_addr6"] = tunnel_local_addr6
        if tunnel_remote_addr6 is not UNSET:
            field_dict["tunnel_remote_addr6"] = tunnel_remote_addr6
        if tunnel_remote_net is not UNSET:
            field_dict["tunnel_remote_net"] = tunnel_remote_net
        if tunnel_remote_net6 is not UNSET:
            field_dict["tunnel_remote_net6"] = tunnel_remote_net6
        if remote_addr is not UNSET:
            field_dict["remote_addr"] = remote_addr
        if descr is not UNSET:
            field_dict["descr"] = descr
        if link1 is not UNSET:
            field_dict["link1"] = link1
        if greif is not UNSET:
            field_dict["greif"] = greif

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        if_identity = d.pop("if_identity")

        tunnel_local_addr = d.pop("tunnel_local_addr", UNSET)

        tunnel_remote_addr = d.pop("tunnel_remote_addr", UNSET)

        tunnel_local_addr6 = d.pop("tunnel_local_addr6", UNSET)

        tunnel_remote_addr6 = d.pop("tunnel_remote_addr6", UNSET)

        tunnel_remote_net = d.pop("tunnel_remote_net", UNSET)

        tunnel_remote_net6 = d.pop("tunnel_remote_net6", UNSET)

        remote_addr = d.pop("remote_addr", UNSET)

        descr = d.pop("descr", UNSET)

        link1 = d.pop("link1", UNSET)

        greif = d.pop("greif", UNSET)

        gre_interface = cls(
            if_identity=if_identity,
            tunnel_local_addr=tunnel_local_addr,
            tunnel_remote_addr=tunnel_remote_addr,
            tunnel_local_addr6=tunnel_local_addr6,
            tunnel_remote_addr6=tunnel_remote_addr6,
            tunnel_remote_net=tunnel_remote_net,
            tunnel_remote_net6=tunnel_remote_net6,
            remote_addr=remote_addr,
            descr=descr,
            link1=link1,
            greif=greif,
        )

        gre_interface.additional_properties = d
        return gre_interface

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
