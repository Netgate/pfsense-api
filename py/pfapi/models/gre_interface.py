from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GREInterface")


@_attrs_define
class GREInterface:
    """
    Attributes:
        if_ (Union[Unset, str]):
        tunnel_local_addr (Union[Unset, str]):
        tunnel_remote_addr (Union[Unset, str]):
        tunnel_local_addr6 (Union[Unset, str]):
        tunnel_remote_addr6 (Union[Unset, str]):
        tunnel_remote_net (Union[Unset, str]):
        tunnel_remote_net6 (Union[Unset, str]):
        remote_addr (Union[Unset, str]):
        descr (Union[Unset, str]):
        link1 (Union[Unset, bool]):
        greif (Union[Unset, str]):
    """

    if_: Union[Unset, str] = UNSET
    tunnel_local_addr: Union[Unset, str] = UNSET
    tunnel_remote_addr: Union[Unset, str] = UNSET
    tunnel_local_addr6: Union[Unset, str] = UNSET
    tunnel_remote_addr6: Union[Unset, str] = UNSET
    tunnel_remote_net: Union[Unset, str] = UNSET
    tunnel_remote_net6: Union[Unset, str] = UNSET
    remote_addr: Union[Unset, str] = UNSET
    descr: Union[Unset, str] = UNSET
    link1: Union[Unset, bool] = UNSET
    greif: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if_ = self.if_

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
        field_dict.update({})
        if if_ is not UNSET:
            field_dict["if"] = if_
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
        if_ = d.pop("if", UNSET)

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
            if_=if_,
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
