from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NtpServer")


@_attrs_define
class NtpServer:
    """
    Attributes:
        addr (str):
        type (str): pool | peer | server
        prefer (Union[Unset, bool]):
        no_select (Union[Unset, bool]):
    """

    addr: str
    type: str
    prefer: Union[Unset, bool] = UNSET
    no_select: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        addr = self.addr

        type = self.type

        prefer = self.prefer

        no_select = self.no_select

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "addr": addr,
                "type": type,
            }
        )
        if prefer is not UNSET:
            field_dict["prefer"] = prefer
        if no_select is not UNSET:
            field_dict["no_select"] = no_select

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        addr = d.pop("addr")

        type = d.pop("type")

        prefer = d.pop("prefer", UNSET)

        no_select = d.pop("no_select", UNSET)

        ntp_server = cls(
            addr=addr,
            type=type,
            prefer=prefer,
            no_select=no_select,
        )

        ntp_server.additional_properties = d
        return ntp_server

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
