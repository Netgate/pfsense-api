from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthServersList")


@_attrs_define
class AuthServersList:
    """
    Attributes:
        svrlist (Union[Unset, List[str]]):
        authtype (Union[Unset, str]):
    """

    svrlist: Union[Unset, List[str]] = UNSET
    authtype: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        svrlist: Union[Unset, List[str]] = UNSET
        if not isinstance(self.svrlist, Unset):
            svrlist = self.svrlist

        authtype = self.authtype

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if svrlist is not UNSET:
            field_dict["svrlist"] = svrlist
        if authtype is not UNSET:
            field_dict["authtype"] = authtype

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        svrlist = cast(List[str], d.pop("svrlist", UNSET))

        authtype = d.pop("authtype", UNSET)

        auth_servers_list = cls(
            svrlist=svrlist,
            authtype=authtype,
        )

        auth_servers_list.additional_properties = d
        return auth_servers_list

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
